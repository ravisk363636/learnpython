# Real-life problems you can turn into software

This catalog is for building **new products** that fix everyday friction—not toy tutorials. Each idea has a real user, a painful gap, an MVP you can ship, and why it is still worth building even though similar apps exist.

Pick **one** idea. Build a narrow MVP. Talk to 5–10 people who have the problem before adding features.

---

## How to choose

| If you care about… | Start with |
|--------------------|------------|
| Helping family / elderly | [1. DoseCircle](#1-dosecircle--family-medicine-adherence) |
| Local clinics & waiting rooms | [2. QueueLite](#2-queuelite--small-clinic-queue--appointments) |
| Documents, renewals, fines | [3. ExpiryVault](#3-expiryvault--document-and-renewal-reminders) |
| Apartment / housing societies | [4. SocietyDesk](#4-societydesk--apartment-ops-without-whatsapp-chaos) |
| Small shops & GST-lite billing | [5. CounterBook](#5-counterbook--kirana--workshop-billing) |
| Tuition / coaching classes | [6. ClassKeep](#6-classkeep--tuition-fees-attendance-parent-updates) |
| Daily-wage / site labour | [7. MusterPay](#7-musterpay--attendance--wage-for-small-contractors) |
| Surplus food → people who need it | [8. SurplusBridge](#8-surplusbridge--food-rescue-for-restaurants--ngos) |
| Finding a trusted local technician | [9. FixNeighbor](#9-fixneighbor--trusted-plumberelectrician-for-one-locality) |
| Commute pooling on a fixed route | [10. RoutePod](#10-routepod--office-route-carpool-with-trust) |
| Farmers selling small lots | [11. LotBoard](#11-lotboard--small-farmer-lot--buyer-matching) |
| Lost items in campuses/societies | [12. FoundHere](#12-foundhere--lost--found-for-a-closed-community) |

**Already in this repo:** a full build prompt for a [badminton club management app](./badminton-sports-app-prompt.md) (courts, coaches, attendance).

**Copy-paste build prompts (same style as the badminton brief):**

- [Family medicine adherence](./family-medicine-adherence-prompt.md)
- [Small clinic queue](./clinic-queue-prompt.md)
- [Document expiry vault](./document-expiry-vault-prompt.md)

---

## 1. DoseCircle — family medicine adherence

**Problem:** People miss doses, especially elders on 4–8 medicines a day. Family members only find out after a hospital visit. Pill boxes and generic reminder apps do not share a simple “did they take it?” signal with caregivers.

**Who it is for:** Adult children of aging parents; people with diabetes, BP, thyroid, post-surgery meds.

**Why a new product can win:** Most reminder apps are personal to-do lists. The gap is **shared accountability** (caregiver sees missed dose in minutes), **photo proof optional**, **local language**, and **offline-first** for poor network.

**MVP:** Medicine schedule per person; dose check-in; missed-dose SMS/push to 1–3 caregivers; simple history; no diagnosis, no e-pharmacy required.

**Avoid:** Storing full medical records, replacing a doctor, or selling medicines in v1.

---

## 2. QueueLite — small clinic queue + appointments

**Problem:** Patients wait 1–3 hours in small clinics with no visibility. Reception uses paper or WhatsApp. Doctors cannot tell who is next after walk-ins mix with appointments.

**Who it is for:** Single-doctor or 2–4 doctor clinics, dental offices, diagnostic collection centres.

**Why a new product can win:** Hospital HIS software is heavy and expensive. WhatsApp is chaotic. A **token + ETA + SMS** product for one clinic is enough.

**MVP:** Walk-in token, booked slot, “now serving”, SMS when 2 people ahead, doctor pause/break, daily list export. One clinic, one language.

**Avoid:** Full EMR, insurance billing, and multi-hospital networks in v1.

---

## 3. ExpiryVault — document and renewal reminders

**Problem:** Passport, visa, insurance, PUC, driving licence, rent agreement, domain, SSL, professional memberships—people forget until they pay a fine or cannot travel.

**Who it is for:** Households, freelancers, small business owners, NRIs with documents in two countries.

**Why a new product can win:** Calendar apps need manual events. Password managers store files but do not nag with **lead times** (90/30/7 days) or **shared family vault** with least privilege.

**MVP:** Encrypted document metadata (not necessarily the file); expiry date; reminder channels; shared access for spouse; audit of who viewed.

**Avoid:** Scanning Aadhaar/SSN as a “backup”; never store government ID numbers unless the user pastes them and you encrypt at rest.

---

## 4. SocietyDesk — apartment ops without WhatsApp chaos

**Problem:** Housing societies run on 12 WhatsApp groups: complaints, visitors, maintenance dues, gym booking, water tanker, vendor bills. Nothing is searchable; treasurers use Excel.

**Who it is for:** Secretaries, treasurers, residents of 20–200 unit societies.

**Why a new product can win:** MyGate-class apps are visitor-heavy and fee-heavy. Many small societies want **complaints + dues + notices** only.

**MVP:** Raise ticket with photo; status; dues ledger (manual payment mark); PDF notice; visitor optional later.

---

## 5. CounterBook — kirana / workshop billing

**Problem:** Small shops still use paper or illegal modified Excel. They need fast billing, stock of 200–2000 SKUs, and a simple tax invoice—not a full ERP.

**Who it is for:** Grocery, medical retail (careful with regulated drugs), mobile repair, auto spare shops.

**Why a new product can win:** Tally/Vyapar exist; the gap for learners is a **fast, offline, barcode-optional** counter that a shopkeeper can use in 2 taps. Differentiation: **credit (udhaar) ledger** that is first-class, not an afterthought.

**MVP:** Item master, bill, print/share PDF, daily sales, udhaar list, stock decrement. GST fields optional behind a flag.

---

## 6. ClassKeep — tuition fees, attendance, parent updates

**Problem:** Tuition teachers and small coaching centres collect fees in cash, mark attendance in a diary, and parents only hear when a test goes badly.

**Who it is for:** Home tutors, 20–150 student coaching batches.

**Why a new product can win:** School ERPs are overkill. WhatsApp broadcasts are one-way. Need **fee due + attendance + test marks** in one place.

**MVP:** Batches, students, fee cycles, attendance, one parent phone number, monthly due SMS.

**Related:** The badminton prompt in this repo is the sports analogue (courts instead of classrooms).

---

## 7. MusterPay — attendance + wage for small contractors

**Problem:** Site supervisors mark labour on paper; wage disputes are weekly. Overtime and advances (kharcha) are oral.

**Who it is for:** Civil contractors, housekeeping vendors, farm labour groups (10–80 workers).

**Why a new product can win:** Biometric attendance products are sold to factories. Small contractors need **muster + advance + weekly cash payout sheet** on a phone, in the local language.

**MVP:** Worker list, present/absent/half-day, daily wage rate, advances, weekly payable, PDF for owner.

**Avoid:** Replacing statutory payroll/PF/ESI in v1 unless you have legal help.

---

## 8. SurplusBridge — food rescue for restaurants + NGOs

**Problem:** Restaurants and event caterers dump edible food; NGOs and night shelters cannot see surplus in time. Phone trees fail after 9pm.

**Who it is for:** Restaurant managers, wedding caterers, city food banks, shelter coordinators.

**Why a new product can win:** Generic “donate food” apps die on **logistics + food safety + pickup SLA**. A city-scoped board with pickup windows and “claimed” locks is enough.

**MVP:** Post surplus (type, qty, pickup by, address); NGO claims; status; simple safety checklist (cooked time, veg/non-veg, chilled).

---

## 9. FixNeighbor — trusted plumber/electrician for one locality

**Problem:** People Google random numbers, get overcharged, or wait all day. Word-of-mouth does not scale past one building.

**Who it is for:** Residents in one pin code; independent technicians (not aggregators with 30% commission).

**Why a new product can win:** Urban Company is national and commission-heavy. A **society-verified technician roster** with job photos and “completed” confirmation can be hyperlocal.

**MVP:** Technician profile, service types, request, accept, done, rating by verified residents only.

---

## 10. RoutePod — office route carpool with trust

**Problem:** Same 20 people drive parallel routes to the same IT park. Fuel, parking, and time are wasted. Public carpool apps feel unsafe.

**Who it is for:** Employees of one company or one office park.

**Why a new product can win:** Trust comes from **company email / ID**, not from a public marketplace. Fixed routes, not “anywhere to anywhere.”

**MVP:** Home cluster → office, departure window, seats, recurring weekdays, in-app “I am in the car” ping. No payments in v1 (settle in cash/UPI outside).

---

## 11. LotBoard — small farmer lot → buyer matching

**Problem:** Small farmers sell through middlemen because they cannot reach 5 buyers for 200 kg of a vegetable. WhatsApp groups are noisy and not comparable.

**Who it is for:** FPOs, mandi traders, hotel buyers, farmers with a smartphone (or a kiosk operator).

**Why a new product can win:** Agri-tech giants chase credit and input sales. A **lot listing + pickup date + quality photo** board is simpler and still useful.

**MVP:** Crop, qty, grade, location, asking price, “interested” from verified buyers, phone reveal after both sides opt in.

---

## 12. FoundHere — lost & found for a closed community

**Problem:** ID cards, bottles, umbrellas, and laptops get lost in colleges, offices, and clubs. Emails and WhatsApp get ignored.

**Who it is for:** Campus admin, office facilities, sports clubs (pairs well with the badminton app).

**Why a new product can win:** Public lost-and-found sites attract spam. A **closed tenant** (one campus) with photo + last-seen location works.

**MVP:** Report lost, report found, match suggestions (category + location + date), claim with staff confirmation.

---

## Ideas that look real but are poor first products

- **Another ChatGPT wrapper** with no workflow and no user who already has a painful job.
- **Full hospital EMR / bank / government ID system** — regulation and liability will stall you.
- **Marketplace with two-sided cold start** (anything + anywhere) before you have a beachhead (one clinic, one society, one office).
- **Crypto / generic NFT** with no problem owner.

---

## Suggested first build (if you are learning Python)

1. **DoseCircle** or **ExpiryVault** — clear data model, auth, reminders (cron/Celery), almost no hardware.  
2. **QueueLite** — real-time-ish status; still one tenant.  
3. **ClassKeep** — if you liked the badminton domain (people + attendance + money).

Stack that matches this repo: **Python 3.12 + FastAPI or Django**, PostgreSQL, Redis for jobs, server-rendered admin (Django templates) or HTMX—no need for a heavy JS SPA.

---

## What to do next

1. Pick one row from the table.  
2. Open the matching prompt file (or write a one-page brief).  
3. Interview 5 users; change the MVP if they laugh at a feature.  
4. Ship a demo with seed data and a README, same bar as the badminton prompt.
