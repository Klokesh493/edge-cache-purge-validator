import csv
import sys


def validate(row):
    issues = []
    if row["scope"].lower() == "global" and row["approved"].lower() != "yes":
        issues.append("approval_required")
    if not row["rollback_note"].strip():
        issues.append("rollback_note")
    return issues


def main(path):
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            issues = validate(row)
            print(f"{row['request_id']}: {'pass' if not issues else ','.join(issues)}")


if __name__ == "__main__":
    main(sys.argv[1])
