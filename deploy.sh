#!/bin/bash
# One-liner GitHub Pages deploy (run inside repo)
git init && git add . && git commit -m "Deploy PCI DSS portal" && git branch -M main && git remote add origin <YOUR_GITHUB_REPO_URL> && git push -u origin main
echo "Now enable GitHub Pages: Settings → Pages → Source: main / root"
