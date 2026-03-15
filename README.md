# Annabelle Lee's Space

AI-Native Research & Web3 Systems. Built with Jekyll.

## Local preview

Uses Ruby 3.3 with Bundler 4.0. First-time setup (run each command separately):

```bash
rbenv install 3.3.10
rbenv local 3.3.10
gem install bundler:4.0.3
bundle install
```

Then start the server:

```bash
./serve.sh
```

Open [http://localhost:4003](http://localhost:4003)

## Deploy

Push to `main`. GitHub Actions builds and deploys to Pages (no local Jekyll needed).

**First-time setup:** Repo Settings → Pages → Build and deployment → Source: **GitHub Actions**

### Commit and push to GitHub

```bash
git add .
git commit -m "Your commit message"
git push origin main
```

To commit and push only the latest post:

```bash
git add _posts/2026-03-15-openclaw-token-economics.md
git commit -m "Your commit message"
git push origin main
```

### Undo the last commit (keep your file changes)

If you committed by mistake (e.g. included `_site/` or wrong files):

```bash
git reset HEAD~1
```

This removes the last commit and unstages everything; your edits stay in the working directory. Then add only the files you want and commit again. Do **not** run this after you have already pushed (use with care).

