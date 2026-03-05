# Annabelle Lee's Space

AI-Native Research & Web3 Systems. Built with Jekyll.

## Local preview

Uses Ruby 3.1 with Bundler 2.3. First-time setup (run each command separately):

```bash
rbenv install 3.1.4
rbenv local 3.1.4
gem install bundler:2.3.26
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
