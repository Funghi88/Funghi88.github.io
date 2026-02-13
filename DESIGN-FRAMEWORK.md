# funghi88.github.io — Design Framework

Collaboration doc for AI + human alignment. References [Dense Discovery](https://www.densediscovery.com/) and [Linear Now](https://linear.app/now) aesthetics with our palette.

---

## Aesthetic Alignment

| Source | Takeaway |
|-------|----------|
| **Dense Discovery** | Newsletter-style clarity, strong typography hierarchy, generous whitespace, one clear font, subtle accent |
| **Linear Now** | Clean product blog, card-based content blocks, clear date/meta, minimal chrome |

**Our blend:** Editorial minimal + product-blog structure. Content leads. No clutter.

---

## 1️⃣ ASCII Wireframe

### Home Page

```
┌─────────────────────────────────────────────────────────────┐
│  [Site Title]                    [About] [Writing] [Connect] │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Annabelle Lee                                               │
│  AI-Native Product Architect                                 │
│  Frontier Web3 Research · Tooling · Design Systems           │
│                                                             │
│  ─────────────────────────────────────────────────────────  │
│                                                             │
│  I build structured systems...                               │
│                                                             │
│  ## Work                                                    │
│  • Protocol Intelligence                                    │
│  • Research Compression Frameworks                          │
│  ...                                                        │
│                                                             │
│  ## Writing                                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Phase I — Why Web3 Infrastructure Research           │   │
│  │ 2026-02-13 · excerpt...                              │   │
│  └─────────────────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ [Next post]                                           │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ## Connect                                                 │
│  GitHub · X                                                 │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  Footer — minimal                                           │
└─────────────────────────────────────────────────────────────┘
```

### Post Page

```
┌─────────────────────────────────────────────────────────────┐
│  [Site Title]                    [About] [Writing] [Connect] │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Post Title — aqua highlight bar                             │
│  2026-02-13 · 3 min read                                     │
│                                                             │
│  Body content with generous line-height...                   │
│                                                             │
│  ## Section                                                 │
│  More content. Code blocks in pink bg.                       │
│                                                             │
│  [← Back] or [Next →]                                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 2️⃣ Swimlane Diagram

### Content Publishing Flow

```
┌─────────────┬──────────────────────────────────────────────────────────┐
│ Author      │  Write → Save → Push → GitHub Pages builds                │
├─────────────┼──────────────────────────────────────────────────────────┤
│ Jekyll      │  ────────→ Parse YAML → Render layout → Output HTML       │
├─────────────┼──────────────────────────────────────────────────────────┤
│ Reader      │  ──────────────────────────────→ Visit → Read → Navigate │
└─────────────┴──────────────────────────────────────────────────────────┘
```

### Multi-Role (if adding Web3 later)

```
┌─────────────┬──────────────────────────────────────────────────────────┐
│ User        │  Click "Connect" → Approve wallet → View content         │
├─────────────┼──────────────────────────────────────────────────────────┤
│ Frontend    │  Request connect → Show address → Render gated content    │
├─────────────┼──────────────────────────────────────────────────────────┤
│ Wallet      │  Sign → Return address                                    │
└─────────────┴──────────────────────────────────────────────────────────┘
```

---

## 3️⃣ State Machine Diagram

### Nav / Mobile Menu (if added)

```
[Closed] ──click hamburger──→ [Open] ──click/outside──→ [Closed]
```

### Wallet Connect (future Web3)

```
[Disconnected] ──connect──→ [Connecting] ──success──→ [Connected]
     ↑                            │                        │
     └──────────fail/timeout──────┘                        │
     └────────────────disconnect──────────────────────────┘
```

### Page Load

```
[Loading] ──DOM ready──→ [Ready] ──navigate──→ [Loading]
```

---

## 4️⃣ Sequence Diagram

### Standard Page Load

```
User -> Browser: navigate to URL
Browser -> GitHub: fetch HTML
GitHub -> Browser: return static page
Browser -> User: render content
```

### Post Navigation

```
User -> Frontend: click post link
Frontend -> Browser: navigate (full page or SPA)
Browser -> User: show post
```

### Web3 Flow (future)

```
User -> Frontend: click Connect
Frontend -> Wallet: request signature
Wallet -> User: prompt approve
User -> Wallet: approve
Wallet -> Frontend: return address
Frontend -> Chain: (optional) verify
Chain -> Frontend: tx hash / verified
Frontend -> User: show connected state
```

---

## 5️⃣ Design Token Table

| Token | Value | Usage |
|-------|-------|-------|
| `bg` | #EFF7F5 | Page background |
| `text` | #3d4d4a | Body text |
| `heading` | #2a3a38 | H1, H2, post titles |
| `muted` | #5a6a67 | Meta, secondary text |
| `link` | #80D0ED | Links |
| `link-hover` | #5a9bb8 | Link hover |
| `accent-aqua` | #B8F3EB | Title highlight, borders |
| `accent-pink` | #F9DDDD | Code blocks |
| `accent-rose` | #F0BBDD | Optional accent |
| `space-4` | 16px | Base spacing unit |
| `space-8` | 32px | Section gaps |
| `radius-md` | 8px | Cards, buttons |
| `radius-sm` | 4px | Inline elements |
| `font-body` | 1rem | Body copy |
| `font-meta` | 0.9rem | Post meta |
| `line-height` | 1.7 | Body readability |

---

## 6️⃣ Component Tree Map

```
site
├── header
│   ├── site-title (link to home)
│   └── nav
│       ├── page-link (About)
│       ├── page-link (Writing)
│       └── page-link (Connect)
├── main
│   ├── home
│   │   ├── page-heading (h1)
│   │   ├── intro (markdown)
│   │   ├── section (Work)
│   │   ├── section (Writing)
│   │   │   └── post-list
│   │   │       └── post-list-item
│   │   │           ├── post-meta (date)
│   │   │           ├── post-link (title)
│   │   │           └── excerpt
│   │   └── section (Connect)
│   └── post
│       ├── post-header
│       │   ├── post-title
│       │   └── post-meta
│       ├── post-content (markdown)
│       └── post-nav (prev/next)
└── footer
```

---

## 7️⃣ Constraint Checklist

Before any visual/layout change:

- [ ] Grid consistent (multiples of 8px)
- [ ] Spacing multiple of 8
- [ ] Radius consistent (4px or 8px)
- [ ] Shadow consistent (or none)
- [ ] Typography scale consistent
- [ ] Light background only (#EFF7F5)
- [ ] Palette: 5 colors from spec (no new colors without updating table)
- [ ] Minima theme — override via `_sass/minima/` only
- [ ] No JS unless explicitly needed

---

## When to Use

| Need | Artifact |
|------|----------|
| Layout / structure | ASCII Wireframe |
| Multi-role flow | Swimlane Diagram |
| State (nav, wallet) | State Machine |
| Precise flow (Web3) | Sequence Diagram |
| Color / spacing | Design Token Table |
| Structure optimization | Component Tree Map |
| Before visual change | Constraint Checklist |

---

*Reference this doc when making changes. Keeps AI and human aligned.*
