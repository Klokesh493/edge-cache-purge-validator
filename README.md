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
