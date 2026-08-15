figma.showUI(__html__, { width: 380, height: 210 });

const C = {
  brand: hex("#0F766E"),
  brandDark: hex("#115E59"),
  brandSoft: hex("#F0FDFA"),
  ink: hex("#0F172A"),
  ink2: hex("#334155"),
  mute: hex("#64748B"),
  line: hex("#E2E8F0"),
  app: hex("#F4F7F6"),
  card: hex("#FFFFFF"),
  tv: hex("#0B1220"),
  tvCard: hex("#121A2B"),
  warn: hex("#D97706"),
  ok: hex("#059669"),
  danger: hex("#DC2626"),
  pause: hex("#7C3AED"),
  white: hex("#FFFFFF"),
  calledBg: hex("#FFFBEB"),
};

function hex(h) {
  const v = h.replace("#", "");
  return {
    r: parseInt(v.slice(0, 2), 16) / 255,
    g: parseInt(v.slice(2, 4), 16) / 255,
    b: parseInt(v.slice(4, 6), 16) / 255,
  };
}

function paint(color) {
  return [{ type: "SOLID", color }];
}

async function fonts() {
  const styles = ["Regular", "Medium", "Semi Bold", "Bold"];
  for (const style of styles) {
    await figma.loadFontAsync({ family: "Inter", style });
  }
}

function frame(name, w, h, fill, radius) {
  const f = figma.createFrame();
  f.name = name;
  f.resize(w, h);
  f.fills = paint(fill || C.white);
  if (radius) f.cornerRadius = radius;
  f.clipsContent = true;
  return f;
}

function auto(name, mode, opts) {
  const f = figma.createFrame();
  f.name = name;
  f.layoutMode = mode;
  f.fills = opts.fill ? paint(opts.fill) : [];
  if (opts.w && opts.h) f.resize(opts.w, opts.h);
  else if (opts.w) f.resize(opts.w, 40);
  f.primaryAxisSizingMode = opts.hugMain ? "AUTO" : "FIXED";
  f.counterAxisSizingMode = opts.hugCross ? "AUTO" : "FIXED";
  if (opts.pad) {
    const p = Array.isArray(opts.pad) ? opts.pad : [opts.pad, opts.pad, opts.pad, opts.pad];
    f.paddingTop = p[0];
    f.paddingRight = p[1];
    f.paddingBottom = p[2];
    f.paddingLeft = p[3];
  }
  f.itemSpacing = opts.gap || 0;
  f.primaryAxisAlignItems = opts.main || "MIN";
  f.counterAxisAlignItems = opts.cross || "MIN";
  if (opts.radius) f.cornerRadius = opts.radius;
  if (opts.stroke) {
    f.strokes = paint(opts.stroke);
    f.strokeWeight = opts.strokeW || 1;
  }
  f.clipsContent = !!opts.clip;
  return f;
}

function fillChild(n) {
  n.layoutSizingHorizontal = "FILL";
}

function text(chars, size, style, color, opts) {
  const t = figma.createText();
  t.fontName = { family: "Inter", style: style || "Regular" };
  t.characters = chars;
  t.fontSize = size;
  t.fills = paint(color || C.ink);
  if (opts && opts.center) t.textAlignHorizontal = "CENTER";
  if (opts && opts.width) {
    t.resize(opts.width, t.height);
    t.textAutoResize = "HEIGHT";
  }
  return t;
}

function pill(label, bg, fg) {
  const f = auto("Pill/" + label, "HORIZONTAL", {
    hugMain: true,
    hugCross: true,
    pad: [4, 10, 4, 10],
    gap: 0,
    fill: bg,
    radius: 999,
    main: "CENTER",
    cross: "CENTER",
  });
  f.appendChild(text(label, 11, "Semi Bold", fg));
  return f;
}

function btn(label, variant) {
  const fill = variant === "ghost" ? C.white : variant === "danger" ? C.danger : C.brand;
  const fg = variant === "ghost" ? C.ink : C.white;
  const stroke = variant === "ghost" ? C.line : fill;
  const f = auto("Button/" + label, "HORIZONTAL", {
    hugMain: true,
    hugCross: true,
    pad: [10, 16, 10, 16],
    fill,
    radius: 10,
    stroke,
    main: "CENTER",
    cross: "CENTER",
  });
  f.appendChild(text(label, 13, "Semi Bold", fg));
  return f;
}

function sidebar(active) {
  const s = auto("Sidebar", "VERTICAL", {
    w: 240,
    h: 900,
    fill: C.ink,
    pad: 20,
    gap: 8,
  });
  s.appendChild(text("QueueLite", 18, "Bold", C.white));
  s.appendChild(text("Greenfield Family Clinic", 11, "Regular", C.mute));
  const nav = ["Today", "Appointments", "Doctors", "Hours & SMS", "Audit"];
  for (const item of nav) {
    const row = auto("Nav/" + item, "HORIZONTAL", {
      w: 200,
      hugMain: false,
      hugCross: true,
      pad: [10, 12, 10, 12],
      fill: item === active ? C.brand : undefined,
      radius: 8,
    });
    row.resize(200, 40);
    row.primaryAxisSizingMode = "FIXED";
    row.counterAxisSizingMode = "FIXED";
    row.counterAxisAlignItems = "CENTER";
    row.appendChild(text(item, 13, item === active ? "Semi Bold" : "Regular", C.white));
    s.appendChild(row);
  }
  const spacer = frame("spacer", 200, 1, C.ink);
  spacer.layoutGrow = 1;
  s.appendChild(spacer);
  s.appendChild(text("Priya  ·  Reception", 12, "Medium", C.white));
  s.appendChild(text("Sign out", 12, "Regular", C.mute));
  return s;
}

function topbar(title, right) {
  const bar = auto("Topbar", "HORIZONTAL", {
    w: 1200,
    hugCross: true,
    pad: [16, 24, 16, 24],
    fill: C.white,
    main: "SPACE_BETWEEN",
    cross: "CENTER",
    stroke: C.line,
  });
  bar.resize(1200, 64);
  bar.primaryAxisSizingMode = "FIXED";
  bar.counterAxisSizingMode = "FIXED";
  bar.appendChild(text(title, 20, "Bold", C.ink));
  if (right) bar.appendChild(right);
  return bar;
}

function staffShell(pageTitle, activeNav, bodyBuilder) {
  const art = frame("Desktop / " + pageTitle, 1440, 900, C.app);
  const row = auto("Shell", "HORIZONTAL", { w: 1440, h: 900, fill: C.app, gap: 0 });
  row.resize(1440, 900);
  const side = sidebar(activeNav);
  const main = auto("Main", "VERTICAL", { w: 1200, h: 900, fill: C.app, gap: 0 });
  main.resize(1200, 900);
  main.appendChild(topbar(pageTitle));
  const body = auto("Body", "VERTICAL", {
    w: 1200,
    h: 836,
    pad: 24,
    gap: 16,
    fill: C.app,
  });
  body.resize(1200, 836);
  bodyBuilder(body);
  main.appendChild(body);
  row.appendChild(side);
  row.appendChild(main);
  art.appendChild(row);
  row.x = 0;
  row.y = 0;
  return art;
}

function queueRow(num, name, kind, status, eta) {
  const row = auto("QueueRow/" + num, "HORIZONTAL", {
    w: 1152,
    hugCross: true,
    pad: [12, 16, 12, 16],
    fill: C.white,
    radius: 12,
    stroke: C.line,
    main: "SPACE_BETWEEN",
    cross: "CENTER",
  });
  row.resize(1152, 64);
  row.primaryAxisSizingMode = "FIXED";
  row.counterAxisSizingMode = "FIXED";
  const left = auto("L", "HORIZONTAL", { hugMain: true, hugCross: true, gap: 12, cross: "CENTER" });
  const token = auto("T", "HORIZONTAL", {
    hugMain: true,
    hugCross: true,
    pad: [6, 10, 6, 10],
    fill: C.brandSoft,
    radius: 8,
  });
  token.appendChild(text(num, 16, "Bold", C.brandDark));
  left.appendChild(token);
  const meta = auto("M", "VERTICAL", { hugMain: true, hugCross: true, gap: 2 });
  meta.appendChild(text(name, 14, "Semi Bold", C.ink));
  meta.appendChild(text(kind, 11, "Regular", C.mute));
  left.appendChild(meta);
  row.appendChild(left);
  const right = auto("R", "HORIZONTAL", { hugMain: true, hugCross: true, gap: 8, cross: "CENTER" });
  right.appendChild(text(eta, 12, "Regular", C.mute));
  const colors = {
    Waiting: [hex("#F1F5F9"), C.ink2],
    Called: [C.calledBg, C.warn],
    "In consult": [C.brandSoft, C.brandDark],
    Done: [hex("#ECFDF5"), C.ok],
    "No-show": [hex("#FEF2F2"), C.danger],
  };
  const c = colors[status] || colors.Waiting;
  right.appendChild(pill(status, c[0], c[1]));
  row.appendChild(right);
  return row;
}

async function generate() {
  await fonts();

  const coverPage = figma.currentPage;
  coverPage.name = "00 Cover";
  for (const n of [...coverPage.children]) n.remove();

  const cover = frame("Cover", 1440, 900, C.ink);
  const coverCol = auto("CoverCol", "VERTICAL", {
    w: 1440,
    h: 900,
    pad: 80,
    gap: 16,
    fill: C.ink,
    main: "CENTER",
  });
  coverCol.resize(1440, 900);
  coverCol.appendChild(pill("MVP UI / UX", C.brand, C.white));
  coverCol.appendChild(text("QueueLite", 64, "Bold", C.white));
  coverCol.appendChild(
    text("Token queue + appointments for a 1–4 doctor clinic", 22, "Regular", hex("#94A3B8"), {
      width: 720,
    })
  );
  coverCol.appendChild(text("Greenfield Family Clinic  ·  Staff · Doctor · Patient · TV", 14, "Medium", C.mute));
  cover.appendChild(coverCol);
  coverCol.x = 0;
  coverCol.y = 0;

  const flowsPage = figma.createPage();
  flowsPage.name = "01 Flows";
  const flowArt = frame("Flows", 1440, 900, C.app);
  const flowCol = auto("FlowCol", "VERTICAL", { w: 1440, h: 900, pad: 48, gap: 24, fill: C.app });
  flowCol.resize(1440, 900);
  flowCol.appendChild(text("User flows", 28, "Bold", C.ink));
  flowCol.appendChild(
    text(
      "Walk-in → token → wait → notify at 2 ahead → call next → consult → done. Appointments check in, then take the next token and join the live queue. TV and patient links never show names or phones.",
      14,
      "Regular",
      C.ink2,
      { width: 1100 }
    )
  );
  const steps = [
    ["1. Issue", "Reception assigns next number to a doctor"],
    ["2. Wait", "ETA from avg consult minutes"],
    ["3. Notify", "When N=2 people ahead"],
    ["4. Call", "Now serving on TV as a number only"],
    ["5. Pause", "Doctor lunch / emergency"],
  ];
  const stepRow = auto("Steps", "HORIZONTAL", { w: 1344, hugCross: true, gap: 12 });
  stepRow.resize(1344, 140);
  for (const [t, d] of steps) {
    const card = auto(t, "VERTICAL", {
      w: 250,
      hugCross: true,
      pad: 16,
      gap: 8,
      fill: C.white,
      radius: 12,
      stroke: C.line,
    });
    card.resize(250, 120);
    card.appendChild(text(t, 16, "Bold", C.brand));
    card.appendChild(text(d, 12, "Regular", C.ink2, { width: 210 }));
    stepRow.appendChild(card);
  }
  flowCol.appendChild(stepRow);
  flowArt.appendChild(flowCol);
  flowCol.x = 0;
  flowCol.y = 0;
  flowsPage.appendChild(flowArt);

  const recPage = figma.createPage();
  recPage.name = "02 Reception";

  const today = staffShell("Today’s queue", "Today", (body) => {
    const kpi = auto("KPIs", "HORIZONTAL", { w: 1152, hugCross: true, gap: 12 });
    kpi.resize(1152, 88);
    const kpis = [
      ["Waiting", "11"],
      ["Now serving", "A-14"],
      ["Appointments left", "7"],
      ["Avg wait", "18 min"],
    ];
    for (const [l, v] of kpis) {
      const c = auto(l, "VERTICAL", {
        w: 279,
        hugCross: true,
        pad: 16,
        gap: 4,
        fill: C.white,
        radius: 12,
        stroke: C.line,
      });
      c.resize(279, 88);
      c.appendChild(text(l, 12, "Medium", C.mute));
      c.appendChild(text(v, 24, "Bold", C.ink));
      kpi.appendChild(c);
    }
    body.appendChild(kpi);
    const actions = auto("Actions", "HORIZONTAL", { hugMain: true, hugCross: true, gap: 8 });
    actions.appendChild(btn("Issue token"));
    actions.appendChild(btn("Book appointment", "ghost"));
    actions.appendChild(btn("Call next"));
    body.appendChild(actions);
    body.appendChild(text("Dr. Meera Shah  ·  Room 1", 14, "Semi Bold", C.ink));
    body.appendChild(queueRow("A-14", "Ananya K.", "Walk-in", "Called", "Now"));
    body.appendChild(queueRow("A-15", "Rahul M.", "Appointment 10:30", "Waiting", "~12 min"));
    body.appendChild(queueRow("A-16", "Fatima S.", "Walk-in", "Waiting", "~24 min"));
    body.appendChild(queueRow("A-17", "Walk-in hold", "Walk-in", "Waiting", "~36 min"));
  });
  recPage.appendChild(today);
  today.x = 0;
  today.y = 0;

  const issue = staffShell("Issue token", "Today", (body) => {
    const card = auto("Form", "VERTICAL", {
      w: 560,
      hugCross: true,
      pad: 24,
      gap: 12,
      fill: C.white,
      radius: 16,
      stroke: C.line,
    });
    card.resize(560, 420);
    card.appendChild(text("New walk-in", 18, "Bold", C.ink));
    card.appendChild(text("Doctor", 12, "Medium", C.mute));
    card.appendChild(text("Dr. Meera Shah  ·  GP  ·  Room 1", 14, "Regular", C.ink));
    card.appendChild(text("Patient name (staff only — never on TV)", 12, "Medium", C.mute));
    card.appendChild(text("Sanjay Rao", 14, "Regular", C.ink));
    card.appendChild(text("Phone (for notify-when-2-ahead)", 12, "Medium", C.mute));
    card.appendChild(text("+91 98•••• 214", 14, "Regular", C.ink));
    const row = auto("btns", "HORIZONTAL", { hugMain: true, hugCross: true, gap: 8 });
    row.appendChild(btn("Issue next number"));
    row.appendChild(btn("Cancel", "ghost"));
    card.appendChild(row);
    body.appendChild(card);
  });
  recPage.appendChild(issue);
  issue.x = 1520;
  issue.y = 0;

  const empty = staffShell("Today’s queue", "Today", (body) => {
    const card = auto("Empty", "VERTICAL", {
      w: 1152,
      hugCross: true,
      pad: 48,
      gap: 12,
      fill: C.white,
      radius: 16,
      stroke: C.line,
      main: "CENTER",
      cross: "CENTER",
    });
    card.resize(1152, 280);
    card.appendChild(text("No tokens yet this morning", 20, "Bold", C.ink));
    card.appendChild(text("Issue the first walk-in token or check in an appointment.", 14, "Regular", C.ink2));
    card.appendChild(btn("Issue token"));
    body.appendChild(card);
  });
  recPage.appendChild(empty);
  empty.x = 0;
  empty.y = 980;

  const book = staffShell("Book appointment", "Appointments", (body) => {
    body.appendChild(text("Wednesday 15 Aug  ·  Dr. Arun Patel", 14, "Semi Bold", C.ink));
    const grid = auto("Slots", "HORIZONTAL", { w: 1152, hugCross: true, gap: 8 });
    const slots = ["09:00", "09:20", "09:40", "10:00 taken", "10:20", "10:40", "11:00", "11:20"];
    for (const s of slots) {
      const taken = s.includes("taken");
      const cell = auto(s, "HORIZONTAL", {
        w: 130,
        hugCross: true,
        pad: [12, 8, 12, 8],
        fill: taken ? hex("#F1F5F9") : C.brandSoft,
        radius: 10,
        main: "CENTER",
        cross: "CENTER",
        stroke: taken ? C.line : C.brand,
      });
      cell.resize(130, 44);
      cell.appendChild(text(taken ? "10:00" : s, 13, "Semi Bold", taken ? C.mute : C.brandDark));
      grid.appendChild(cell);
    }
    body.appendChild(grid);
    body.appendChild(text("Taken slots cannot be double-booked. Walk-ins do not occupy calendar slots.", 12, "Regular", C.mute));
    body.appendChild(btn("Confirm 10:20 with Dr. Patel"));
  });
  recPage.appendChild(book);
  book.x = 1520;
  book.y = 980;

  const docPage = figma.createPage();
  docPage.name = "03 Doctor";
  const doctor = staffShell("My queue", "Today", (body) => {
    const banner = auto("PauseBar", "HORIZONTAL", {
      w: 1152,
      hugCross: true,
      pad: 12,
      gap: 12,
      fill: hex("#F5F3FF"),
      radius: 12,
      cross: "CENTER",
      main: "SPACE_BETWEEN",
    });
    banner.resize(1152, 56);
    banner.primaryAxisSizingMode = "FIXED";
    banner.appendChild(text("Queue is live  ·  Room 1", 13, "Semi Bold", C.pause));
    banner.appendChild(btn("Pause queue"));
    body.appendChild(banner);
    body.appendChild(queueRow("A-14", "Ananya K.", "In your room", "In consult", "Started 09:41"));
    body.appendChild(queueRow("A-15", "Rahul M.", "Next", "Waiting", "~8 min"));
    body.appendChild(queueRow("A-16", "Fatima S.", "Waiting", "Waiting", "~20 min"));
    const acts = auto("DocActs", "HORIZONTAL", { hugMain: true, hugCross: true, gap: 8 });
    acts.appendChild(btn("Mark done"));
    acts.appendChild(btn("No-show", "danger"));
    acts.appendChild(btn("Call next"));
    body.appendChild(acts);
  });
  docPage.appendChild(doctor);
  doctor.x = 0;
  doctor.y = 0;

  const paused = staffShell("My queue", "Today", (body) => {
    const banner = auto("Paused", "VERTICAL", {
      w: 1152,
      hugCross: true,
      pad: 16,
      gap: 6,
      fill: hex("#F5F3FF"),
      radius: 12,
    });
    banner.resize(1152, 88);
    banner.appendChild(text("Paused — lunch / emergency", 16, "Bold", C.pause));
    banner.appendChild(text("TV shows PAUSED. New tokens still issue; call next is disabled until you resume.", 12, "Regular", C.ink2));
    body.appendChild(banner);
    body.appendChild(btn("Resume queue"));
    body.appendChild(queueRow("A-14", "Ananya K.", "Waiting after pause", "Waiting", "Held"));
  });
  docPage.appendChild(paused);
  paused.x = 1520;
  paused.y = 0;

  const admPage = figma.createPage();
  admPage.name = "04 Admin";
  const doctors = staffShell("Doctors & rooms", "Doctors", (body) => {
    const cards = auto("Docs", "HORIZONTAL", { w: 1152, hugCross: true, gap: 16 });
    for (const d of [
      ["Dr. Meera Shah", "GP  ·  Room 1  ·  12 min avg"],
      ["Dr. Arun Patel", "Dental  ·  Room 2  ·  20 min avg"],
    ]) {
      const c = auto(d[0], "VERTICAL", {
        w: 360,
        hugCross: true,
        pad: 20,
        gap: 8,
        fill: C.white,
        radius: 16,
        stroke: C.line,
      });
      c.resize(360, 140);
      c.appendChild(text(d[0], 18, "Bold", C.ink));
      c.appendChild(text(d[1], 13, "Regular", C.ink2));
      c.appendChild(pill("Token prefix A / B", C.brandSoft, C.brandDark));
      cards.appendChild(c);
    }
    body.appendChild(cards);
    body.appendChild(btn("Add doctor"));
  });
  admPage.appendChild(doctors);
  doctors.x = 0;
  doctors.y = 0;

  const hours = staffShell("Hours & SMS", "Hours & SMS", (body) => {
    const card = auto("Cfg", "VERTICAL", {
      w: 640,
      hugCross: true,
      pad: 24,
      gap: 12,
      fill: C.white,
      radius: 16,
      stroke: C.line,
    });
    card.resize(640, 320);
    card.appendChild(text("Working hours", 16, "Bold", C.ink));
    card.appendChild(text("Mon–Sat  09:00–13:00  and  16:00–20:00", 14, "Regular", C.ink2));
    card.appendChild(text("Notify when N people ahead", 16, "Bold", C.ink));
    card.appendChild(text("N = 2   ·   SMS flag ON   ·   Email fallback in dev", 14, "Regular", C.ink2));
    card.appendChild(text("TV board never shows names or phone numbers.", 12, "Medium", C.warn));
    body.appendChild(card);
  });
  admPage.appendChild(hours);
  hours.x = 1520;
  hours.y = 0;

  const audit = staffShell("Audit log", "Audit", (body) => {
    const rows = [
      ["09:41", "Called A-14", "Priya · Reception"],
      ["09:38", "Issued A-17 walk-in", "Priya · Reception"],
      ["09:12", "Appointment 10:20 booked", "Priya · Reception"],
      ["09:02", "Queue opened", "Dr. Shah"],
    ];
    for (const r of rows) {
      const row = auto(r[1], "HORIZONTAL", {
        w: 1152,
        hugCross: true,
        pad: [12, 16, 12, 16],
        fill: C.white,
        radius: 10,
        stroke: C.line,
        main: "SPACE_BETWEEN",
      });
      row.resize(1152, 48);
      row.primaryAxisSizingMode = "FIXED";
      row.appendChild(text(r[0] + "   " + r[1], 13, "Regular", C.ink));
      row.appendChild(text(r[2], 12, "Regular", C.mute));
      body.appendChild(row);
    }
  });
  admPage.appendChild(audit);
  audit.x = 0;
  audit.y = 980;

  const denied = staffShell("Today’s queue", "Today", (body) => {
    const card = auto("Denied", "VERTICAL", {
      w: 640,
      hugCross: true,
      pad: 32,
      gap: 10,
      fill: C.white,
      radius: 16,
      stroke: C.danger,
    });
    card.resize(640, 180);
    card.appendChild(text("You cannot open another clinic", 18, "Bold", C.danger));
    card.appendChild(text("Reception is limited to Greenfield Family Clinic. This is tenant isolation, not a missing button.", 13, "Regular", C.ink2, { width: 560 }));
    body.appendChild(card);
  });
  admPage.appendChild(denied);
  denied.x = 1520;
  denied.y = 980;

  const patPage = figma.createPage();
  patPage.name = "05 Patient mobile";

  function phone(name, builder) {
    const device = frame("Mobile / " + name, 390, 844, C.app, 32);
    const col = auto("PhoneCol", "VERTICAL", { w: 390, h: 844, pad: [48, 20, 24, 20], gap: 16, fill: C.app });
    col.resize(390, 844);
    builder(col);
    device.appendChild(col);
    col.x = 0;
    col.y = 0;
    return device;
  }

  const pWait = phone("Waiting", (col) => {
    col.appendChild(text("Greenfield Family Clinic", 12, "Medium", C.mute));
    col.appendChild(text("Your token", 14, "Regular", C.ink2));
    col.appendChild(text("A-16", 56, "Bold", C.brandDark));
    col.appendChild(pill("2 people ahead", C.calledBg, C.warn));
    const card = auto("eta", "VERTICAL", {
      w: 350,
      hugCross: true,
      pad: 16,
      gap: 6,
      fill: C.white,
      radius: 16,
      stroke: C.line,
    });
    card.resize(350, 110);
    card.appendChild(text("About 24 min", 22, "Bold", C.ink));
    card.appendChild(text("We’ll text you when you are 2 ahead. Keep this link — it cannot be guessed.", 12, "Regular", C.ink2, { width: 310 }));
    col.appendChild(card);
    col.appendChild(text("Now serving A-14  ·  Dr. Shah", 13, "Medium", C.mute));
  });
  patPage.appendChild(pWait);

  const pNext = phone("You are next", (col) => {
    col.appendChild(text("You’re next", 28, "Bold", C.ink));
    col.appendChild(text("A-16", 56, "Bold", C.warn));
    col.appendChild(text("Please wait near Room 1. Your name is not shown on the TV.", 14, "Regular", C.ink2, { width: 340 }));
  });
  patPage.appendChild(pNext);
  pNext.x = 430;

  const pCalled = phone("Called", (col) => {
    col.appendChild(text("Please come in", 28, "Bold", C.brandDark));
    col.appendChild(text("A-16", 56, "Bold", C.brand));
    col.appendChild(text("Room 1  ·  Dr. Meera Shah", 16, "Medium", C.ink));
  });
  patPage.appendChild(pCalled);
  pCalled.x = 860;

  const pBad = phone("Invalid link", (col) => {
    col.appendChild(text("This status link is invalid", 22, "Bold", C.danger));
    col.appendChild(text("It may have expired, or the address was typed by hand. Ask reception for a new SMS link. Token numbers are not public URLs.", 14, "Regular", C.ink2, { width: 340 }));
  });
  patPage.appendChild(pBad);
  pBad.x = 1290;

  const tvPage = figma.createPage();
  tvPage.name = "06 TV board";

  function tvBoard(title, paused) {
    const art = frame("TV / " + title, 1920, 1080, C.tv);
    const col = auto("TVCol", "VERTICAL", { w: 1920, h: 1080, pad: 48, gap: 24, fill: C.tv });
    col.resize(1920, 1080);
    const head = auto("H", "HORIZONTAL", { w: 1824, hugCross: true, main: "SPACE_BETWEEN", cross: "CENTER" });
    head.resize(1824, 48);
    head.primaryAxisSizingMode = "FIXED";
    head.appendChild(text("Greenfield Family Clinic", 28, "Bold", C.white));
    head.appendChild(text(paused ? "PAUSED" : "Wed 15 Aug  ·  09:42", 20, "Medium", paused ? hex("#C4B5FD") : C.mute));
    col.appendChild(head);
    const now = auto("Now", "VERTICAL", {
      w: 1824,
      hugCross: true,
      pad: 32,
      gap: 8,
      fill: C.tvCard,
      radius: 24,
      cross: "CENTER",
    });
    now.resize(1824, 420);
    now.appendChild(text(paused ? "Paused" : "Now serving", 22, "Medium", C.mute));
    now.appendChild(text(paused ? "—" : "A-14", 160, "Bold", paused ? hex("#C4B5FD") : C.white));
    now.appendChild(text(paused ? "Doctor will resume shortly" : "Room 1", 24, "Regular", C.mute));
    col.appendChild(now);
    const up = auto("Up", "HORIZONTAL", { w: 1824, hugCross: true, gap: 16 });
    for (const n of paused ? ["A-15", "A-16", "A-17"] : ["A-15", "A-16", "A-17"]) {
      const c = auto(n, "VERTICAL", {
        w: 597,
        hugCross: true,
        pad: 24,
        gap: 8,
        fill: C.tvCard,
        radius: 20,
        cross: "CENTER",
      });
      c.resize(597, 200);
      c.appendChild(text("Up next", 16, "Medium", C.mute));
      c.appendChild(text(n, 56, "Bold", C.white));
      up.appendChild(c);
    }
    col.appendChild(up);
    col.appendChild(text("Token numbers only. Names are never displayed.", 16, "Regular", C.mute));
    art.appendChild(col);
    col.x = 0;
    col.y = 0;
    return art;
  }
  const tv1 = tvBoard("Live", false);
  const tv2 = tvBoard("Paused", true);
  tvPage.appendChild(tv1);
  tvPage.appendChild(tv2);
  tv2.x = 2000;

  const loginPage = figma.createPage();
  loginPage.name = "07 Login";
  const login = frame("Desktop / Login", 1440, 900, C.app);
  const loginCol = auto("LoginCol", "VERTICAL", {
    w: 1440,
    h: 900,
    pad: 0,
    gap: 16,
    fill: C.app,
    main: "CENTER",
    cross: "CENTER",
  });
  loginCol.resize(1440, 900);
  const box = auto("Card", "VERTICAL", {
    w: 420,
    hugCross: true,
    pad: 32,
    gap: 12,
    fill: C.white,
    radius: 16,
    stroke: C.line,
  });
  box.resize(420, 360);
  box.appendChild(text("QueueLite", 22, "Bold", C.brandDark));
  box.appendChild(text("Staff sign in", 16, "Semi Bold", C.ink));
  box.appendChild(text("Work email", 12, "Medium", C.mute));
  box.appendChild(text("priya@greenfield.clinic", 14, "Regular", C.ink));
  box.appendChild(text("Password", 12, "Medium", C.mute));
  box.appendChild(text("••••••••••••", 14, "Regular", C.ink));
  box.appendChild(btn("Sign in"));
  box.appendChild(text("Locked after repeated failures. No patient login here.", 11, "Regular", C.mute));
  loginCol.appendChild(box);
  login.appendChild(loginCol);
  loginCol.x = 0;
  loginCol.y = 0;
  loginPage.appendChild(login);

  const compPage = figma.createPage();
  compPage.name = "08 Components";
  let cx = 0;
  const variants = ["Waiting", "Called", "In consult", "Done", "No-show"];
  for (const v of variants) {
    const p = queueRow("A-00", "Example patient", "Walk-in", v, "—");
    p.x = 0;
    p.y = cx;
    compPage.appendChild(p);
    cx += 80;
  }
  const b1 = btn("Primary");
  const b2 = btn("Secondary", "ghost");
  const b3 = btn("Danger", "danger");
  b1.x = 0;
  b1.y = cx + 20;
  b2.x = 140;
  b2.y = cx + 20;
  b3.x = 280;
  b3.y = cx + 20;
  compPage.appendChild(b1);
  compPage.appendChild(b2);
  compPage.appendChild(b3);

  figma.currentPage = coverPage;
}

figma.ui.onmessage = async (msg) => {
  if (msg.type === "generate") {
    try {
      await generate();
      figma.notify("QueueLite UI created. Check pages 00–08.");
      figma.closePlugin();
    } catch (e) {
      figma.notify(String(e), { error: true });
    }
  }
};
