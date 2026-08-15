#!/usr/bin/env python3
"""Capture QueueLite frames to PNG for dropping into Figma."""
import os
import subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
FRAMES = os.path.join(ROOT, "frames", "capture.html")
OUT = os.path.join(ROOT, "previews")
os.makedirs(OUT, exist_ok=True)

SPECS = [
    ("cover", 1440, 900),
    ("login", 1440, 900),
    ("reception", 1440, 900),
    ("issue", 1440, 900),
    ("book", 1440, 900),
    ("doctor", 1440, 900),
    ("paused", 1440, 900),
    ("admin", 1440, 900),
    ("patient-waiting", 390, 844),
    ("patient-called", 390, 844),
    ("tv", 1920, 1080),
]


def capture(name, w, h, dest):
    url = "file://" + FRAMES + "?frame=" + name
    cmd = [
        "google-chrome",
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--no-first-run",
        "--no-default-browser-check",
        "--force-device-scale-factor=1",
        "--allow-file-access-from-files",
        "--remote-debugging-port=0",
        f"--user-data-dir=/tmp/ql-chrome-{name}",
        f"--window-size={w},{h}",
        f"--screenshot={dest}",
        url,
    ]
    print("capturing", name)
    proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        proc.wait(timeout=12)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait()
    if not os.path.isfile(dest) or os.path.getsize(dest) < 1000:
        raise SystemExit("failed " + name)
    print("wrote", dest, os.path.getsize(dest))


def main():
    for name, w, h in SPECS:
        capture(name, w, h, os.path.join(OUT, name + ".png"))


if __name__ == "__main__":
    main()
