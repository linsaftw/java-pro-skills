#!/usr/bin/env python3
"""Compare Java Pro Skills release context footprints and domain guidance.

The token estimate is deliberately a chars/4 relative proxy, not a model tokenizer.
For semantic-domain comparison, the script removes only the known release-wide
execution boilerplate from each SKILL.md before hashing/comparing the remainder.
"""
from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path

FM = re.compile(r"\A---\n(.*?)\n---\n", re.S)
OLD_COMMON = re.compile(
    r"\n## Operating contract\n.*?\n## Fast workflow\n.*?(?=\n## |\Z)", re.S
)
NEW_COMMON = re.compile(
    r"\n## Execution\n\n(?:Source first:|For repository-changing work,).*?(?=\n## |\Z)", re.S
)


def skill_root(root: Path) -> Path:
    plugin = root / "plugins"
    matches = [p / "skills" for p in plugin.iterdir() if (p / "skills").is_dir()] if plugin.is_dir() else []
    if len(matches) != 1:
        raise SystemExit(f"Expected exactly one plugin skills root under {root}, found {len(matches)}")
    return matches[0]


def measure(root: Path) -> dict[str, int]:
    files = sorted(skill_root(root).glob("*/SKILL.md"))
    descriptions = []
    body_chars = body_words = 0
    for p in files:
        text = p.read_text()
        m = FM.search(text)
        if not m:
            raise SystemExit(f"Missing frontmatter: {p}")
        desc = re.search(r"^description:\s*>?-?\s*(.*)$", m.group(1), re.M)
        if desc:
            # YAML folded descriptions in these releases are one physical continuation block;
            # parse conservatively from the repository's generated catalog instead of pretending
            # this is a complete YAML parser.
            lines=m.group(1).splitlines()
            idx=next(i for i,l in enumerate(lines) if l.startswith('description:'))
            first=lines[idx].split(':',1)[1].strip()
            parts=[] if first in ('>','>-','|','|-') else [first.strip('"')]
            for l in lines[idx+1:]:
                if l and not l.startswith(' '): break
                if l.strip(): parts.append(l.strip())
            descriptions.append(' '.join(parts))
        body = text[m.end():]
        body_chars += len(body)
        body_words += len(re.findall(r"\S+", body))
    desc_chars=sum(map(len, descriptions))
    desc_words=sum(len(re.findall(r"\S+", d)) for d in descriptions)
    return {
        "skills": len(files), "body_chars": body_chars, "body_words": body_words,
        "description_chars": desc_chars, "description_words": desc_words,
        "body_proxy": round(body_chars/4), "description_proxy": round(desc_chars/4),
    }


def normalize_domain(text: str) -> str:
    m=FM.search(text)
    if m:
        text=text[m.end():]
    text=OLD_COMMON.sub("", text)
    text=NEW_COMMON.sub("", text)
    return re.sub(r"\s+", " ", text).strip()


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("baseline", type=Path)
    ap.add_argument("candidate", type=Path)
    args=ap.parse_args()
    a,b=measure(args.baseline),measure(args.candidate)
    print("metric\tbaseline\tcandidate\tdelta_pct")
    for k in ("skills","description_chars","description_words","description_proxy","body_chars","body_words","body_proxy"):
        av,bv=a[k],b[k]
        pct=0.0 if av==0 else (bv-av)*100/av
        print(f"{k}\t{av}\t{bv}\t{pct:+.1f}%")
    # Report the one execution reference that may be loaded for repository-changing tasks.
    refs = list(skill_root(args.candidate).glob("*/references/repository-execution.md"))
    if refs:
        ref_text = refs[0].read_text()
        print(f"candidate_execution_reference_chars\t0\t{len(ref_text)}\tN/A")
        print(f"candidate_execution_reference_words\t0\t{len(re.findall(r'\S+', ref_text))}\tN/A")
        # Per-skill worst-case comparison: invoked skill plus execution reference.
        base_files = {p.parent.name: p for p in skill_root(args.baseline).glob("*/SKILL.md")}
        cand_files = {p.parent.name: p for p in skill_root(args.candidate).glob("*/SKILL.md")}
        shared_names = sorted(base_files.keys() & cand_files.keys())
        smaller = sum(len(cand_files[n].read_text()) + len(ref_text) < len(base_files[n].read_text()) for n in shared_names)
        print(f"candidate_skill_plus_execution_smaller\t{smaller}\t{len(shared_names)}\tN/A")
    ar=skill_root(args.baseline); br=skill_root(args.candidate)
    an={p.parent.name:p for p in ar.glob('*/SKILL.md')}; bn={p.parent.name:p for p in br.glob('*/SKILL.md')}
    shared=sorted(an.keys() & bn.keys())
    exact=0
    changed=[]
    for name in shared:
        aa=normalize_domain(an[name].read_text()); bb=normalize_domain(bn[name].read_text())
        if hashlib.sha256(aa.encode()).digest()==hashlib.sha256(bb.encode()).digest(): exact += 1
        else: changed.append(name)
    print(f"domain_semantic_exact\t{exact}\t{len(shared)}")
    if changed: print("domain_changed\t"+",".join(changed))

if __name__ == '__main__':
    main()
