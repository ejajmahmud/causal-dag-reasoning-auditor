"""Core Causal DAG Reasoning Auditor implementation."""
from typing import Dict, List, Set, Optional

class CausalEdge:
    def __init__(self, source: str, target: str):
        self.source = source
        self.target = target

class CausalVerdict:
    def __init__(self, is_valid_cause: bool, path: List[str], reason: str):
        self.is_valid_cause = is_valid_cause
        self.path = path
        self.reason = reason

class CausalDAGAuditor:
    def __init__(self):
        self.graph: Dict[str, List[str]] = {}

    def add_causal_relation(self, cause: str, effect: str):
        if cause not in self.graph:
            self.graph[cause] = []
        self.graph[cause].append(effect)

    def evaluate_causality(self, cause_node: str, effect_node: str) -> CausalVerdict:
        if cause_node not in self.graph:
            return CausalVerdict(False, [], f"No outgoing causal relationships defined from {cause_node}")

        visited: Set[str] = set()
        path: List[str] = []

        def dfs(curr: str) -> bool:
            path.append(curr)
            visited.add(curr)
            if curr == effect_node:
                return True
            for nxt in self.graph.get(curr, []):
                if nxt not in visited:
                    if dfs(nxt):
                        return True
            path.pop()
            return False

        found = dfs(cause_node)
        if found:
            return CausalVerdict(True, path, f"Valid causal chain found: {' -> '.join(path)}")
        else:
            return CausalVerdict(False, [], f"No directed causal path exists from {cause_node} to {effect_node}")
