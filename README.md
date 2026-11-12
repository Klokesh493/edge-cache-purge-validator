# Edge Cache Purge Validator

Validates cache purge requests for scope, approval, and rollback notes.

Focus: Telecom DevOps edge operations.

Built as a small, runnable Python project with clear input, output, sample data, and tests.

## Run

```bash
python3 purge_validator.py sample_purges.csv
```

## Verify

```bash
python3 -m unittest discover . -v
```

## Local verification

Run `make verify` with Make and Python 3 installed. The target runs the documented sample through the project CLI. It also runs the existing Python unit tests.

## Project walkthrough

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)
