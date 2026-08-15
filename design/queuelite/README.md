# QueueLite UI / UX (Figma)

Figma’s cloud API cannot create a `.fig` file from this environment. This folder is the UI kit for `prompts/clinic-queue-prompt.md`, in two forms:

1. **Figma plugin** — generates native Figma pages, frames, and components in *your* file.
2. **HTML prototype** — same screens in the browser, for review without Figma.

## Create the Figma file (about 1 minute)

1. Open [Figma](https://www.figma.com) → **New design file**.
2. Menu: **Plugins → Development → Import plugin from manifest…**
3. Select `design/queuelite/figma-plugin/manifest.json` from this repo.
4. Run **QueueLite UI Generator** → **Generate Figma screens**.

You should get pages:

| Page | Contents |
|------|----------|
| 00 Cover | Product cover |
| 01 Flows | Queue story |
| 02 Reception | Today, issue token, empty morning, book slot |
| 03 Doctor | Live queue, paused |
| 04 Admin | Doctors, hours & SMS, audit, tenant denied |
| 05 Patient mobile | Waiting, next, called, invalid signed link |
| 06 TV board | Live + paused (numbers only, no names) |
| 07 Login | Staff sign-in |
| 08 Components | Status rows + buttons |

Optional: Tokens Studio → import `design/queuelite/tokens/tokens.json`.

## Preview without Figma

Open `design/queuelite/prototype/index.html` in a browser.

Static captures: `design/queuelite/previews/cover.png`, `design/queuelite/previews/reception.png`.

## UX notes

See `design/queuelite/ux/flows.md` (appointment vs walk-in mix, privacy on TV, signed patient URLs).

Demo clinic in the mockups: **Greenfield Family Clinic** (fictional).
