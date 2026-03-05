#!/bin/bash
# Kill any existing Jekyll on port 4003, then start fresh
eval "$(rbenv init -)" 2>/dev/null || true
python3 scripts/generate-og-cards.py 2>/dev/null || true
ruby scripts/generate-en-posts.rb 2>/dev/null || true
lsof -ti:4003 | xargs kill 2>/dev/null
bundle exec jekyll serve --port 4003
