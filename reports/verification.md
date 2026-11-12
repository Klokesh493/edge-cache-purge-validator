# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 purge_validator.py sample_purges.csv
prg-1: pass
prg-2: approval_required,rollback_note
test_global_purge_requires_approval (test_purge_validator.PurgeValidatorTest) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
````
