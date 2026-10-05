#!/usr/bin/env python3
"""Measure skill routing/body context cost without depending on a model-specific tokenizer."""
from __future__ import annotations
from pathlib import Path
import argparse, re


def resolve_skills(root: Path) -> Path:
    if root.name == "skills" and root.is_dir():
        return root
    plugin_root = root / "plugins"
    matches = sorted(p / "skills" for p in plugin_root.iterdir() if (p / "skills").is_dir()) if plugin_root.is_dir() else []
    if len(matches) == 1:
        return matches[0]
    raise SystemExit(f"Expected one plugin skills directory under {root}, found {len(matches)}")


def metrics(root: Path) -> dict[str, float | int]:
    skills = resolve_skills(root)
    files = sorted(skills.glob("*/SKILL.md"))
    desc_chars = desc_words = body_chars = body_words = 0
    for path in files:
        text = path.read_text()
        m = re.search(r"^description:\s*(.*)$", text, re.M)
        if not m:
            raise SystemExit(f"Missing description: {path}")
        desc = m.group(1).strip()
        desc_chars += len(desc)
        desc_words += len(desc.split())
        body_chars += len(text)
        body_words += len(text.split())
    return {
        "skills": len(files),
        "description_chars": desc_chars,
        "description_words": desc_words,
        "skill_chars": body_chars,
        "skill_words": body_words,
        "avg_skill_words": round(body_words / len(files), 1),
        # Relative proxy only. Tokenization varies by model/content.
        "description_char4_proxy": round(desc_chars / 4),
        "skill_char4_proxy": round(body_chars / 4),
    }


def print_metrics(label: str, m: dict[str, float | int]) -> None:
    print(label)
    for key, value in m.items():
        print(f"  {key}: {value}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--compare", type=Path)
    args = parser.parse_args()
    current = metrics(args.root.resolve())
    print_metrics("current", current)
    if args.compare:
        base = metrics(args.compare.resolve())
        print_metrics("compare", base)
        for key in ("description_chars", "description_words", "skill_chars", "skill_words"):
            before = float(base[key]); after = float(current[key])
            delta = ((after - before) / before * 100.0) if before else 0.0
            print(f"  delta_{key}: {delta:+.1f}%")
    print("note: *_char4_proxy is a relative chars/4 proxy, not a Claude tokenizer count")

if __name__ == "__main__":
    main()
