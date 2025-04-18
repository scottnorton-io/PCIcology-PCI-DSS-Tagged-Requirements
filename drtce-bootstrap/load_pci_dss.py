"""
PCI DSS Loader Script for DRTCE Integration
"""

import json
from pathlib import Path

def load_controls(path="controls_registry.json"):
    return json.loads(Path(path).read_text())

def load_tasks(path="tasks_library.json"):
    return json.loads(Path(path).read_text())

def load_roles(path="role_task_matrix.json"):
    return json.loads(Path(path).read_text())

def load_deliverables(path="deliverables_index.json"):
    return json.loads(Path(path).read_text())
