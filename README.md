# Owl Lab Website Maintenance Guide

This is the bilingual Owl Lab website built with Quarto. Chinese is served from the root; English mirrors live under `en/`.

## Preview and render

From the repository root:

```sh
./scripts/preview.sh
```

Open <http://127.0.0.1:4321/>. The script runs `quarto preview` and refreshes the browser after source changes.

Create the complete production output with:

```sh
quarto render
```

Rendered files are written to `_site/`. Check internal source links and Chinese/English mirrors with:

```sh
python3 scripts/check-links.py
```

## Where content lives

| Content | Current source files |
|---|---|
| Chinese homepage | `index.qmd` |
| English homepage | `en/index.qmd` |
| Chinese Research overview | `research/index.qmd` |
| English Research overview | `en/research/index.qmd` |
| Research threads | `research/space-process/index.qmd`, `research/human-environment/index.qmd`, `research/sensing-modelling/index.qmd` |
| English research threads | Matching paths under `en/research/` |
| Chinese Notebook | `notebook/index.qmd` |
| English Notebook | `en/notebook/index.qmd` |
| Chinese People | `people.qmd` |
| English People | `en/people.qmd` |
| Chinese News | `news.qmd` |
| English News | `en/news.qmd` |
| Chinese About page | `about/index.qmd` |
| English About page | `en/about/index.qmd` |

When changing bilingual content, update the corresponding root and `en/` sources together. The English Notebook is intentionally shorter at present.

## Structured records

- People records: `data/people.yml`; field guide: `templates/person.yml`
- News records: `data/news.yml`; field guide: `templates/news.yml`
- Current project records: `data/projects.yml`; field guide: `templates/project.yml`. The People page currently exposes only each project's public title, period, broad summary, and member IDs; the schema leaves room for a future standalone `/projects/` route without adding it to navigation yet.
- Publication records: `data/publications.yml`; field guide: `templates/publication.yml`

These YAML files are retained as the structured-content foundation, but current QMD pages do not yet import them automatically. Until a template pipeline is added, visible People and News changes must also be made in their QMD pages. Projects and publications can be prepared in the YAML files, but they will not appear on the rendered site without a corresponding QMD/template integration.

## Site-wide controls

- `_quarto.yml` controls the explicit render list, site metadata, navigation, bilingual routing behavior, footer, favicon, HTML options, and output directory.
- `styles.scss` controls design tokens, typography, colors, spacing, grids, Notebook layout, research accents, and responsive behavior.
- `AGENTS.md` contains contributor rules that automated coding assistants and maintainers should follow.
- `DESIGN_BRIEF.md` records the approved identity, architecture, editorial conventions, and visual principles.
- `scripts/preview.sh` starts the standard local preview on port 4321.
- `scripts/check-links.py` validates source links and required English mirrors.

## Generated files

Never edit these manually:

- `.quarto/` — Quarto working cache
- `_site/` — generated website output
- `**/*.quarto_ipynb` — generated notebook intermediates

They are all ignored by `.gitignore`. `_site/` should remain ignored: `.github/workflows/publish.yml` renders the source on GitHub Actions and publishes the result to the `gh-pages` branch, so generated output does not belong on `main`.

## Small content-update workflow

1. Update the relevant Chinese QMD/YAML source and its `en/` mirror where applicable.
2. Run `./scripts/preview.sh` and inspect the changed pages at desktop and mobile widths.
3. Run `quarto render`.
4. Run `python3 scripts/check-links.py`.
5. Review the changes with `git diff` and confirm that `_site/` and `.quarto/` are absent.
6. Commit only source changes: `git add <files>`, `git commit -m "Describe the content update"`, then `git push`.

This working folder is not currently recognized as a Git repository. The Git steps above apply after working in the actual cloned repository or after repository metadata is restored; do not initialize or reconnect it without confirming the intended remote first.

## LEGACY_AUDIT

No files were deleted, moved, or renamed during this audit.

| Suspected legacy source | Rendered now? | In `_quarto.yml`? | Linked from current pages? | Current dependency | Later removal assessment |
|---|---:|---:|---:|---|---|
| `about.qmd` | No | No | No | None found; it is distinct from the active `about/index.qmd` route | Appears safe to remove after review; reflects the earlier personal-site architecture. |
| `publications.qmd` | No | No | No | Mentions `data/publications.yml`, but no code imports the page | Page appears safe to remove after review; retain `data/publications.yml` and `templates/publication.yml` for planned structured content. |
| `teaching.qmd` | No | No | No | None found | Appears safe to remove after review; Teaching is no longer in the approved architecture. |
| `group/index.qmd` | No | No | No | Links only within the obsolete Group structure; one relative People target is not present inside `group/` | Appears safe to remove after review. Current People and News pages replace its function. |
| `group/join.qmd` | No | No | No | None found outside `group/` | Appears safe to remove after review; current Join Us content belongs within `people.qmd`. |
| `zh-cn/` (five QMD files) | No | No | No | None found | Appears safe to remove after review. It belongs to the former English-root/Chinese-subdirectory routing; Chinese now lives at root. |

Other reviewed files:

- `data/*.yml` and `templates/*.yml` are currently unconsumed by rendered pages, but they support the approved structured-content direction and should be retained.
- `assets/favicon.svg`, `scripts/preview.sh`, `scripts/check-links.py`, `.github/workflows/publish.yml`, `AGENTS.md`, and `DESIGN_BRIEF.md` are active maintenance or build infrastructure, not legacy material.
