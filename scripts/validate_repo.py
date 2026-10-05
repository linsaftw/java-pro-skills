#!/usr/bin/env python3
from __future__ import annotations
from collections import Counter
from pathlib import Path
import csv, json, re, sys

root = Path(__file__).resolve().parents[1]
skills = root / "plugins" / "java-pro-skills" / "skills"
errors: list[str] = []
name_re = re.compile(r"^[a-z0-9-]{1,64}$")

if not skills.is_dir():
    errors.append("missing canonical plugins/java-pro-skills/skills directory")
    skill_dirs = []
else:
    skill_dirs = sorted(d for d in skills.iterdir() if d.is_dir())

names: set[str] = set()
description_chars = 0
line_presence: Counter[str] = Counter()
for directory in skill_dirs:
    path = directory / "SKILL.md"
    if not path.exists():
        errors.append(f"missing SKILL.md: {directory.relative_to(root)}")
        continue
    text = path.read_text()
    if len(text.splitlines()) >= 500:
        errors.append(f"{directory.name}: SKILL.md >=500 lines")
    match = re.search(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        errors.append(f"{directory.name}: missing frontmatter")
        continue
    frontmatter = match.group(1)
    nm = re.search(r"^name:\s*(.+)$", frontmatter, re.M)
    ds = re.search(r"^description:\s*(.+)$", frontmatter, re.M)
    if not nm or not ds:
        errors.append(f"{directory.name}: missing name/description")
        continue
    name = nm.group(1).strip()
    desc = ds.group(1).strip()
    names.add(name)
    description_chars += len(desc)
    if name != directory.name:
        errors.append(f"{directory.name}: folder/name mismatch {name}")
    if not name_re.fullmatch(name):
        errors.append(f"{name}: invalid name")
    if "claude" in name or "anthropic" in name:
        errors.append(f"{name}: reserved word in skill name")
    if not desc or len(desc) > 220:
        errors.append(f"{name}: description must be 1..220 chars, got {len(desc)}")
    for bad in ("/mnt/data", "file_000000", "@gmail.com", "@outlook.com"):
        if bad.lower() in text.lower():
            errors.append(f"{name}: forbidden/private marker {bad}")
    for link in re.findall(r"\[[^\]]+\]\((references/[^)#]+)", text):
        if not (directory / link).exists():
            errors.append(f"{name}: broken reference {link}")
    # Detect future boilerplate growth: repeated prose is metadata/context cost when invoked.
    for line in set(text.splitlines()):
        stripped = line.strip()
        if len(stripped) >= 90 and not stripped.startswith("description:"):
            line_presence[stripped] += 1

if len(skill_dirs) != 33:
    errors.append(f"expected 33 skills, found {len(skill_dirs)}")
if description_chars > 6000:
    errors.append(f"routing metadata budget exceeded: {description_chars} description chars > 6000")
for line, count in line_presence.items():
    if count >= 10 and not (line.startswith("Source first:") or line.startswith("For repository-changing work,")):
        errors.append(f"repeated long prose in {count} skills: {line[:100]}...")


# Progressive-disclosure execution reference must exist and stay identical across all skills.
execution_refs = []
for directory in skill_dirs:
    ref = directory / "references" / "repository-execution.md"
    if not ref.exists():
        errors.append(f"{directory.name}: missing references/repository-execution.md")
        continue
    ref_text = ref.read_text()
    execution_refs.append(ref_text)
    words = len(ref_text.split())
    if not 100 <= words <= 180:
        errors.append(f"{directory.name}: repository-execution reference must stay compact (100..180 words), got {words}")
    skill_text = (directory / "SKILL.md").read_text() if (directory / "SKILL.md").exists() else ""
    if "[references/repository-execution.md](references/repository-execution.md)" not in skill_text:
        errors.append(f"{directory.name}: SKILL.md does not route repository-changing work to execution reference")
if execution_refs and len(set(execution_refs)) != 1:
    errors.append("repository-execution reference drifted across skills")

# Plugin/marketplace identities and version must agree.
version = (root / "VERSION").read_text().strip()
try:
    plugin = json.loads((root / "plugins/java-pro-skills/.claude-plugin/plugin.json").read_text())
    if plugin.get("name") != "java-pro-skills": errors.append("plugin.json name must be java-pro-skills")
    if plugin.get("version") != version: errors.append("plugin.json version != VERSION")
except Exception as exc:
    errors.append(f"plugin.json invalid: {exc}")
try:
    market = json.loads((root / ".claude-plugin/marketplace.json").read_text())
    if market.get("name") != "java-pro-skills": errors.append("marketplace name must be java-pro-skills")
    if market.get("version") != version: errors.append("marketplace version != VERSION")
    entries = market.get("plugins", [])
    if len(entries) != 1:
        errors.append("marketplace must contain exactly one plugin")
    else:
        entry = entries[0]
        if entry.get("name") != "java-pro-skills": errors.append("marketplace plugin identity mismatch")
        if entry.get("source") != "./plugins/java-pro-skills": errors.append("marketplace plugin source mismatch")
        if "version" in entry: errors.append("marketplace entry must not duplicate plugin.json version")
except Exception as exc:
    errors.append(f"marketplace.json invalid: {exc}")

# Routing corpus: at least two positive realistic prompts per skill.
routing = root / "evals/routing.tsv"
counts: Counter[str] = Counter()
try:
    with routing.open(newline="") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            skill = row["skill"]
            if skill not in names: errors.append(f"routing.tsv unknown skill: {skill}")
            if row["expected"] != "activate": errors.append(f"routing.tsv invalid expected for {skill}")
            counts[skill] += 1
    for name in names:
        if counts[name] < 2: errors.append(f"routing.tsv needs >=2 cases for {name}")
except Exception as exc:
    errors.append(f"routing.tsv invalid: {exc}")

overlap = root / "evals/routing-overlap.tsv"
try:
    with overlap.open(newline="") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            expected, avoid = row["expected_skill"], row["avoid_skill"]
            if expected not in names: errors.append(f"routing-overlap unknown expected skill: {expected}")
            if avoid not in names: errors.append(f"routing-overlap unknown avoid skill: {avoid}")
            if expected == avoid: errors.append(f"routing-overlap expected==avoid: {expected}")
except Exception as exc:
    errors.append(f"routing-overlap.tsv invalid: {exc}")

# Privacy scan whole public repo except this validator's literal deny-list.
for path in root.rglob("*"):
    if not path.is_file() or path.name == "validate_repo.py":
        continue
    if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".zip", ".gz", ".jar"}:
        continue
    text = path.read_text(errors="ignore").lower()
    for bad in ("/mnt/data", "file_000000"):
        if bad in text: errors.append(f"{path.relative_to(root)}: private marker {bad}")

if errors:
    print("VALIDATION FAILED")
    for error in errors:
        print("-", error)
    sys.exit(1)
print(f"VALIDATION PASS: {len(skill_dirs)} skills; routing metadata={description_chars} chars")
