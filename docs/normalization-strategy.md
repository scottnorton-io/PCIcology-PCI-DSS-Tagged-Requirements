# 🧠 Normalization Strategy – v4.6.8

## 🎯 Goals
- Reduce duplicate narrative prompts
- Consolidate evidence object references
- Enable canonical task template reuse
- Support optimized frontend UI rendering

## ✅ Action Items

### 1. Canonical Task Templates
- Create reusable `task_id` references
- Abstract common roles, frequencies, evidence

### 2. Prompt Deduplication
- Use `{placeholder}` style format strings
- Tie prompt to `task_id` where relevant

### 3. Evidence Normalization
- Tag common evidence bundles (e.g. `incident_logs`, `change_logs`)
- Map these to tasks using a shared object schema

### 4. Role-Based Filtering
- Leverage RACI data to enable "Show all AppSec tasks"

---
