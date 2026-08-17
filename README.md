# QueueLite — small clinic queue & appointments

Operations software for clinics with 1–4 doctors: walk-in tokens, booked slots, a waiting-room board, and signed patient status links. This is not an EMR (no diagnoses).

## Framework choice

**Python 3.12 + Django 5.x**, PostgreSQL, Redis (cache / rate limits), Django templates, **polling every 8s** (TV + patient pages use meta-refresh). Auth is session-based with RBAC. No invented production credentials: set `DJANGO_SECRET_KEY` and `QUEUELITE_SEED_PASSWORD` yourself.

## Walk-in vs appointment mixing rule

Appointments **hold a time window** (`start_at` → `end_at`) on a doctor’s calendar. They do **not** take a walk-in number at booking time. Overlapping booked/checked-in windows are rejected.

At **check-in**, the patient is issued the next real token (same allocator as walk-ins) and the token is linked to the appointment.

**Call next** for a doctor:

1. Waiting tokens whose appointment is **due** (`now >= start_at − appointment_priority_grace_minutes`), by `sort_order` then `issued_at`.
2. Otherwise the oldest waiting token (walk-in or early check-in), same ordering.

Reception may change `sort_order`; every reorder is a `QueueEvent`. Doctors may pause their queue (lunch/emergency); call-next is blocked while paused.

## Concurrency strategy for token numbers

A `TokenSequence` row per clinic (or per doctor, depending on `Clinic.token_scope`) and service date is locked with `SELECT … FOR UPDATE` inside a transaction, then `next_number` is incremented. `Token` has a unique constraint on `(clinic, doctor, service_date, number)`. Integrity errors retry. Two concurrent “issue token” calls cannot keep the same number.

## Folder structure

```
apps/accounts          StaffUser, RBAC, login
apps/clinics           Clinic, Doctor, Room, WorkingHours, seed
apps/queues            Token, TokenSequence, QueueEvent, board, signed links
apps/appointments      Slot booking + check-in
apps/notifications     NotificationLog; email in DEBUG, SMS if configured
config/                Django settings
templates/ static/     Reception, doctor, TV, patient
design/queuelite/      HTML prototype + Figma generator plugin
```

## Run locally (SQLite, no Docker)

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export DJANGO_DEBUG=1
export DJANGO_SECRET_KEY=dev-only-not-for-production
export QUEUELITE_SEED_PASSWORD='choose-a-long-password'
python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```

Sign in at `/accounts/login/` with usernames `riverside_admin`, `riverside_desk`, `dr_mehta`, or `dr_rao` and the seed password you set.

- Reception today: `/`
- Issue token: `/queue/issue/`
- Appointments: `/appointments/`
- Clinic setup (admin): `/setup/`
- TV board (numbers only): `/board/riverside/`
- Patient link is printed after issue (signed path `/p/<payload>/`)

## Run with Docker Compose (PostgreSQL + Redis)

```bash
export QUEUELITE_SEED_PASSWORD='choose-a-long-password'
export DJANGO_SECRET_KEY='another-long-random-string'
docker compose up --build
```

If `QUEUELITE_SEED_PASSWORD` is empty, seed prints a generated password in the `web` logs (DEBUG only).

Compose database user/password `queuelite` is **local-only**; do not use it in production.

## Tests

```bash
export DJANGO_DEBUG=1 DJANGO_SECRET_KEY=test
python manage.py test
```

Includes concurrent issue-token uniqueness, RBAC / tenant isolation, TV (no names), and non-enumerable patient links.

## Notifications

`Clinic.notifications_enabled` plus `notify_when_ahead` (default 2). Email uses the console backend in DEBUG. SMS is attempted only when `SMS_PROVIDER=twilio` and Twilio env vars are set. Destinations in `NotificationLog` mask phone numbers.

## Security notes

- Staff passwords: Argon2, 12+ chars, session cookies HttpOnly
- Login POST rate-limited; public status GET rate-limited
- Patient URLs are signed + unguessable (`public_key`), not `/token/1/`
- TV board never renders patient names or phones
- Staff querysets are scoped to `request.user.clinic`
