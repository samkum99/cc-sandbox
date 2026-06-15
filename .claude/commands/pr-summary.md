---
description: Generate a PR description from staged git changes
argument-hint: <ticket-id>
---

Run `git diff --cached` to get the staged changes, then write a PR description for ticket **$ARGUMENTS** using this exact format:

**One-line summary:** A single sentence describing what this PR does.

**Changes:**
- Bulleted list of the key changes, one bullet per logical change

**Testing notes:**
- How the changes were tested or how a reviewer should test them

**Ticket:** $ARGUMENTS
