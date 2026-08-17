figma.showUI(__html__, { width: 280, height: 160 });

const SCREENS = [
  "Login",
  "Reception today",
  "Issue token",
  "Appointments",
  "Doctor queue",
  "TV board",
  "Patient status",
  "Clinic setup",
];

figma.ui.onmessage = async (msg) => {
  if (msg.type !== "generate") {
    return;
  }
  await figma.loadFontAsync({ family: "Inter", style: "Regular" });
  let x = 0;
  const nodes = [];
  for (const name of SCREENS) {
    const frame = figma.createFrame();
    frame.name = name;
    frame.resize(390, 844);
    frame.x = x;
    frame.fills = [{ type: "SOLID", color: { r: 0.96, g: 0.97, b: 0.96 } }];
    const title = figma.createText();
    title.characters = "QueueLite · " + name;
    title.x = 24;
    title.y = 40;
    title.fontSize = 22;
    frame.appendChild(title);
    const body = figma.createText();
    body.characters =
      name === "TV board"
        ? "NOW SERVING\n012\nUp next 013 · 014\n(token numbers only)"
        : "Prototype screen. Wire flows: Login → Reception → Issue / Appointments → TV / Patient.";
    body.x = 24;
    body.y = 90;
    body.fontSize = 16;
    frame.appendChild(body);
    nodes.push(frame);
    x += 430;
  }
  for (let i = 0; i < nodes.length - 1; i++) {
    nodes[i].flowStartingPoints = [
      { nodeId: nodes[i + 1].id, name: "Next" },
    ];
  }
  figma.viewport.scrollAndZoomIntoView(nodes);
  figma.closePlugin("Created QueueLite screens");
};
