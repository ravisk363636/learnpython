# QueueLite UI / UX (Figma)

There is no way to check a binary `.fig` into git from this environment. This kit **creates the Figma file in your Figma account** (native frames, auto layout, prototype clicks), and also ships HTML + PNG so you can import without the plugin.

Spec: `prompts/clinic-queue-prompt.md`. Demo clinic: **Greenfield Family Clinic** (fictional).

## Create the Figma file (about 1 minute)

1. Open [Figma](https://www.figma.com) → **New design file**. Name it `QueueLite — clinic queue UI`.
2. Menu: **Plugins → Development → Import plugin from manifest…**
3. Select `design/queuelite/figma-plugin/manifest.json`.
4. Run **QueueLite UI Generator** → **Generate Figma screens**.
5. Press **Present (▶)** to click Login → Reception → Issue token / Book, Doctor pause, Patient waiting → called.

Pages created:

| Page | Contents |
|------|----------|
| 00 Cover | Product cover |
| 01 Flows | Queue story |
| 02 Reception | Today, issue token, empty morning, book slot |
| 03 Doctor | Live queue, paused |
| 04 Admin | Doctors, hours & SMS, audit, tenant denied |
| 05 Patient mobile | Waiting, next, called, invalid signed link |
| 06 TV board | Live + paused (**numbers only**, no names) |
| 07 Login | Staff sign-in (patients never use this) |
| 08 Components | Status rows + buttons |

Optional: Tokens Studio → import `design/queuelite/tokens/tokens.json`.

### Import without the plugin

- **html.to.design**: paste `design/queuelite/frames/capture.html` (open `?frame=reception` etc.).
- **Drag PNGs** from `design/queuelite/previews/` onto the canvas (`reception.png`, `tv.png`, …).

## Preview in a browser (no Figma)

- Clickable screens: `design/queuelite/prototype/app.html`
- Full gallery: `design/queuelite/prototype/index.html`

Regenerate PNGs: `python3 design/queuelite/export_previews.py` (needs Chrome).

## UX notes

See `design/queuelite/ux/flows.md` (appointment vs walk-in mix, privacy on TV, signed patient URLs).
