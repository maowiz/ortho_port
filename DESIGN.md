# Design System — Prof. Dr. Naseer Ahmad Chaudhary

A premium, trustworthy medical aesthetic: **a light, scroll-driven anatomy hero flowing into a clean, clinical
light body, with deep-navy accent bands** (page headers, call-to-action, footer). Built to feel authoritative and
calm — and to load fast on phones.

## Colour palette

| Token | Hex | Use |
|-------|-----|-----|
| `--primary` | `#1366C2` | Primary medical blue — buttons, links, active states |
| `--primary-light` / `--primary-dark` | `#2E86DE` / `#0E4E96` | Gradients, hovers |
| `--secondary` (ink navy) | `#0A2540` | Headings, dark bands, footer |
| `--gold` | `#C2A14D` | Prestige accents only (credentials, awards, stars) — used sparingly |
| `--accent` (teal) | `#0FA39A` | Occasional secondary highlight |
| `--bg` / `--bg-alt` | `#F4F7FB` / `#EAF1F8` | Page background / alternating sections |
| `--bg-card` | `#FFFFFF` | Cards |
| `--text` / `--text-bright` | `#33455A` / `#0A2540` | Body text / headings |
| `--text-secondary` / `--text-muted` | `#5E7186` / `#93A1B2` | Sub-text, captions |
| `--success` / `--whatsapp` | `#1FA971` / `#25D366` | Status / WhatsApp |

All colours are CSS variables in `:root` (top of the `<style>` block in `index.html`). Changing a token re-themes
the whole site, because every component and most inline styles reference these variables.

## Typography

- **Headings:** `Playfair Display` (serif) — authoritative, elegant. Weights 400/700.
- **Body / UI:** `Inter` (sans) — clean, highly legible. Weights 300–800.
- Loaded from Google Fonts with `display=swap` (system-font fallback while loading).
- Scale: hero `clamp(2.4rem, 6.5vw, 4.9rem)`, section titles `clamp(1.85rem, 4vw, 2.85rem)`, body 16–18px, line-height ~1.7.

## Spacing, radius, shadow

- Section vertical rhythm: `--space-section: clamp(64px, 8.5vw, 116px)`; max content width `--max-w: 1240px`.
- Radii: `--radius-sm 10px`, `--radius 16px`, `--radius-lg 24px`, `--radius-full` (pills).
- Shadows are soft and navy-tinted (`--shadow`, `--shadow-lg`, …) for a light, premium feel.

## Motion

- **Hero:** GSAP `ScrollTrigger` pins the hero and scrubs a 120-frame WebP image sequence (muscle → bone) as you scroll;
  three text "phases" cross-fade with progress.
- **Scroll reveals:** elements with `.reveal` fade-and-rise via `IntersectionObserver` (`.reveal.visible`).
- **Counters:** stat numbers count up when scrolled into view.
- **Micro-interactions:** subtle card lifts, button hovers, animated WhatsApp/Call pings.
- **Accessibility:** all of the above are disabled/short-circuited under `prefers-reduced-motion: reduce`
  (the hero shows a single static frame instead of pinning).

## Components (CSS class contract)

Navigation (`.nav`, `.nav-links`, `.mobile-nav`), buttons (`.btn` + `.btn-primary/-outline/-ghost/-white/-whatsapp/-call`),
hero (`.hero-phase`, `.hero-badge-inline`, `.hero-scroll`), cards (`.card`, `.card-icon` with inline SVG, `.service-card`,
`.testimonial-card`, `.result-card`), `.timeline`, `.faq-item`, `.stats-bar`, dark bands (`.page-hero`, `.cta-section`,
`.footer`), floating actions (`.floating-btn`), admin (`.admin-*`), modal/toast.

Icons are inline SVG from the `ICONS` map in the script (themeable, crisp, zero extra requests).

## Responsive

Mobile-first. Breakpoints at 1024 / 860 / 640 px collapse grids (3→2→1), swap the nav for a hamburger drawer,
and re-stack the footer. The hero canvas drops to device-pixel-ratio 1 and loads every 2nd frame on phones.
