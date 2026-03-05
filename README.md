# Annabelle Lee's Space

AI-Native Research & Web3 Systems. Built with Jekyll.

## Local preview

Uses Ruby 3.1 (required by github-pages gem):

```bash
rbenv install 3.1.4   # if needed
bundle install
bundle exec jekyll serve
```

Open http://localhost:4000

## Deploy

Push to `main`. GitHub Actions builds and deploys to Pages (no local Jekyll needed).

**First-time setup:** Repo Settings → Pages → Build and deployment → Source: **GitHub Actions**
