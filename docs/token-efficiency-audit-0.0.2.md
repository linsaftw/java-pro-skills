# 0.0.2 token-efficiency audit

This release optimizes the two Claude Code skill costs separately: routing metadata that is present before activation, and full skill instructions loaded only when a skill is used. Claude Code documents that automatically invocable skill names/descriptions are in context every turn while full skill text loads on use.

The numbers below are deterministic repository measurements, not claims about Anthropic's tokenizer. `chars/4` is only a stable relative comparison proxy.

## Before / after

| Metric | 0.0.1 | 0.0.2 | Change |
|---|---:|---:|---:|
| skills | 33 | 33 | 0% |
| description characters | 10,300 | 5,586 | -45.8% |
| description words | 1,183 | 645 | -45.5% |
| description chars/4 proxy | 2,575 | 1,396 | -45.8% |
| skill-body characters, excluding frontmatter | 79,884 | 48,722 | -39.0% |
| skill-body words, excluding frontmatter | 10,616 | 6,243 | -41.2% |
| skill-body chars/4 proxy | 19,971 | 12,180 | -39.0% |

## What was removed

0.0.1 repeated the same seven-rule operating contract and the same workflow in all 33 skills. That repetition did not add domain information after activation. 0.0.2 replaces it with one compact execution paragraph retaining the important invariants:

- inspect source and locked versions first;
- verify version-sensitive APIs in official target-version docs;
- preserve declared compatibility;
- reuse existing owners before adding abstractions;
- make the smallest complete change;
- surface failure instead of faking success;
- run the repository-proven verification gate.

Descriptions were rewritten as routing predicates: domain + key discriminators + activation condition. SEO/discovery phrases stay in repository docs instead of consuming every-turn skill metadata.

## Semantic recovery pass

After trimming, every 0.0.2 skill was compared to its 0.0.1 counterpart after removing only the known release-wide boilerplate and normalizing whitespace. Before target-version corrections, **33/33 domain bodies were exact matches**. After current-version research, **32/33 remain exact**; the only changed domain body is `developing-android`, where the stale AGP 9.2 snapshot was corrected to the verified AGP 9.4/API 37 baseline. This proves the optimization removed duplicated execution prose rather than substantive domain guidance.

A second pass then re-read the reduced bodies and restored/retained cross-cutting guarantees in the compact execution paragraph. Version research was reapplied afterward; any resulting domain diff is therefore an intentional factual correction, not a trimming loss.

Run the comparison yourself:

```bash
python3 scripts/compare_release.py /path/to/0.0.1 /path/to/0.0.2
```

## Guardrails against future bloat

`validate_repo.py` now fails when:

- total routing descriptions exceed the release metadata budget;
- a description exceeds 220 characters;
- long prose is copied across many skills;
- skill/reference links break;
- routing coverage is missing;
- plugin/marketplace identity drifts;
- public files contain known private-path/file-ID markers.

`evals/routing-overlap.tsv` adds close-neighbor negative routing cases so future compression cannot simply make every description vague and keyword-heavy.

## Decision

Keep 33 skills for 0.0.2. Merging more would reduce metadata further but would also collapse distinct task intents (for example general Minecraft plugins vs Folia scheduling vs packet engineering). The larger remaining optimization opportunity is better routing wording and selective references, not fewer domains.
