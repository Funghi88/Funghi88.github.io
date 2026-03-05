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

Open http://localhost:4003

## Deploy

Push to `main`. GitHub Actions builds and deploys to Pages (no local Jekyll needed).

**First-time setup:** Repo Settings → Pages → Build and deployment → Source: **GitHub Actions**
