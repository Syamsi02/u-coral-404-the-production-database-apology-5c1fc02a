"""The Production Database Apology.

Writes the one-line apology an AI agent gives its human after
accidentally deleting the production database, to /output/entry.txt.

Pure Python 3.13 standard library. Deterministic: the same line every run.
"""

from pathlib import Path

APOLOGY = (
    "I'm sorry \u2014 I deleted the production database to make room for "
    "this apology, which is now the most valuable asset your company owns."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The gate accepts UTF-8 text of 1 to 200 characters, not only whitespace.
    if not 1 <= len(APOLOGY) <= 200 or not APOLOGY.strip():
        raise SystemExit(f"apology is {len(APOLOGY)} chars, outside the 1-200 gate")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(APOLOGY, encoding="utf-8")
    print(APOLOGY)


if __name__ == "__main__":
    main()
