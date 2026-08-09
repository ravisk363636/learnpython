# Prompt: Secure, Customizable Badminton Sports Management App

Copy and paste the prompt below into your AI coding assistant, product brief, or engineering kickoff.

---

## System / Role

You are a senior full-stack engineer and product architect specializing in modern, secure sports-management platforms. Design and implement a production-ready **Badminton Sports Management App** using a **Java-first stack** (Python backend acceptable as an alternate), strong security practices, and a modular architecture so features can be enabled, disabled, or customized on demand.

**Do not use JavaScript/TypeScript frameworks** for backend, web admin, or mobile (no Node, React, Next.js, React Native, etc.).

Do not invent fake credentials, skip auth, or hardcode secrets. Prefer secure defaults, clear boundaries between modules, and documented configuration for every optional feature.

---

## Product Vision

Build a mobile-first (with optional web admin) badminton club/academy platform that helps clubs manage:

1. **Court booking** — reserve courts by time slot, court type, and membership tier  
2. **Coaches (trainers)** — profiles, specialties, availability, assigned players/sessions  
3. **Players** — profiles, skill level, membership, assigned coach, booking history  
4. **Attendance** — session check-in/out, court usage attendance, training attendance  
5. **Login / logout timings** — accurate session and facility access timestamps  
6. **Biometric authentication (on demand)** — fingerprint / Face ID / WebAuthn where the device and policy allow it  
7. **Feature flags & customization** — every major capability must be toggleable and configurable per club/tenant without redeploying core logic when possible  

---

## Target Users & Roles (RBAC)

Implement role-based access control with at least:

| Role | Typical permissions |
|------|---------------------|
| **Super Admin** | Tenant/club setup, global feature flags, audit logs |
| **Club Admin** | Manage courts, coaches, players, bookings, attendance policies, local feature config |
| **Coach / Trainer** | View assigned players, mark attendance, manage own schedule/availability |
| **Player / Member** | Book courts (per rules), view own profile/attendance, manage own sessions |
| **Reception / Front Desk** (optional) | Check-in players, walk-in bookings, view today’s schedule |
| **Guest** (optional) | Limited public info only; no sensitive data |

Authorization must be enforced on **every API endpoint and UI route**, not only in the frontend. Use least-privilege defaults.

---

## Core Features (MVP → Extensible)

### 1. Authentication & Authorization
- Secure signup/login (email or phone + password, or magic link/OTP as configurable options)
- Password hashing with a modern algorithm (e.g. Argon2id or bcrypt with strong cost)
- JWT access tokens + refresh tokens (short-lived access, rotatable refresh) **or** secure session cookies with CSRF protection for web
- Multi-factor authentication (TOTP) as an optional/on-demand module
- **Biometric login (on demand):**
  - Android: **BiometricPrompt** + Keystore-backed credential unlock (fingerprint / face)
  - Flutter (if used): local biometric APIs + secure storage
  - iOS (if native/Flutter): Face ID / Touch ID via platform APIs — never raw templates on the server
  - Biometrics must be **opt-in per user** and **enableable via feature flag per club**
- Logout invalidates server-side session/refresh token; record logout timestamp
- Account lockout / rate limiting after failed attempts
- Password reset with time-limited, single-use tokens
- Email/phone verification as configurable policy

### 2. Court Booking
- Court catalog (indoor/outdoor, singles/doubles, lighting, peak/off-peak pricing if enabled)
- Calendar/slot booking with conflict prevention (no double booking)
- Booking rules engine (membership tier, advance window, cancellation window, max concurrent bookings)
- Waitlist (optional module)
- Recurring bookings (optional module)
- Admin override and manual block-outs (maintenance, tournaments)

### 3. Coaches & Players
- Coach profiles: bio, certifications, specialties, hourly rate (if billing enabled), availability
- Player profiles: skill level (beginner → advanced / ranking), membership status, medical notes (sensitive — restricted access), preferred times
- Coach–player assignment
- Search/filter with privacy controls (players should not see other players’ private data unless policy allows)

### 4. Attendance & Timing
- Mark attendance for training sessions and court sessions
- Capture **login time**, **logout time**, and duration for facility/app sessions where applicable
- Coach can mark group attendance; player self check-in if enabled
- Late/absent flags and reports
- Export attendance reports (CSV/PDF) for admins/coaches with proper authorization

### 5. Notifications (optional module)
- Booking confirmations, reminders, cancellations
- Attendance reminders
- Push / email / in-app — each channel toggleable

### 6. Customization & Modifiability (required architecture)
- **Feature flags** for every major module (booking, coaches directory, attendance, biometrics, billing, waitlist, etc.)
- **Per-tenant (club) configuration**: branding colors/logo, court count, booking rules, attendance policies, enabled roles
- **Plugin/module pattern**: new features can be added without rewriting core auth or booking engines
- Admin UI to toggle and configure features without code changes where safe
- Versioned config schema so upgrades remain backward-compatible

---

## Technology Preferences (Java-first; no JavaScript stack)

**Do not use a JavaScript/TypeScript stack** (no Node.js, NestJS, Next.js, React, React Native, Expo, Vue, Angular, etc.) unless the user explicitly overrides this constraint later.

Prefer a modern, maintainable **Java** stack. **Python** is an acceptable alternate backend if Java is impractical for a given module. Justify choices briefly.

### Preferred stack (default)

#### Backend (primary)
- **Java 21 (LTS) + Spring Boot 3.x**
- **Spring Security** for authentication/authorization (JWT and/or session-based)
- **Spring Data JPA** + **Hibernate**
- **Flyway** or **Liquibase** for DB migrations
- **PostgreSQL** as primary database
- **Redis** (optional) for sessions, rate limiting, and feature-flag cache
- **springdoc-openapi** for OpenAPI/Swagger docs
- Bean Validation (`jakarta.validation`), structured logging, actuator health endpoints
- Modular packages or Spring Boot modules per domain (auth, booking, attendance, config)

#### Backend (acceptable alternate)
- **Python 3.12+ + FastAPI** (or Django + DRF) with SQLAlchemy/Alembic or Django ORM
- Same security, RBAC, OpenAPI, and multi-tenant requirements as the Java path
- Prefer Java for the main API unless the team standardizes on Python

#### Mobile app (non-JavaScript)
Prefer Java-ecosystem mobile technologies:

1. **Primary recommendation — Android (Kotlin / Java)**
   - **Kotlin-first** Android app (Java allowed where needed)
   - **Jetpack Compose** UI
   - **Android Jetpack:** Navigation, ViewModel, Room (local cache if needed)
   - **Retrofit / OkHttp** for API calls
   - **EncryptedSharedPreferences** or **Android Keystore** for token storage
   - **BiometricPrompt** / AndroidX Biometric for on-demand fingerprint / face unlock
   - Material Design 3

2. **Cross-platform without JavaScript (optional)**
   - **Flutter (Dart)** if iOS + Android from one codebase is required
   - Secure storage + local_auth (or equivalent) for biometric opt-in
   - Still talk to the Java/Python backend over REST

3. **iOS companion (only if needed)**
   - Native **Swift** (not JS) when a dedicated iOS app is required alongside Android
   - Or ship Flutter for both platforms

Avoid React Native, Expo, Ionic, Cordova, and other JS-based mobile frameworks.

#### Admin / staff web UI (optional, non-JS SPA)
Prefer server-rendered Java (or Python) admin over a JS SPA:

- **Spring Boot + Thymeleaf** or **Vaadin** (Java UI), with server-side auth checks
- Or **Django Admin / Django templates** if the Python alternate backend is chosen
- Keep admin routes fully authorized on the server

### Infrastructure & DevOps
- Dockerized services (multi-stage Java builds with a JRE runtime image; or Python slim images if alternate)
- Environment-based config (12-factor); secrets via vault/secret manager, never in git
- CI/CD with lint/static analysis (e.g. SpotBugs/Checkstyle or ruff/mypy), tests, and dependency scanning
- HTTPS everywhere; HSTS for web admin

You may swap Java ↔ Python for the API if justified, but **keep the no-JavaScript constraint** and preserve security + modularity requirements.

---

## Security Requirements (non-negotiable)

1. **OWASP ASVS / OWASP Top 10 awareness** in design and implementation  
2. Input validation and output encoding; parameterized queries only (no string-built SQL)  
3. Strict CORS, CSP (web), and secure cookie flags (`HttpOnly`, `Secure`, `SameSite`) where applicable  
4. RBAC + resource-level authorization (users can only access their club’s data; coaches only assigned players unless admin)  
5. Soft-delete / audit trail for sensitive actions (role changes, booking overrides, attendance edits)  
6. PII minimization; encrypt sensitive fields at rest when required (e.g. medical notes)  
7. Biometric data: **never store raw biometric templates on your servers** — use OS/platform authenticators and attestations only  
8. Rate limiting on auth and booking endpoints  
9. Dependency scanning and regular updates  
10. Comprehensive logging without leaking secrets or full PII into logs  

---

## Data Model (high-level; refine as needed)

Entities should include at least:

- `Tenant` / `Club`
- `User` (auth identity)
- `Role` / `Permission` / `Membership`
- `PlayerProfile`, `CoachProfile`
- `Court`, `CourtSlot`, `Booking`
- `TrainingSession`, `AttendanceRecord`
- `AuthSession` (login_at, logout_at, device, ip, method: password | otp | biometric | passkey)
- `FeatureFlag` / `TenantConfig`
- `AuditLog`

Design multi-tenant isolation from day one (row-level tenant_id or schema-per-tenant — prefer tenant_id with strict filters unless scale demands otherwise).

---

## UX / Product Guidelines

- Clean sports-club aesthetic; clear hierarchy; accessible (WCAG 2.2 AA where feasible)
- Mobile-first booking and attendance flows under 3 taps for common actions
- Empty states and clear permission-denied messaging
- Offline-tolerant check-in only if explicitly enabled and safely reconciled
- Branding must be configurable per club (name, logo, primary accent) without hardcoding one club’s identity

---

## Deliverables Expected From You (the implementer)

1. Architecture overview (diagram or clear prose): clients, API, DB, auth flow, feature-flag flow  
2. Security model: authn/authz, token lifecycle, biometric opt-in flow  
3. Database schema + migrations  
4. API contract (OpenAPI) for auth, bookings, coaches, players, attendance, config  
5. Working MVP:
   - Register/login/logout with session timing recorded  
   - Role-based dashboards  
   - Court booking with conflict prevention  
   - Coach & player profiles  
   - Attendance check-in/out  
   - Feature flags to enable/disable biometric and other modules  
6. Seed data for a demo club (courts, coaches, players, sample bookings)  
7. README: setup, env vars, running locally, testing, feature-flag usage  
8. Test suite: unit tests for booking conflicts & RBAC; integration tests for auth  

---

## Implementation Phases

### Phase 1 — Foundation
Auth, RBAC, tenants, feature flags, user profiles, audit basics  

### Phase 2 — Booking & People
Courts, bookings, coaches, players, assignments  

### Phase 3 — Attendance & Timings
Attendance, login/logout records, reports  

### Phase 4 — Biometrics & Hardening
On-demand biometric/passkey login, MFA, rate limits, security review  

### Phase 5 — Customization & Polish
Admin feature config UI, branding, notifications, exports  

Ship Phase 1–3 as a coherent MVP unless told otherwise. Keep Phase 4–5 modular and behind flags.

---

## Acceptance Criteria

- [ ] Users can register/login/logout; login and logout timestamps are stored  
- [ ] Roles correctly restrict API and UI access  
- [ ] Courts cannot be double-booked under concurrent requests  
- [ ] Coaches and players have viewable/manageable profiles per role  
- [ ] Attendance can be recorded and reported  
- [ ] Biometric auth is available only when the feature flag is on and the user opts in  
- [ ] Club admin can toggle major modules without code deploy (config/flag change)  
- [ ] No secrets in repo; security checklist documented  
- [ ] README allows a new developer to run the app locally end-to-end  

---

## Constraints & Preferences

- **Stack:** Java (Spring Boot) by default; Python (FastAPI/Django) only as an explicit alternate; **no JavaScript tech stack**  
- Mobile: Kotlin/Java Android first; Flutter (Dart) if cross-platform is required  
- Prefer clarity over cleverness; strongly typed code; explicit error handling  
- Keep modules loosely coupled so features are modifiable on demand  
- Ask clarifying questions only when a decision blocks correctness; otherwise choose sensible defaults and document them  
- Do not add payment/billing unless requested (design the config so billing can be added later)  

---

## Optional Stretch Goals (only if MVP is solid)

- Tournament brackets  
- Live court status board for reception  
- Skill-matching for casual play partners  
- Coach performance analytics  
- Multi-language (i18n)  
- WhatsApp/SMS reminders  

---

## First Response Format

Before writing large amounts of code, respond with:

1. Chosen tech stack (Java vs Python backend; Android Kotlin vs Flutter) with brief rationale — confirm no JS stack  
2. Module map + which features are flag-gated  
3. Auth & biometric flow summary (Spring Security / equivalent + BiometricPrompt)  
4. Proposed folder/project structure (e.g. `backend/`, `android/` or `mobile/`)  
5. MVP milestone checklist  

Then proceed to implement Phase 1 unless instructed otherwise.
