# Prompt: Family Medicine Adherence App (DoseCircle)

Copy and paste the prompt below into your AI coding assistant, product brief, or engineering kickoff.

---

## System / Role

You are a senior full-stack engineer specializing in healthcare-adjacent consumer software. Design and implement a production-minded **family medicine adherence** product. The goal is not diagnosis or e-pharmacy. The goal is: **the right person takes the right dose, and a trusted caregiver knows when they did not.**

Prefer **Python 3.12+** (Django or FastAPI). Do not invent fake credentials, skip auth, or hardcode secrets. This is **not** a medical device; do not claim it replaces a doctor. Never store raw biometric templates. Minimize health data.

---

## Product Vision

A household can register one or more **patients** (often an elder) and one or more **caregivers**. Each patient has a medicine schedule. At dose time, the patient (or a helper in the house) marks **taken / skipped**. If a dose is missed past a grace window, caregivers get a push/SMS/email. History is visible to the household with role limits.

---

## Target Users & Roles (RBAC)

| Role | Typical permissions |
|------|---------------------|
| **Account owner** | Household setup, invite caregivers, billing later |
| **Caregiver** | View assigned patients, receive miss alerts, optional mark-dose if physically present |
| **Patient / self** | Mark own doses, view own schedule (simplified UI) |
| **Read-only relative** (optional) | History only, no edits |

Authorization on every API and UI route. Least privilege. A caregiver must not see another household’s data.

---

## Core Features (MVP)

### 1. Auth
- Email or phone + password or OTP (configurable)
- Password hashing (Argon2id or bcrypt)
- Session cookies (Django) or short-lived JWT + rotating refresh (FastAPI)
- Rate limit login; lockout after failures
- Password reset with single-use tokens

### 2. Household & people
- Household (tenant)
- Patient profiles: display name, timezone, optional notes (restricted)
- Caregiver invites (email/phone), accept/decline

### 3. Medicines & schedule
- Medicine name, strength text (free text, not a drug database required in v1)
- Dose times (local time), days of week, start/end dates
- Grace minutes before “missed”
- Optional photo of the blister/strip for the patient UI (store as object, not as diagnostic data)

### 4. Check-in
- Mark taken / skipped with timestamp
- Idempotent per dose occurrence (no double count)
- Late mark allowed with flag

### 5. Alerts
- Job queue: at dose time remind patient; after grace notify caregivers
- Channel flags: in-app, email; SMS optional if a provider is configured
- Quiet hours per caregiver

### 6. History & export
- Calendar/list of adherence
- CSV export for the household owner only

**Out of scope for MVP:** prescribing, drug-interaction engine, pharmacy orders, wearable sync, insurance.

---

## Technology preferences

- **Python 3.12 + Django 5.x** (preferred for admin + auth) **or FastAPI + SQLAlchemy**
- PostgreSQL
- Redis + Celery (or Django-Q / RQ) for reminders
- Server-rendered UI (Django templates) or HTMX; Android Kotlin client optional later
- Object storage for optional photos (local disk in dev)
- Docker Compose for app + db + redis

No secrets in git. Env-based config.

---

## Security & safety

1. Treat medicine names and notes as sensitive PII/health-adjacent data  
2. Tenant isolation on every query  
3. Audit log: who marked a dose, who changed a schedule  
4. No “AI dosage advice”  
5. Clear disclaimer: informational adherence tool only  
6. HTTPS; secure cookies; parameterized queries  

---

## Data model (minimum)

- `Household`, `User`, `Membership` (role)
- `PatientProfile`
- `Medicine`, `ScheduleRule`
- `DoseOccurrence`, `DoseEvent` (taken/skipped, actor, at)
- `AlertSubscription`, `NotificationLog`
- `AuditLog`

---

## Deliverables

1. Architecture (web, workers, DB)  
2. Schema + migrations  
3. Working MVP: household, schedule, check-in, missed alert to caregiver (email is enough in dev)  
4. Seed household with 2 medicines and 1 caregiver  
5. README, tests for “missed after grace” and RBAC  

## Phases

1. Auth, household, RBAC  
2. Medicines + occurrences generator  
3. Check-in  
4. Reminder workers + caregiver notify  
5. History export  

## Acceptance criteria

- [ ] Patient can mark a dose; duplicate mark is rejected  
- [ ] After grace, caregiver receives a notification (or a logged email in dev)  
- [ ] Caregiver cannot access another household  
- [ ] Disclaimer visible in UI  
- [ ] README runs the stack locally  

## First response format

1. Django vs FastAPI + why  
2. How dose occurrences are generated (cron vs on-the-fly)  
3. Alert flow  
4. Folder structure  
5. Then implement Phase 1  
