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

Rendered files are written to `_site/`. Check the source links and Chinese/English mirrors covered by the maintenance script with:

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
| Chinese Join Us page | `join/index.qmd` |
| English Join Us page | `en/join/index.qmd` |

When changing bilingual content, update the corresponding root and `en/` sources together. The English Notebook is intentionally shorter at present.

## Structured records

- People records: `data/people.yml`; field guide: `templates/person.yml`
- News records: `data/news.yml`; field guide: `templates/news.yml`
- Current project records: `data/projects.yml`; field guide: `templates/project.yml`. Current project summaries and members are maintained directly in `people.qmd` and `en/people.qmd`; there is no standalone `/projects/` route.
- Publication records: `data/publications.yml`; field guide: `templates/publication.yml`

These YAML files provide structured records and field guides, but current QMD pages do not import them automatically. Visible People, project, and News changes must be made in their QMD pages as well as the corresponding records. Publication records have no dedicated rendered page. The root-level `news.yml` also exists, but is not imported by the current QMD pages.

## Site-wide controls

- `_quarto.yml` controls the explicit render list, site metadata, navigation, bilingual routing behavior, footer, favicon, HTML options, and output directory.
- `styles.scss` controls design tokens, typography, colors, spacing, grids, Notebook layout, research accents, and responsive behavior.
- `scripts/preview.sh` starts the standard local preview on port 4321.
- `scripts/check-links.py` checks local Markdown links and English mirrors for the homepage, Research overview, People, Notebook, News, and About pages. Research thread and Join Us pages are not included in its explicit page list.

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
5. Review the changes with `git diff` and `git status --short`; confirm that generated `_site/` and `.quarto/` files are not staged.
6. Commit only source changes: `git add <files>`, `git commit -m "Describe the content update"`, then `git push`.

## Publishing

`.github/workflows/publish.yml` runs on pushes to `main` and can also be started manually with `workflow_dispatch`. It checks out the repository, installs Quarto, and uses the Quarto publish action with `target: gh-pages` and `GITHUB_TOKEN` to render and publish the site. The workflow does not run `scripts/check-links.py`, so run that check locally before pushing.

`_quarto.yml` sets the site URL to `https://owllab.space/` and includes `CNAME` in the published resources for the custom domain. Keep these settings consistent when maintaining publication.
