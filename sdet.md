# SDET 8-week plan (Java + Python + JavaScript)

**Goal:** In two months, study daily so you can **start SDET interviews** with a public GitHub project, a pipeline you own, and stories in Java, TypeScript, and Python—not only Selenium UI scripts.

**Starting point assumed:** automation engineer with **Java + Selenium**. You will not master every tool. You will be interview-ready on a **coherent stack**.

**Target combination:** Java depth (JUnit, REST Assured, Selenium kept) + TypeScript Playwright fluency + Python pytest fluency.

**Daily time:** **2–2.5 hours** on weekdays, **4 hours** Saturday, **3 hours** Sunday (~18 hours/week). If you only have 90 minutes/day, keep the weekday **hands-on** block and skip optional videos.

---

## How to use this file

1. Follow **one week at a time**. Do not binge weeks 3–8 of docs on day 1.
2. For every topic: **official docs → type the code yourself → commit**. Videos are for when docs are not enough.
3. Saturday is **project + generative AI lab** (same topics, different method).
4. Sunday is **review + 5 interview questions out loud**.
5. By Sunday of week 8 you should be applying, not still collecting courses.

**Lab repo (day 1 is done for you):** [`sdet-lab/`](sdet-lab/README.md) — `java-api/`, `python-api/`, `playwright-ts/`. CI is [`.github/workflows/sdet-lab.yml`](.github/workflows/sdet-lab.yml). Commit new tests there as you study.

---

## Consolidated syllabus (what interviews actually probe)

| Pillar | Must be able to do | Defer until after you have offers |
|---|---|---|
| **Coding** | Java collections/streams, TS async/types, Python pytest fixtures; small DSA (arrays, maps, strings) | Competitive programming |
| **API** | REST Assured + httpx + Playwright API; status, JSONPath, auth headers | Full GraphQL/gRPC unless the JD requires it |
| **UI** | Selenium 4 you already have; Playwright TS locators, fixtures, traces, POM | Cypress, Appium (learn if JD lists them) |
| **CI** | GitHub Actions: install, run, upload artifacts, fail the job | Kubernetes, Jenkins plugins deep-dive |
| **Env** | Docker + one Testcontainers example | Multi-cluster, service mesh |
| **Quality extras** | One k6 or Locust script; axe in Playwright; OWASP Top 10 *literacy* | Full security engineer / perf engineer role |
| **Design** | Test pyramid, flake policy, how you would test checkout/auth | Staff-level platform design |
| **AI (SDET-relevant)** | RAG over *your* docs/tests; evals; agent + tools; MCP literacy | Training an LLM from scratch, GPU clusters |

---

## Canonical study materials (use these first)

Prefer **docs + TAU + official YouTube**. Use other YouTube only if the official source is missing a demo.

### Hubs (video + structured courses)

| Source | URL | Use for |
|---|---|---|
| Test Automation University (free) | https://testautomationu.applitools.com/ | Playwright, Selenium, API, GitHub Actions — search the catalog |
| TAU: GitHub Actions for Testing | https://testautomationu.applitools.com/github-actions-for-testing/ | Week 2 CI |
| Playwright docs (best written) | https://playwright.dev/docs/intro | Weeks 3–4 |
| Playwright YouTube (Microsoft) | https://www.youtube.com/@Playwrightdev | Watch after reading the matching docs page |
| Ministry of Testing | https://www.ministryoftesting.com/ | Articles, community, interview mindset |
| GitHub Skills | https://skills.github.com/ | Git + Actions interactive |
| Microsoft Learn — Playwright | https://learn.microsoft.com/en-us/training/modules/build-with-playwright/ | Extra TS/Playwright module |

### Languages

| Topic | Docs | Video / interactive |
|---|---|---|
| Java | https://dev.java/learn/ · https://junit.org/junit5/docs/current/user-guide/ · https://www.baeldung.com/ | Keep Selenium knowledge; deepen JUnit 5 on Baeldung |
| TypeScript | https://www.typescriptlang.org/docs/handbook/intro.html · https://javascript.info/ | https://www.totaltypescript.com/tutorials (many free) |
| Python | https://docs.python.org/3/tutorial/ · https://docs.pytest.org/ | pytest docs are the course |
| Git | https://git-scm.com/book/en/v2 | https://learngitbranching.js.org/ |
| HTTP | https://developer.mozilla.org/en-US/docs/Web/HTTP | — |
| SQL | https://www.postgresql.org/docs/current/tutorial.html · https://mode.com/sql-tutorial/ | — |

### Automation and quality engineering

| Topic | Docs | Video |
|---|---|---|
| Selenium (keep sharp) | https://www.selenium.dev/documentation/ | TAU Selenium courses |
| REST Assured | https://rest-assured.io/ · https://github.com/rest-assured/rest-assured/wiki/Usage | TAU API courses; optional playlist https://www.youtube.com/playlist?list=PLMer2TvhZIw-8KszaIZFsOrE8MEJXVYoY |
| Playwright TS | https://playwright.dev/docs/writing-tests · https://playwright.dev/docs/best-practices · https://playwright.dev/docs/api-testing · https://playwright.dev/docs/ci | https://www.youtube.com/@Playwrightdev |
| Playwright Java | https://playwright.dev/java/docs/intro | After TS is fluent |
| Playwright Python | https://playwright.dev/python/docs/intro | Optional |
| Docker | https://docs.docker.com/get-started/ | Official: https://www.youtube.com/@docker |
| GitHub Actions | https://docs.github.com/en/actions · https://docs.github.com/en/actions/writing-workflows/quickstart | TAU Actions course |
| Testcontainers | https://testcontainers.com/getting-started/ · https://java.testcontainers.org/ | Guides on testcontainers.com |
| Allure | https://allurereport.org/docs/ | — |
| k6 | https://grafana.com/docs/k6/latest/ | Grafana k6 channel / docs examples |
| Locust | https://docs.locust.io/ | — |
| Accessibility | https://playwright.dev/docs/accessibility-testing · https://www.w3.org/WAI/fundamentals/ | — |
| OWASP | https://owasp.org/www-project-top-ten/ | — |
| OpenTelemetry | https://opentelemetry.io/docs/ | Skim only in week 7 |
| Pact / OpenAPI | https://docs.pact.io/ · https://learn.openapis.org/ | — |
| WireMock | https://wiremock.org/docs/ | — |
| Spring testing | https://spring.io/guides · https://docs.spring.io/spring-framework/reference/testing.html | If JD is Spring-heavy |

### Practice apps (always the same three)

- UI: https://the-internet.herokuapp.com/
- API: https://restful-booker.herokuapp.com/ · https://jsonplaceholder.typicode.com/
- OpenAPI: https://petstore.swagger.io/
- Security playground (legal, local): https://owasp.org/www-project-juice-shop/

### Communities

- Playwright Discord: https://aka.ms/playwright/discord
- Stack Overflow tags: `playwright`, `rest-assured`, `pytest`, `selenium`

---

## Daily rhythm (repeat every weekday)

| Minutes | Block | Rule |
|---|---|---|
| 15 | **Interview drill** | One coding puzzle *or* one “how would you test X” out loud |
| 45–60 | **Input** | Docs first; one TAU/official video if stuck |
| 60–90 | **Output** | Code in `sdet-lab`; tests must run |
| 10 | **Log** | 3 bullets: learned / broke / tomorrow |

**Do not** watch 2 hours of video with zero commits.

---

## Eight-week calendar

Weekend AI labs are specified under [Generative AI track](#generative-ai-track-learn-the-same-syllabus-a-second-way). Do them **in addition** to the Saturday project hours (split 2h project / 2h AI, or 2.5 / 1.5).

### Week 1 — Java as an SDET language + API pyramid base

**Outcome:** Maven + JUnit 5 + REST Assured suite against Restful Booker (or JSONPlaceholder). No new UI framework yet.

| Day | Study | Hands-on | Interview |
|---|---|---|---|
| Mon | https://martinfowler.com/articles/practical-test-pyramid.html · JUnit 5 user guide (annotations, assertions, parameterized) | Init `java-api/` Maven project; 5 JUnit tests of a small `String`/`List` util | Why API tests before UI? |
| Tue | REST Assured wiki Usage · MDN HTTP methods/status | GET/POST Restful Booker; assert status + JSON | Idempotency: what is it? |
| Wed | Auth: https://jwt.io/introduction · https://www.oauth.com/ (skim) | Booker auth token → authenticated call | Bearer vs Basic |
| Thu | Baeldung: REST Assured serialization / POJOs | Map JSON to POJO; negative tests (400/401) | How do you test error contracts? |
| Fri | OpenAPI: https://learn.openapis.org/ (1–2 pages) · Petstore | One test driven from an OpenAPI path | What belongs in a contract test? |
| Sat | Refactor: config, env base URL, logging. Optional TAU API course chapters | README: how to run | — |
| Sun | Review week 1 diffs | 5 LeetCode Easy (arrays/strings) in Java | Tell your pyramid story |

**Videos:** TAU API automation (catalog search). Optional Rest Assured playlist only after you have 5 passing tests.

### Week 2 — Git, Docker, GitHub Actions (pipeline you own)

**Outcome:** Push `java-api` tests; PR workflow runs Maven tests and uploads surefire/Allure or XML.

| Day | Study | Hands-on | Interview |
|---|---|---|---|
| Mon | Pro Git ch. 2–3 or Learn Git Branching | Branch/PR hygiene on `sdet-lab` | rebase vs merge |
| Tue | Docker Get Started (modules 1–2) | Dockerfile that runs `mvn test` | Why Docker for tests? |
| Wed | GHA quickstart + setup-java | Workflow on push/PR | How do you fail the build? |
| Thu | TAU GitHub Actions for Testing ch. 1–2 | Cache Maven; artifacts | Secrets vs variables |
| Fri | Allure docs (minimal) or JUnit XML only | Publish report artifact | Flake vs product bug |
| Sat | Docker official intro video if needed | Same tests in container locally | — |
| Sun | Write “CI quality gates” (smoke vs full) in README | 5 Java coding questions | Design: test a login API |

**Videos:** TAU https://testautomationu.applitools.com/github-actions-for-testing/ · Docker YouTube @docker · GitHub Skills Actions course on https://skills.github.com/

### Week 3 — TypeScript + Playwright core

**Outcome:** Playwright TS project; 8–12 tests on the-internet or Playwright’s own site; traces on failure.

| Day | Study | Hands-on | Interview |
|---|---|---|---|
| Mon | TS Handbook: types, interfaces, unions | `npx playwright init`; tsconfig strict | Why TypeScript for tests? |
| Tue | javascript.info: promises/async (if rusty) | Convert one test to async/await cleanly | event loop in one sentence |
| Wed | Playwright intro + writing tests | Locators: getByRole, getByLabel | Why not XPath-first? |
| Thu | Best practices + auto-waiting | Delete `waitForTimeout`; use web-first asserts | What causes flakes? |
| Fri | Trace viewer + UI mode | Fail a test on purpose; read the trace | How do you debug CI-only fails? |
| Sat | @Playwrightdev videos matching this week’s pages | POM for 2 pages | — |
| Sun | Compare Selenium vs Playwright (write 10 lines) | 5 TS type puzzles (Handbook exercises) | When keep Selenium? |

**Docs:** https://playwright.dev/docs/intro · https://playwright.dev/docs/writing-tests · https://playwright.dev/docs/best-practices · https://playwright.dev/docs/trace-viewer  
**Video:** https://www.youtube.com/@Playwrightdev  
**Course:** TAU Playwright (catalog) + https://learn.microsoft.com/en-us/training/modules/build-with-playwright/

### Week 4 — Playwright as a framework (API + UI + CI)

**Outcome:** Same repo: UI + Playwright `APIRequestContext` setup; GHA from https://playwright.dev/docs/ci ; HTML report artifact.

| Day | Study | Hands-on | Interview |
|---|---|---|---|
| Mon | Fixtures, projects, parallelism | `storageState` or API login then UI | Test isolation |
| Tue | API testing guide | Create resource via API, assert in UI | Test data strategy |
| Wed | Network mocking (docs) | Mock one API for a UI test | When to mock vs real |
| Thu | Accessibility testing page | axe in one spec | a11y in CI: what fails the build? |
| Fri | Playwright CI page (copy, then understand) | GHA for Playwright + traces on failure | Sharding |
| Sat | Stabilise flakes; tags `@smoke` | Smoke job vs full job | — |
| Sun | README architecture diagram | 5 “explain this Playwright snippet” | Design: test a checkout |

### Week 5 — Python pytest + same APIs

**Outcome:** `python-api/` with pytest + httpx covering the **same** Restful Booker cases as Java (proves you can switch languages).

| Day | Study | Hands-on | Interview |
|---|---|---|---|
| Mon | Python tutorial ch. 3–5, 9 (classes) | venv/uv; first pytest | Python vs Java for API tests |
| Tue | pytest fixtures, parametrize, conftest | Parametrize status codes | fixture scope |
| Wed | httpx docs | Rewrite Booker GET/POST | sync vs async httpx |
| Thu | Pydantic | Validate response schema | contract vs schema |
| Fri | pytest-xdist (optional) + coverage.py skim | Markers `smoke` | — |
| Sat | Add Python job to GHA (`setup-python`) | All three folders in one pipeline | — |
| Sun | Compare Java vs Python suite (table in README) | 5 Python list/dict exercises | When pick Python in a Java shop? |

**Docs:** https://docs.python.org/3/tutorial/ · https://docs.pytest.org/ · https://www.python-httpx.org/ · https://docs.pydantic.dev/

### Week 6 — Test infrastructure: Testcontainers, doubles, reports

**Outcome:** One Testcontainers test (Postgres or WireMock) **or** WireMock without containers if Docker is heavy; Allure or Playwright report linked from README.

| Day | Study | Hands-on | Interview |
|---|---|---|---|
| Mon | Testcontainers getting started | Java JUnit + Postgres *or* WireMock | Why not a shared QA DB? |
| Tue | WireMock docs | Stub Booker-like API; test against stub | Stub vs mock vs fake |
| Wed | Pact *or* OpenAPI schemathesis skim | One consumer contract **or** one Schemathesis run | Consumer-driven contracts |
| Thu | SQL tutorial (joins) | Assert DB row after API (if Testcontainers) | test data factories |
| Fri | Flake policy write-up | Quarantine tag + owner in README | Retry: when is it a lie? |
| Sat | Polish reports | Allure or keep Playwright HTML | — |
| Sun | System design: “test a payments service” 1 page | 5 SQL questions | — |

**Docs:** https://testcontainers.com/getting-started/ · https://wiremock.org/docs/ · https://docs.pact.io/ · https://schemathesis.readthedocs.io/

### Week 7 — Performance literacy, security literacy, interview coding + design

**Outcome:** One k6 **or** Locust script against JSONPlaceholder; OWASP Top 10 notes; 30–45 min timed Java coding daily.

| Day | Study | Hands-on | Interview |
|---|---|---|---|
| Mon | k6 docs intro **or** Locust quickstart | 50 VUs smoke; record p95 | latency vs throughput |
| Tue | OWASP Top 10 (read summaries) | Checklist vs your Booker tests (authz) | IDOR in one sentence |
| Wed | Playwright a11y recap | Fail CI on critical axe | — |
| Thu | OpenTelemetry “what is a trace” (1 hour max) | Add trace-id note to README debug section | How do you debug microservices E2E? |
| Fri | DSA: maps, two pointers, stacks | 4 timed Easy/Medium Java | Talk while coding |
| Sat | Mock interview: 45 min coding + 30 min test design | Record yourself | — |
| Sun | Selenium 4 refresh (Grid, waits) so you don’t rust | 10 Selenium vs Playwright comparison Qs | Legacy suite migration |

**k6:** https://grafana.com/docs/k6/latest/  
**Locust:** https://docs.locust.io/  
**OTel:** https://opentelemetry.io/docs/  
**AWS skim (optional):** https://skillbuilder.aws/ Cloud Practitioner free digital — only if JDs ask AWS.

### Week 8 — Capstone, interviews, AI quality story

**Outcome:** Public repo README that a hiring manager can run in 10 minutes; 20 STAR stories; applications sent.

| Day | Study | Hands-on | Interview |
|---|---|---|---|
| Mon | Capstone: README, architecture, how to run all suites | Fix CI until green | — |
| Tue | 15 behavioral STAR (conflict, flake, missed bug, pipeline) | Write them down | — |
| Wed | 15 technical Q: HTTP, waits, pyramid, Docker, GHA | Answer without notes | — |
| Thu | Live coding practice | 2 Medium Java + 1 pytest fixture design | — |
| Fri | Apply to 5–10 roles that match Java SDET + Playwright | Tailor README link | — |
| Sat | **AI capstone** (see below): RAG over your own `sdet-lab` + this file | Demo in README | How do you test an LLM feature? |
| Sun | Rest + light review | Second mock interview | Keep applying |

**You are ready to attend interviews if:** CI is green, you can explain every folder, you can code a REST Assured or Playwright test on a whiteboard, and you have a 5-minute “how I would test X” structure.

---

## Generative AI track (learn the same syllabus a second way)

Use AI as a **tutor, indexer, and agent with tools**—not as a replacement for running tests. Interviewers will ask what you **verified**.

### Mental model (learn this once, week 1 Sunday + week 8)

| Approach | What it is | When SDETs use it | What it is *not* |
|---|---|---|---|
| **Prompting** | You + a chat model | Explain a stack trace, draft a test, quiz you | Source of truth |
| **RAG** | Retrieve chunks from *your* docs/code, then generate | “What does our framework do for retries?” | Training a new model |
| **Fine-tuning / training** | Change model weights on a dataset | Rare for personal SDET study; companies may fine-tune on internal bugs | You will **not** train GPT from scratch in 8 weeks |
| **Agents** | Model + **tools** (run tests, open browser, grep repo) in a loop | Generate then *execute* tests; triage failures | Magic autonomy without evals |
| **MCP** | Standard way to expose tools (e.g. Playwright) to an LLM client | Cursor/Claude + Playwright MCP | A replacement for Playwright Test |
| **Evals** | Dataset of Q/A or “expected test behavior”; score the model | **This is the SDET skill for AI products** | Skipping assertions because “the model said so” |

**Do not spend weeks on CUDA or pretraining.** Spend hours on **RAG + evals + one agent with tools**. That is what SDET JDs mean by AI.

### Official learning path for AI (evenings / Saturdays)

Complete in this order (short courses, not a second master’s degree):

| Order | Resource | URL | Time |
|---|---|---|---|
| 1 | RAG concept + Chat with your data | https://www.deeplearning.ai/short-courses/langchain-chat-with-your-data/ | ~1 hour |
| 2 | Hugging Face Agents course (free) | https://huggingface.co/learn/agents-course | sample 2–4 units |
| 3 | LangChain Academy / LangGraph RAG agent | https://academy.langchain.com/ · https://docs.langchain.com/oss/python/langgraph/agentic-rag | 1 Saturday |
| 4 | Evaluate RAG | https://docs.langchain.com/langsmith/evaluate-rag-tutorial | 1 evening |
| 5 | OpenAI evals | https://platform.openai.com/docs/guides/evals | skim + one eval |
| 6 | promptfoo (test LLM output like tests) | https://www.promptfoo.dev/docs/intro/ | 1 evening |
| 7 | MCP spec (literacy) | https://modelcontextprotocol.io/ | 45 min |
| 8 | Playwright MCP | https://github.com/microsoft/playwright-mcp | week 8 |
| 9 | Fine-tuning *literacy* only | https://huggingface.co/learn/nlp-course (transformer intuition) · OpenAI fine-tuning guide if you use their API | optional week 8 |
| 10 | Neural net intuition (optional) | https://www.3blue1brown.com/topics/neural-networks | Sunday background |

**NLP course** is for vocabulary (embeddings, tokens). Stop before training large models.

### Saturday AI labs (parallel to weeks 1–8)

Each lab is **the week’s topic**, learned via AI. Still commit code you ran yourself.

| Week | AI lab (90–120 min) |
|---|---|
| 1 | **Tutor mode:** Paste REST Assured wiki section; ask the model to quiz you; then write tests **without** pasting the solution. Rule: if you cannot explain a line, delete it. |
| 2 | **RAG v0:** Put Docker + GHA docs PDFs/markdown in a folder. Use a simple RAG notebook (DeepLearning.AI course pattern: chunk → embed → retrieve → answer). Ask “how do I cache Maven in GHA?” and **verify against official docs**. |
| 3 | **Grounded Playwright tutor:** Index https://playwright.dev/docs/best-practices (save HTML/MD). Refuse answers that are not in retrieved chunks (prompt: “only use context”). |
| 4 | **Agent with tools (narrow):** Script: LLM proposes a Playwright test → you or a tool **runs** `npx playwright test` → paste failure back. Loop until green. Log every tool call. This *is* an agent; keep max 8 steps. |
| 5 | **Pytest generator + eval:** Generate 10 httpx tests; run pytest; measure how many passed without edits. That number is your **eval**. Improve the prompt (not the model). |
| 6 | **Failure-triage agent:** Tool 1: read surefire/Playwright JSON report. Tool 2: grep source. Output: flake vs product vs env. You label 10 failures as ground truth (eval set). |
| 7 | **promptfoo or OpenAI evals:** 15 questions: “p95 vs average”, “when to mock”. Score the tutor. |
| 8 | **Capstone:** (1) RAG over `sdet.md` + your README. (2) Playwright MCP in Cursor: explore the-internet, then **convert** exploration into committed tests. (3) One-page “How I would test a RAG chatbot” (retrieval metrics, groundedness, jailbreak/refusal, latency, eval dataset). |

### How to build a tiny RAG (enough to talk in interviews)

1. Collect files: this `sdet.md`, Playwright best-practices, your test `README`.
2. Split into chunks (headings / 500–1000 tokens).
3. Embed with a hosted API or a local sentence-transformers model ([Hugging Face sentence-transformers](https://huggingface.co/sentence-transformers)).
4. Store vectors (Chroma / FAISS — follow the DeepLearning.AI notebook).
5. At query time: retrieve top-k → prompt: answer only from chunks + cite file names.
6. **Eval:** 10 questions with known answers; track faithfulness (did it invent a Playwright API?).

That is RAG. **Training** would mean updating model weights; skip it unless a job is ML-platform SDET.

### How to create an agent (enough to talk in interviews)

An agent is a loop:

1. Model chooses a **tool** (run tests, read file, browser snapshot).
2. Your code **executes** the tool (never let it run unbounded shell on a shared machine).
3. Observation goes back to the model.
4. Stop on success, max steps, or human approval.

Implement with LangGraph tutorial above **or** a 40-line Python loop. Expose Playwright via [playwright-mcp](https://github.com/microsoft/playwright-mcp) instead of inventing browser tools.

Patterns worth naming in interviews (from real SDET usage):

- Generate tests from OpenAPI / tickets, then **run** them
- Triage CI failures from reports + traces
- Exploratory agent → human turns session into regression tests

Patterns to distrust: self-healing locators that hide product bugs; agents that click production.

### Alternative ways to study each week (when you are stuck)

| If you… | Do this instead of more video |
|---|---|
| Learn by teaching | Feynman: 5-minute voice note; RAG tutor asks follow-ups |
| Learn by testing | Write the test first; use AI only for locator ideas; you decide assertions |
| Learn by reading | Official docs only; AI summarizes *after* you read |
| Learn by building | AI as pair programmer in Cursor with “do not write tests I didn’t ask for” |
| Learn visually | Playwright trace + @Playwrightdev ; 3Blue1Brown only for ML vocab |

### Interview answers for AI (memorize the shape)

- **RAG vs fine-tune:** RAG when knowledge changes (docs, tests); fine-tune when style/format must change and you have a clean dataset and evals.
- **How do you test a chatbot?** Golden questions, retrieval hit-rate, groundedness/faithfulness, toxicity/safety, latency, regression evals in CI (promptfoo).
- **What is an agent?** LLM + tools + stop conditions + logging; you test tools and the loop, not only the prose.
- **MCP?** Protocol so IDEs/models can call tools like Playwright consistently.

---

## Interview pack (start using from week 2)

**Coding:** Java Easy/Medium on arrays, strings, HashMap, two pointers (30 min, talk aloud).  
**Automation live:** “Write a REST Assured GET + POST” or “Playwright login with getByRole.”  
**Design:** Login, checkout, file upload, webhook, flaky suite, CI strategy.  
**Behavioral:** flake you fixed, bug automation missed, disagreement with a developer, time you stopped a release.

Apply from **Friday of week 8**; if CI and README are ready earlier, apply from week 7.

---

## What not to do in two months

- Do not start Cypress, Appium, Kafka, and K8s in parallel.
- Do not collect 15 Udemy courses; TAU + official docs + one repo.
- Do not train an LLM. Learn RAG, evals, and one agent.
- Do not skip CI. A local-only suite is still an automation-engineer portfolio.

---

## Communities

- https://www.ministryoftesting.com/
- https://testautomationu.applitools.com/
- https://aka.ms/playwright/discord

Ask questions with a failing test and a stack trace, not “how do I become SDET.”
