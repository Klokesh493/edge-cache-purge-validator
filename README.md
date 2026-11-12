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

```mermaid
flowchart LR
    A["Purge request CSV"]
    B["Check approval for global scope and require rollback notes"]
    C{"Validation issues present?"}
    D["Report missing approval or rollback notes"]
    E["Request passes the local checks"]
    A --> B --> C
    C -->|Yes| D
    C -->|No| E
```

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)
