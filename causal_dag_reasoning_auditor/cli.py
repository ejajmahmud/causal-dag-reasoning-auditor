"""CLI for Causal DAG Reasoning Auditor."""
import argparse
from .core import CausalDAGAuditor

def main():
    parser = argparse.ArgumentParser(description="Causal DAG Reasoning Auditor CLI")
    parser.add_argument("--demo", action="store_true", help="Run causal DAG verification demo")
    args = parser.parse_args()

    auditor = CausalDAGAuditor()
    auditor.add_causal_relation("memory_leak", "high_memory_usage")
    auditor.add_causal_relation("high_memory_usage", "oom_kill")
    auditor.add_causal_relation("oom_kill", "service_downtime")

    res = auditor.evaluate_causality("memory_leak", "service_downtime")
    print("Claim: Memory leak caused service downtime.")
    print("Verdict:", res.is_valid_cause)
    print("Path:", res.reason)

if __name__ == "__main__":
    main()
