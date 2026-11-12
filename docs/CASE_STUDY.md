# Edge Cache Purge Validator walkthrough

## Business problem

Validates cache purge requests for scope, approval, and rollback notes.

## Reproduce the workflow

Run `python3 purge_validator.py sample_purges.csv` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
prg-1: pass
prg-2: approval_required,rollback_note
```

The sample supplies these fields. `request_id`, `scope`, `approved`, `rollback_note`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
