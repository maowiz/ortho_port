# Orthopaedic Practice Website — single-file, mobile-first, zero build

> A production-grade sample website for a medical practice (orthopaedic surgeon), engineered as **one self-contained `index.html`** — no framework, no build step, no server. Total weight ≈ 2.5 MB with a cinematic scroll animation, first paint stays light.

## Highlights

- **📄 Single-file architecture** — all HTML, CSS, and JS inline in `index.html`. Deploy = copy one file anywhere (any static host, even a USB stick)
- **🎬 Scroll-driven hero animation** — 120 pre-rendered WebP frames (~1.8 MB) scrubbed by scroll position, the "expensive agency site" effect with zero JavaScript dependencies
- **📱 Mobile-first design system** — documented in `DESIGN.md`; consistent tokens for type, spacing, and color
- **⚙️ Built-in admin panel** — non-technical content editing (profile, stats, testimonials, clinic details) directly in the browser, persisted to localStorage — the client updates their own site without touching code
- **🗺️ Practice-site essentials** — clinic locations with map directions, WhatsApp/call actions, qualifications, patient testimonials, services

## Why single-file?

Small practices don't have DevOps. This architecture means:

| Concern | Answer |
|---|---|
| Hosting cost | any free static host |
| Build pipeline | none |
| Maintenance | edit content in the built-in admin panel |
| Performance | no framework payload; images lazy-loaded; ~2.5 MB total |
| Portability | one file + two asset folders |

## Structure

```
index.html    ← the entire site (markup + styles + logic)
frames/       ← 120 WebP frames for the scroll animation (~1.8 MB)
images/       ← photos & assets (~0.5 MB)
DESIGN.md     ← design system notes
```

## Tech

`HTML5` · `CSS3` · `Vanilla JavaScript` · `WebP frame animation` · `localStorage persistence` — deliberately dependency-free.

---

**Muhammad Maowiz Saleem** — [GitHub](https://github.com/maowiz) · [LinkedIn](https://linkedin.com/in/muhammad-maowiz-saleem) · maowizsaleem009@gmail.com
*More web work: [Portfolio](https://github.com/maowiz/My_Portfolio) ([live](https://maowiz.github.io/My_Portfolio/))*
