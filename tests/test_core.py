"""Tests for CausalDAGAuditor."""
import unittest
from causal_dag_reasoning_auditor.core import CausalDAGAuditor

class TestCausalDAGAuditor(unittest.TestCase):
    def test_causal_evaluation(self):
        a = CausalDAGAuditor()
        a.add_causal_relation("A", "B")
        a.add_causal_relation("B", "C")

        v1 = a.evaluate_causality("A", "C")
        self.assertTrue(v1.is_valid_cause)
        self.assertEqual(v1.path, ["A", "B", "C"])

        v2 = a.evaluate_causality("C", "A")
        self.assertFalse(v2.is_valid_cause)
