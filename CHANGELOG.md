# Changelog

## [Unreleased]

- build: migrate Poetry → uv, add ruff; require Python 3.12
- deps: major: mkdocs-table-reader-plugin 3→4, mkdocstrings 0.28→1.0, mkdocstrings-python 1→2, pytest 8→9 (fixes PYSEC-2026-1845)
- deps: minor: nzshm-common 0.9.4→0.10.1
- ci: publish.yml uses nshm-github-actions python-install-uv for Python+uv; bump checkout v7, configure-pages v6, upload-pages-artifact v5, deploy-pages v5
