# funghi88.github.io — Design Spec

Shared reference for design decisions. Update when we change things.

---

## Design Token Table

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

---

## Component Tree

```
site
├── header (nav, site-title)
├── main
│   ├── home
│   │   ├── page-heading (h1)
│   │   ├── content (markdown)
│   │   └── post-list
│   │       └── post-list-item (post-meta, post-link, excerpt)
│   └── post
│       ├── post-header (post-title, post-meta)
│       └── post-content
└── footer
```

---

## Constraint Checklist

- [ ] Light background only (#EFF7F5)
- [ ] Palette: 5 colors from spec (no new colors without updating table)
- [ ] Minima theme — override via `_sass/minima/` only
- [ ] No JS unless explicitly needed

---

## When to Use

| Need | Artifact |
|------|----------|
| Color change | Design Token Table |
| Layout / structure | Component Tree |
| Flow / UX | Sequence Diagram |
| State (e.g. nav open) | State Machine |
| Rules | Constraint Checklist |

---

## Related

- **DESIGN-FRAMEWORK.md** — Full collaboration doc: ASCII wireframes, swimlanes, state machines, sequence diagrams, token table, component tree, constraint checklist. Dense Discovery + Linear aesthetics with our palette.

---

*Yes — using these keeps us aligned. I'll reference this spec when we make changes.*
