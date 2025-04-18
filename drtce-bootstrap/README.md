# 📦 PCI DSS v4.0.1 DRTCE Bootstrap Kit

This folder includes a fully structured PCI DSS v4.0.1 dataset, optimized for loading into the **Dynamic Role-Task Coaching Engine (DRTCE)**.

---

## 📁 Included Files

| File | Description |
|------|-------------|
| `controls_registry.json` | Full set of PCI DSS sub-requirements, with tags, UUIDs, and cross-refs |
| `tasks_library.json` | Canonical task templates with descriptions and trigger prompts |
| `role_task_matrix.json` | Mapping of roles (e.g. AppSec, CISO) to associated control responsibilities |
| `deliverables_index.json` | List of expected evidence types mapped by tag |
| `load_pci_dss.py` | Python loader for all files – can be used in Jupyter, Streamlit, or DRTCE runtime |

---

## ✅ Integration Steps

1. Copy this folder into your DRTCE installation as `/frameworks/pci-dss-v4.0.1/`
2. Load via:
```python
from load_pci_dss import load_controls, load_roles, load_tasks, load_deliverables
controls = load_controls()
roles = load_roles()
```

3. Use these datasets to populate:
   - Coaching prompts
   - Role dashboards
   - Evidence validation modules
   - Weekly digest tracking

---

## 🔐 Notes

- UUIDs are consistent across controls
- Tags include both operational (`inference_tags`) and behavioral (`grc_subtags`)
- Role mappings and task structures are deduplicated and ready for coaching UX

For questions or version updates, refer to `pci-dss-v4.0.1-tagged-requirements-v4.8.1.zip`.
