"""
gradebook.py
------------
Reads grades.csv, groups scores per student,
computes average, and writes a report.txt.
"""

import csv
from pathlib import Path

CSV_FILE = Path(__file__).with_name("grades.csv")
REPORT_FILE = Path(__file__).with_name("report.txt")


def load_grades(filename: Path) -> dict[str, list[float]]:
    """Return {student_id: [scores]} dict."""
    data: dict[str, list[float]] = {}
    with filename.open(newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sid = row["student"].strip()
            score = float(row["score"])
            data.setdefault(sid, []).append(score)
    return data

def compute_averages(data: dict[str, list[float]]) -> dict[str, float]:
    """Return {student_id: average_score} dict."""
    return {sid: sum(scores) / len(scores) for sid, scores in data.items()}

def write_report(avgs: dict[str, float], outfile: Path) -> None:
    """Write averages to outfile, sorted by student id."""
    with outfile.open("w") as f:
        f.write("Student  Average\n")
        f.write("-----------------\n")
        for sid in sorted(avgs):
            f.write(f"{sid:7}  {avgs[sid]:.2f}\n")
    print(f"Wrote report to {outfile}")


def main() -> None:
    grades = load_grades(CSV_FILE)
    avgs = compute_averages(grades)
    write_report(avgs, REPORT_FILE)

# ---- sanity check ----------------------------------------------------------
assert abs(compute_averages({"X": [80, 100]})["X"] - 90) < 1e-9

# ---- script-vs-module guard -----------------------------------------------
if __name__ == "__main__":
    main()


