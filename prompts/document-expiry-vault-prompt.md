# Prompt: Personal Document Expiry Vault (ExpiryVault)

Copy and paste the prompt below into your AI coding assistant, product brief, or engineering kickoff.

---

## System / Role

You are a senior full-stack engineer specializing in privacy-aware personal productivity software. Design and implement a **document expiry and renewal reminder** product for households and freelancers.

Prefer **Python 3.12+** (Django or FastAPI). Do not invent credentials. **Do not encourage uploading government ID numbers as a “backup of Aadhaar/SSN.”** Store the minimum metadata needed to remind. Encrypt files at rest if file upload is enabled.

---

## Product Vision

Users catalog items that **expire or must be renewed**: passport, visa, insurance, driving licence, PUC, rent agreement, domain names, SSL certs, professional licences. They set the expiry date and lead times (e.g. 90/30/7 days). The app nags them (and an optional partner) before it is too late. Optional encrypted file attachments.

---

## Target Users & Roles

| Role | Typical permissions |
|------|---------------------|
| **Owner** | Full vault |
| **Partner / shared member** | Items explicitly shared with them |
| **Guest** | None |

Item-level sharing, not “whole account dump” by default.

---

## Core Features (MVP)

### 1. Auth
- Email + password; hashing; sessions or JWT+refresh; reset tokens; rate limits; optional TOTP later

### 2. Items
- Title, category, expiry date, notes, reminder offsets (default 90/30/7)
- Optional file upload (size-capped); encryption at rest (dev: Fernet/age with key from env)
- Tags (e.g. `travel`, `vehicle`, `work`)

### 3. Reminders
- Daily job: due reminders → email (SMS optional)
- Mark “renewed” → new expiry; keep history of past expiries

### 4. Sharing
- Invite partner; share selected items read-only or edit

### 5. Dashboard
- Timeline of upcoming expiries; overdue highlight

**Out of scope:** OCR of IDs as a default; government integrations; password-manager replacement (no website login passwords in v1).

---

## Technology preferences

- Python 3.12 + Django 5.x or FastAPI
- PostgreSQL
- Redis + Celery/RQ for daily digest
- Local filesystem or S3-compatible for files
- Docker Compose
- Server-rendered UI

---

## Security

1. Encrypt file blobs; never log file contents  
2. Do not require national ID numbers as fields  
3. CSRF, secure cookies, parameterized queries  
4. Shared users only see shared rows  
5. Download authorization checked server-side  
6. Retention: user can delete item + blob  

---

## Data model (minimum)

- `User`, `Household` (optional)
- `VaultItem` (title, category, expires_on, reminder_offsets JSON)
- `VaultFile` (storage key, checksum, encrypted flag)
- `Share` (item, user, permission)
- `ReminderLog`
- `AuditLog`

---

## Deliverables

1. Threat notes (what you store vs what you refuse)  
2. Schema + migrations  
3. MVP: items, dashboard, email reminder job, optional upload  
4. Seed user with 5 sample expiries  
5. Tests: share isolation; reminder job selects the right items  

## Phases

1. Auth + items + dashboard  
2. Reminder worker  
3. Sharing  
4. Encrypted uploads  
5. Digest email polish  

## Acceptance criteria

- [ ] Upcoming and overdue items show correctly in the user’s timezone  
- [ ] Daily job sends (or logs) reminders only for due offsets not already sent  
- [ ] Partner cannot see unshared items  
- [ ] File download requires auth  
- [ ] README runs locally  

## First response format

1. Framework choice  
2. Encryption approach for files  
3. Reminder idempotency  
4. Folder structure  
5. Implement Phase 1  
