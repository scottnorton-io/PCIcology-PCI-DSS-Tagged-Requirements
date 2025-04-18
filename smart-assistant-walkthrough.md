# Smart Assistant Walkthrough for PCI DSS v4.0.1

This document outlines how an assistant might guide a user through PCI DSS compliance using the JSON dataset.

## 📌 Step-by-Step Interaction Model

1. **Start with Scope Detection**
   - Ask: "Is cardholder data stored, processed, or transmitted in this environment?"
   - If yes → load relevant sub-requirements based on `"cde-scope"` tag.

2. **Role Assignment**
   - Prompt: "Who on your team handles network architecture?"
   - Match to tags: `architect`, `developer`, etc.

3. **Show Requirements Per Role**
   - Display table with `req_id`, `title`, and `inference_tags` filtered by their role.

4. **Evidence Collection Guidance**
   - Surface all `"artifact"` or `"policy"` tagged sub-requirements for that team.

5. **AI Reminders**
   - Flag any `task-blocked`, `needs-human-validation`, or `evidence-missing`.

## 🧠 Uses Inference Tags

This flow uses:
- Contextual routing (`cde-scope`, `realtime`, `periodic`)
- Evidence prompts (`artifact`, `report`)
- Dynamic advisor follow-ups

Ready for integration with GPT-based interfaces or Notion buttons.
