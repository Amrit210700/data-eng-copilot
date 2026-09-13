"""Day 17 entrypoint: run the eval harness against the golden set.

Usage: python scripts/run_eval.py
Intended to be wired into CI as a regression gate.
"""

from app.eval.golden_set import load_golden_set
from app.eval.harness import run_eval

if __name__ == "__main__":
    golden_set = load_golden_set()
    report = run_eval(golden_set)
    print(report)
