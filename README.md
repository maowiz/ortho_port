# Prof. Dr. Naseer Ahmad Chaudhary — Website

A fast, mobile-first, single-file website for Prof. Dr. Naseer Ahmad Chaudhary
(Professor & Head of Orthopaedics, Bahawal Victoria Hospital, Bahawalpur).

- **One file to ship:** `index.html` (all HTML, CSS and JS inline).
- **Assets:** `frames/` (the scroll animation, 120 WebP frames ≈ 1.8 MB) and `images/` (≈ 0.5 MB).
- **No build step, no server needed.** Total weight ≈ 2.5 MB; first paint is light.
- See `DESIGN.md` for the design system.

---

## ✅ Real details now in the site

- **Two clinics** (Contact page + footer): **Bahawalpur** — 10‑A, Lane 2, Medical Colony, BVH (Mon–Fri 4–10 PM, **+92 345 9678595**); **Rahim Yar Khan** — 1‑A Model Town, Shaikh Zaid Hospital Road (Sunday 10 AM–5 PM, **+92 300 8674595**).
- **Primary WhatsApp / Call / nav** number: **+92 300 8674595** (RYK). Map "Get Directions" → his Google Maps pin.
- **Professional photos** (AI): home intro, About bio, About banner.
- Qualifications/positions (MBBS AIMC, FCPS, CHPE, AO Trauma; HOD BVH, Visiting Prof QAMC, Ex‑HOD SZMC RYK) + 4.9/5 / 780+ reviews + languages.

## ⚠️ Still optional / to confirm

| What | Status | Where to change |
|------|--------|-----------------|
| **Email** | none yet (Email button removed; add when available) | Admin → Profile, then re‑add to Contact/footer |
| **Stats** | placeholders: 25+ yrs, 10,000+ procedures, 98% | Admin → Surgeon Profile (set real, honest numbers) |
| **Patient reviews** | sample testimonials | Admin → Testimonials |
| **Primary number** | currently RYK (+92 300 8674595) | to make Bahawalpur primary, find/replace `923008674595`→`923459678595` and `+92 300 8674595`→`+92 345 9678595` |

> Please double‑check the qualifications/positions for accuracy.

### Replacing the photo
A real, professional photo (ideally a clinic/formal head-and-shoulders shot) makes a big difference.
Save it as **`images/doctor-portrait.jpg`** (portrait orientation, roughly 4:5, ≤ ~300 KB).
*(The 6 images currently in `profile/` are casual travel photos and are not used — a proper clinical photo is recommended.)*

---

## ✏️ Editing content (Admin panel)

1. Open the site and click the **⚙ button** (bottom-right) or press **Ctrl + Shift + A**.
2. Edit Surgeon Profile, Services, Testimonials, Case Results, Articles, FAQs and Settings.
3. Changes show immediately.

**Important — how saving works (please read):**
The admin panel saves to the **browser's local storage**. That means edits are saved **only in the browser/device
where they were made** — they do **not** automatically reach other visitors. This is normal for a static site.

To **publish** changes for everyone, pick one:
- **Simple:** in Admin → Settings click **Export Data**, send me the file, and I'll bake it into `index.html`; **or**
- **Self-service (optional upgrade):** connect a free **Firebase** database so the doctor can edit the live site
  himself from anywhere. This needs a one-time ~5-minute setup (free) — tell me if you'd like this and I'll wire it in.

> Tip: the built-in defaults live in the `defaultData` object near the top of the `<script>` in `index.html`.
> Editing there changes what every fresh visitor sees. (There's a `dataVersion` flag — bumping it makes a new
> published version override any old cached edits.)

---

## 🎞 The hero scroll animation

`frames/frame-001.webp … frame-120.webp` — a muscle→bone reveal scrubbed as you scroll.
- Configured in `defaultData.settings` (`heroFrameFolder`, `heroFramePrefix`, `heroFrameCount`, `heroFrameExtension`).
- Loads the first few frames then reveals the page instantly and lazy-loads the rest (phones load every 2nd frame).
- To regenerate from a source sequence: convert your JPG/PNG frames to WebP into `frames/` named `frame-001.webp …`
  and update `heroFrameCount`.

---

## 🚀 Deploy

It's a static site — upload `index.html`, `images/`, and `frames/` to any host:
- **Netlify / Vercel / Cloudflare Pages:** drag-and-drop the folder.
- **GitHub Pages / Hugging Face Spaces (static):** push the files.
- **Shared hosting / cPanel:** upload to `public_html`.

No environment variables or build commands. Just make sure `images/` and `frames/` are uploaded alongside `index.html`.

---

## Browser support & accessibility
Works on current Chrome, Safari, Edge, Firefox (desktop + mobile). Animations respect
`prefers-reduced-motion`. Fonts and GSAP load from CDNs with graceful fallbacks.
