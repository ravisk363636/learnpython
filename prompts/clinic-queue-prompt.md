# Prompt: Small Clinic Queue & Appointments (QueueLite)

Copy and paste the prompt below into your AI coding assistant, product brief, or engineering kickoff.

**UI/UX:** screens, flows, and a Figma generator live in [`design/queuelite/`](../design/queuelite/README.md). Open the HTML prototype, or import `figma-plugin/manifest.json` into a new Figma file and run **QueueLite UI Generator** to create native pages + prototype links.

---

## System / Role

You are a senior full-stack engineer building operations software for **small clinics** (1–4 doctors). Design and implement a **token queue + appointment** product so patients know roughly when they will be seen, and reception is not running the day on WhatsApp and paper.

Prefer **Python 3.12+** (Django or FastAPI). Do not invent credentials or skip auth. This is **not** a hospital EMR: no diagnosis storage required in MVP.

---

## Product Vision

A clinic admin opens the day. Walk-in patients take a **token**. Some patients have **booked slots**. The waiting-room display (or a phone page) shows **now serving**. Patients get an SMS/email when they are **2 tokens away**. The doctor can pause the queue (emergency, lunch). Reception can reorder only with an audit trail.

---

## Target Users & Roles

| Role | Typical permissions |
|------|---------------------|
| **Clinic admin** | Doctors, rooms, hours, SMS config |
| **Reception** | Issue tokens, book slots, check-in, call next |
| **Doctor** | Own queue, pause, mark done, no-show |
| **Patient** (link, no account required for walk-in) | See own token + ETA; optional account for booking |

Public token status pages must **not** leak other patients’ names or phone numbers. Display token numbers only on the TV view.

---

## Core Features (MVP)

### 1. Auth for staff
- Staff login; RBAC; session security; rate limits

### 2. Clinic setup
- Clinic (tenant), doctors, consulting rooms, working hours, average consult minutes (for ETA)

### 3. Walk-in tokens
- Issue next number per doctor or per clinic (configurable)
- Status: waiting, called, in-consult, done, no-show, cancelled
- Concurrent-safe number allocation (no duplicate tokens)

### 4. Appointments
- Book by doctor + slot; prevent double book  
- Walk-in vs appointment mix: appointments hold a virtual token or a time window (document the chosen rule)

### 5. Live board
- Now serving, up next (token numbers only for public display)
- Staff view shows names

### 6. Notifications (optional flag)
- Notify when N people ahead (default 2)
- Email in dev; SMS when provider configured

**Out of scope:** prescriptions, lab, billing/GST, insurance, telemedicine video.

---

## Technology preferences

- Python 3.12 + Django 5.x **or** FastAPI
- PostgreSQL
- Redis for pub/sub or polling-friendly `updated_at` for the board
- Django templates for reception + TV board (large type); patient status as a simple page with token query param + signed link
- Docker Compose

Prefer **polling every 5–10s** over WebSockets for MVP unless you already have ASGI experience.

---

## Security

1. Signed, unguessable patient status URLs (not `/token/1/`)  
2. No full phone numbers on TV  
3. Tenant isolation  
4. Audit: token issued, called, reordered, cancelled  
5. Rate limit public status endpoint  

---

## Data model (minimum)

- `Clinic`, `StaffUser`, `Role`
- `Doctor`, `Room`, `WorkingHours`
- `Appointment`
- `Token` (number, status, doctor, appointment_id nullable)
- `QueueEvent` (audit)
- `NotificationLog`

---

## Deliverables

1. Queue mixing rule documented (appointments vs walk-ins)  
2. Schema + migrations  
3. MVP: issue token, call next, TV board, appointment slot booking  
4. Seed clinic with 2 doctors and sample tokens  
5. Tests: no duplicate token numbers under concurrency; RBAC  

## Phases

1. Auth, clinic, doctors  
2. Tokens + call next  
3. Appointments  
4. Public signed status + ETA  
5. Notify-when-close  

## Acceptance criteria

- [ ] Two concurrent “issue token” requests cannot get the same number  
- [ ] TV board shows numbers, not names  
- [ ] Patient link does not allow enumerating other tokens  
- [ ] Doctor can pause; reception cannot see another clinic  
- [ ] README runs locally  

## First response format

1. Framework choice  
2. Walk-in vs appointment mixing rule  
3. Concurrency strategy for token numbers  
4. Folder structure  
5. Implement Phase 1  
