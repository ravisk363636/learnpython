# From Java Selenium automation engineer to SDET

Java + Selenium is still a strong **enterprise baseline**. The SDET step-up is not “more page objects.” It is **software engineering for quality**: you design test systems, own pipelines, test APIs and services, and treat quality as a product of the delivery platform.

You do not need equal depth in Java, Python, and JavaScript/TypeScript on day one. You need **one primary language at SDET depth** (Java is a valid primary) and **working fluency in the other two**, because teams mix them.

**Practical combination from a Java Selenium starting point:** Java depth + TypeScript Playwright fluency + Python pytest fluency.

Use **TypeScript, not only JavaScript**, for anything you will maintain: types catch bad fixtures, API payloads, and page objects.

---

## What actually changes vs automation engineer

| Automation engineer (typical) | SDET (what hiring managers mean) |
|---|---|
| Writes UI scripts | Designs a **test architecture** (layers, contracts, data, environments) |
| Owns a suite | Owns **release gates** in CI/CD |
| Debugs flaky locators | Debugs **systems** (logs, traces, contracts, infra) |
| “QA tools” | Same languages, patterns, and reviews as developers |

You already have the most common pairing in job posts: **Java + Selenium**. Keep it. Add depth around it, then add the layers that pay more: **API, pipelines, containers, system design**.

Automation is the floor. UI scripts alone are not a premium skill.

---

## How the three languages split in SDET work

| Language | Where it wins | Typical hiring signal |
|---|---|---|
| **Java** | Enterprise UI (Selenium), Spring services, REST Assured, banks/ERP | Strongest **Java + Selenium** pairing in many job posts |
| **Python** | API, data, scripts, performance glue, ML/eval of AI products | Fast to write; strong in backend/data-heavy QA |
| **JavaScript / TypeScript** | Frontend, Playwright, Cypress, Node APIs, GitHub Actions glue | Largest overlap with **new** web automation; TS preferred over plain JS |

---

## Target stack

Use this as a resume and study map. You do not need every tool; you need **one coherent stack** you can explain end to end.

### 1. Programming (this is the real SDET filter)

SDET interviews fail more often on **coding + design** than on “which locator strategy.”

**Java**

- Java 17+, collections, concurrency basics, streams, exceptions, generics
- OOP + design patterns that show up in frameworks: builder, factory, strategy, facade
- Clean code: SOLID, immutability, no god Page classes
- Unit testing of your own framework: JUnit 5, AssertJ, Mockito
- Maven/Gradle

**Python**

- 3.11+, typing (`list[str]`, Pydantic), virtualenv/uv/poetry
- pytest, fixtures, parametrize
- `httpx` / `requests`, dataclasses
- asyncio at a reading level

**JavaScript / TypeScript**

- ES2022+, **TypeScript** (strict), npm/pnpm
- async/await, Promises, modules
- Jest or Vitest, Playwright test runner

Cross-language skills interviews actually test: data structures, HTTP, OOP vs composition, designing a small framework, reading someone else’s code.

### 2. Test pyramid (stop living only in UI)

| Layer | Java | Python | JS/TS |
|---|---|---|---|
| Unit / component | JUnit 5, TestNG, PIT mutation testing | pytest, coverage.py, mutmut (optional) | Vitest or Jest, Testing Library, Stryker |
| API / contract | REST Assured, Spring `WebTestClient` / `MockMvc`, Jackson, WireMock, Pact / Spring Cloud Contract | pytest + `httpx`, Pydantic, Schemathesis, Pact Python | Playwright `APIRequestContext`, supertest, Pact JS, Zod |
| UI | Selenium 4 (W3C WebDriver), Playwright for Java | Selenium + pytest, Playwright for Python | **Playwright Test + TypeScript** (strongest for new work); Cypress in JS-first teams |
| Mobile (if relevant) | Appium 2 | Appium 2 | Appium / WDIO; Playwright for mobile web |

Enterprise still runs Selenium. New greenfield and many “modern SDET” posts prefer **Playwright**. Learn Playwright without throwing Selenium away.

Shared ideas (language-agnostic): OpenAPI as source of truth, consumer-driven contracts, idempotency, auth (OAuth2/JWT), event-driven waits (not `sleep`).

Patterns transfer between tools: page object / screenplay, fixture management, data builders, custom assertions.

### 3. Backend and architecture literacy

Talk like you understand the app, not only the browser:

- REST, HTTP, auth (**OAuth2/OIDC, JWT**), idempotency, retries
- **Microservices**: service boundaries, eventual consistency, test doubles vs real env
- **Message queues** (Kafka/Rabbit) at “can I write a consumer test / wait for an event” level
- **GraphQL** if the UI is GraphQL-backed
- **Spring Boot** enough to read controllers, profiles, Testcontainers-style integration tests

### 4. CI/CD and DevOps (this is the salary jump)

Pipeline ownership beats a third UI framework.

- Git (branches, PRs, bisect, hooks)
- **GitHub Actions** and/or **Jenkins** / GitLab CI
- **Docker**: run tests in the same image as CI
- Parallelism, sharding, retries with quarantine policy (not “retry until green”)
- Test reporting: Allure, JUnit XML, Playwright traces
- Secrets, environments, feature flags

Language-specific packaging:

- Java: Maven/Gradle cache, Surefire/Failsafe
- Python: poetry/uv, pytest `-n` (pytest-xdist)
- JS/TS: pnpm cache, Playwright browser cache, matrix shards

Kubernetes is useful **after** Docker + CI are solid, not before.

### 5. Cloud

One cloud is enough: **AWS** is the most common (S3 artifacts, IAM, ECS/EKS at a high level, CloudWatch). Azure if you target Microsoft shops.

### 6. Observability (how SDETs debug now)

Flakes are often **not** locators. They are timing, data, downstream 5xx, or missing isolation.

- Structured logs
- **OpenTelemetry** / traces (Jaeger, Grafana Tempo)
- Metrics: Prometheus + Grafana at a reading level
- Tie a failed E2E to a **trace id**, not a screenshot only

### 7. Quality beyond functional UI

- **Performance**: k6 (JS) or JMeter; Locust (Python); know p95 vs average
- **Security testing literacy**: OWASP Top 10, authz vs authn, dependency scanning; not “become a pentester”
- **Accessibility**: axe-core in the pipeline
- **Chaos / resilience** (optional, senior): timeouts, retries, circuit breakers

### 8. AI (trend, not a replacement for engineering)

The trend is **AI-assisted quality**, not “prompt until the suite exists”:

- Copilot/Cursor for scaffolding tests you still **review**
- Self-healing locators (use carefully; they hide product bugs)
- LLM-generated tests grounded in **your** repo, OpenAPI, and acceptance criteria
- **Testing AI products**: evals, golden datasets, hallucination/regression of model output
- MCP / agent workflows appear in some senior interviews; treat as **orchestration + judgment**, not a tool list to memorize

Python still dominates **evals, datasets, pandas, pytest for LLM output**. TS/JS dominates **Playwright MCP / agent + browser**. Java dominates **enterprise frameworks** the agents must respect.

---

## Trends that should change how you study

1. **Automation is the floor.** UI scripts alone are not a premium skill.
2. **Playwright + TypeScript** is the default for *new* web suites; Selenium remains huge in banks, ERP, older Java estates.
3. **API-first and contract tests** beat a giant UI suite.
4. **Shift-left**: SDETs pair on stories, review PRs, add tests next to production code.
5. **Test as infrastructure**: environments via Testcontainers, ephemeral envs, not one shared QA box.
6. **Quality gates in the pipeline**: coverage of *risk*, flake budgets, smoke vs full vs nightly.
7. **System design for test platforms**: grid vs cloud browsers, artifact storage, reporting, data factories.
8. **AI in the loop**, with humans owning strategy, domain, and “when not to trust the agent.”

---

## Three canonical stacks (master one, speak the others)

Pick **one** as the repo you show; keep the others at “I can contribute in a week.”

**A. Enterprise Java SDET (current base)**  
Java 17, JUnit 5, Selenium 4, REST Assured, Testcontainers, Maven, Jenkins/GHA, Allure, Docker.  
*Add:* Playwright Java or a small TS Playwright sidecar.

**B. Modern web SDET (highest overlap with new postings)**  
TypeScript, Playwright Test, API tests in the same project, Zod, GitHub Actions, Docker, traces on failure, axe.  
*Add:* Node/Express or Next.js enough to read the app.

**C. API / data / platform SDET**  
Python, pytest, httpx, Pydantic, Testcontainers, SQL, Locust or k6, GHA.  
*Add:* contracts + Kafka/Redis at “can test it” level.

A strong SDET is **A + B**, with Python for C-shaped work (data setup, reports, AI evals, glue).

**Resume-shaped stack (Java SDET with the other two languages):**

- **Core:** Java 17+, Maven/Gradle, Git, JUnit 5 / TestNG, Selenium 4, REST Assured, Jackson, Allure
- **Modern add:** Playwright (Java or TS), Testcontainers, WireMock, Awaitility
- **JS/TS:** Playwright Test, Zod, GitHub Actions
- **Python:** pytest, httpx, Pydantic
- **Delivery:** GitHub Actions or Jenkins, Docker, parallel CI, Allure + traces
- **Data/env:** SQL, Faker / factory pattern, test users via API not UI
- **Cloud/obs (one each):** AWS basics, OpenTelemetry or at least CloudWatch/ELK reading

That combination reads as SDET. “Selenium + Cucumber + Jenkins job I didn’t write” still reads as automation engineer.

Example resume line: *SDET-style automation across Java (Selenium, REST Assured, JUnit), TypeScript (Playwright), and Python (pytest, API/data), with Dockerized CI, contract-aware API tests, and pipeline quality gates.*

---

## Shared engineering layer (this is the SDET part)

Regardless of language:

- Test pyramid and risk-based gates
- Page objects / screenplay / fixtures — patterns transfer
- CI as the product: smoke / full / nightly
- Flake policy, quarantine, owners
- System design: how you would test checkout, auth, or a worker pipeline
- Shift-left: PR reviews, tests next to production code

You do not become an SDET by collecting tools. You become one when you can **design how quality is built into the software and the pipeline**, using Java/Selenium as one layer—not the whole job.

---

## How to sequence the move (high ROI order)

1. **Deepen Java** so you look like an engineer (framework design, API tests, CI you own).
2. **API automation + contract thinking** on a real service (not another login UI).
3. **CI you own**: PR smoke, nightly full, artifacts, fail-the-build policy.
4. **Dockerize** the suite; kill “works on my machine.”
5. **TypeScript + Playwright** on a small app (UI + API in one repo).
6. **Python + pytest + httpx** against a real API; add one Locust or k6 scenario.
7. **System design**: how you would test a checkout, payments, or auth service (layers, data, risks, gates).
8. **One cloud + traces** so you can debug a failure without guessing.
9. Docker + one pipeline that runs **two** language suites (e.g. Java API + TS UI).
10. AI tools last, on top of that foundation.

**Portfolio that converts:** a public repo with a small app (or Testcontainers against a real API), pyramid of tests, CI badge, Allure/Playwright report, README that explains *why* tests live where they live. Interviewers look for that more than a 400-test Selenium dump.

---

## Systematic learning path (docs first)

Use **official docs first**, then one structured course track, then a **single GitHub project** that ties the three languages together. Paid Udemy courses go stale; docs and TAU stay closer to the tools.

How to study (so this does not become 40 open tabs):

1. One **primary language week** at a time (Java already known → TS next → Python).
2. Every topic: **docs tutorial → 20–40 lines in your repo → commit**.
3. Skip random YouTube playlists until you have read the official “intro + best practices” pages.
4. Capstone: one repo with **Java API tests + TypeScript Playwright UI + Python pytest API/data**, Docker, GitHub Actions.

Hubs that organize many free courses:

- [Test Automation University](https://testautomationu.applitools.com/) — Selenium, Playwright, API, CI (free)
- [Ministry of Testing](https://www.ministryoftesting.com/) — community, articles, learning paths
- [QA to SDET roadmap (2026 overview)](https://qaskills.sh/blog/qa-to-sdet-roadmap-2026) — sequencing, not a substitute for docs

### Phase 0 — Testing as engineering (1–2 days)

| Topic | Learn here |
|---|---|
| Test pyramid | [The Practical Test Pyramid (Martin Fowler)](https://martinfowler.com/articles/practical-test-pyramid.html) |
| Testing trophy | [The testing trophy and testing classifications](https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications) |
| Arrange-Act-Assert | TAU intro courses on [Test Automation University](https://testautomationu.applitools.com/) |

**Done when:** you can explain why a login UI test is the wrong *first* test for a checkout service.

### Phase 1 — Languages

#### Java (deepen, don’t restart)

| Topic | Link |
|---|---|
| Official learn track | [dev.java/learn](https://dev.java/learn/) |
| Language tutorials | [Oracle Java Tutorials](https://docs.oracle.com/javase/tutorial/) |
| Practical articles | [Baeldung](https://www.baeldung.com/) (JUnit 5, REST Assured, Testcontainers) |
| JUnit 5 | [JUnit 5 User Guide](https://junit.org/junit5/docs/current/user-guide/) |
| AssertJ | [AssertJ docs](https://assertj.github.io/doc/) |
| Mockito | [Mockito docs](https://site.mockito.org/) |
| Maven | [Maven Getting Started](https://maven.apache.org/guides/getting-started/) |
| Gradle | [Gradle Getting Started](https://docs.gradle.org/current/userguide/getting_started.html) |

#### JavaScript then TypeScript

| Topic | Link |
|---|---|
| JS in order | [javascript.info](https://javascript.info/) |
| Browser/JS reference | [MDN JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) |
| TypeScript Handbook | [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html) |
| TS exercises | [Total TypeScript tutorials](https://www.totaltypescript.com/tutorials) (many free) |
| Node packages | [npm docs](https://docs.npmjs.com/) |

#### Python

| Topic | Link |
|---|---|
| Official tutorial | [Python Tutorial](https://docs.python.org/3/tutorial/) |
| Typing | [typing docs](https://docs.python.org/3/library/typing.html) |
| pytest | [pytest docs](https://docs.pytest.org/) |
| HTTP client | [httpx docs](https://www.python-httpx.org/) |
| Data validation | [Pydantic](https://docs.pydantic.dev/) |
| Packaging | [pip](https://pip.pypa.io/en/stable/), [uv](https://docs.astral.sh/uv/), [Poetry](https://python-poetry.org/docs/) |

**Done when:** you can write JUnit tests, a TS function with types, and a pytest parametrize test without copying.

### Phase 2 — Git, HTTP, SQL

| Topic | Link |
|---|---|
| Git | [Pro Git book](https://git-scm.com/book/en/v2) · [Learn Git Branching](https://learngitbranching.js.org/) |
| HTTP | [MDN HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP) |
| OpenAPI | [Learn OpenAPI](https://learn.openapis.org/) |
| SQL | [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html) · [Mode SQL tutorial](https://mode.com/sql-tutorial/) |
| Auth | [OAuth 2.0](https://www.oauth.com/) · [JWT introduction](https://jwt.io/introduction) |

### Phase 3 — UI automation (Selenium stay + Playwright add)

#### Selenium (Java / Python / JS)

| Topic | Link |
|---|---|
| Official docs (all languages) | [Selenium Documentation](https://www.selenium.dev/documentation/) |
| Getting started | [Using Selenium](https://www.selenium.dev/documentation/webdriver/getting_started/using_selenium/) |
| Grid | [Selenium Grid](https://www.selenium.dev/documentation/grid/) |
| Free courses | [TAU](https://testautomationu.applitools.com/) |

#### Playwright

| Language | Intro | Follow-on |
|---|---|---|
| **TypeScript** (priority) | [Playwright intro](https://playwright.dev/docs/intro) | [Writing tests](https://playwright.dev/docs/writing-tests) · [Best practices](https://playwright.dev/docs/best-practices) · [Trace viewer](https://playwright.dev/docs/trace-viewer) · [API testing](https://playwright.dev/docs/api-testing) · [CI](https://playwright.dev/docs/ci) |
| **Java** | [Playwright for Java](https://playwright.dev/java/docs/intro) | Same topics in the Java docs tree |
| **Python** | [Playwright for Python](https://playwright.dev/python/docs/intro) | Same |

Microsoft videos: [Playwright YouTube](https://www.youtube.com/@Playwrightdev).

Cypress only if the job is Cypress-heavy: [Cypress docs](https://docs.cypress.io/).

**Done when:** a Playwright TS suite on a public demo with traces on failure + GitHub Actions from the [CI page](https://playwright.dev/docs/ci).

### Phase 4 — API, contracts, test doubles

| Topic | Link |
|---|---|
| REST Assured (Java) | [rest-assured.io](https://rest-assured.io/) · [Usage wiki](https://github.com/rest-assured/rest-assured/wiki/Usage) |
| Spring HTTP tests | [Spring Testing](https://docs.spring.io/spring-framework/reference/testing.html) · [Spring Guides](https://spring.io/guides) |
| Python HTTP + pytest | [httpx](https://www.python-httpx.org/) + [pytest](https://docs.pytest.org/) |
| TS API in Playwright | [Playwright API testing](https://playwright.dev/docs/api-testing) |
| OpenAPI | [Learn OpenAPI](https://learn.openapis.org/) · [Swagger Editor](https://editor.swagger.io/) |
| Consumer-driven contracts | [Pact docs](https://docs.pact.io/) |
| Mocks (Java) | [WireMock](https://wiremock.org/docs/) |
| Mocks (Node) | [MSW](https://mswjs.io/docs/) |
| Schema-based API tests | [Schemathesis](https://schemathesis.readthedocs.io/) (Python) |

**Done when:** tests hit a real API (or WireMock), assert JSON, and one contract or OpenAPI-generated check exists.

### Phase 5 — Docker + Testcontainers

| Topic | Link |
|---|---|
| Docker | [Docker Get Started](https://docs.docker.com/get-started/) · [Dockerfile reference](https://docs.docker.com/reference/dockerfile/) |
| Testcontainers overview | [Getting started](https://testcontainers.com/getting-started/) |
| Java | [Testcontainers Java](https://java.testcontainers.org/) · [Lifecycle guide](https://testcontainers.com/guides/testcontainers-container-lifecycle/) |
| Python | [testcontainers-python](https://testcontainers-python.readthedocs.io/) |
| Node | [Testcontainers Node](https://node.testcontainers.org/) |

**Done when:** a test starts Postgres (or WireMock) in Docker and the suite is reproducible on a clean machine.

### Phase 6 — CI/CD

| Topic | Link |
|---|---|
| GitHub Actions | [Actions docs](https://docs.github.com/en/actions) · [Quickstart](https://docs.github.com/en/actions/writing-workflows/quickstart) |
| Playwright on GHA | [Playwright CI](https://playwright.dev/docs/ci) |
| Jenkins | [Jenkins User Handbook](https://www.jenkins.io/doc/) |
| Reporting | [Allure Report](https://allurereport.org/docs/) |
| Java on GHA | [setup-java](https://github.com/actions/setup-java) |
| Python on GHA | [setup-python](https://github.com/actions/setup-python) |

**Done when:** PR runs smoke tests; main runs more; reports/traces upload as artifacts; a red test fails the job.

### Phase 7 — Performance, a11y, security literacy, observability

| Topic | Link |
|---|---|
| k6 (JS) | [Grafana k6 docs](https://grafana.com/docs/k6/latest/) |
| Locust (Python) | [Locust docs](https://docs.locust.io/) |
| JMeter | [JMeter User Manual](https://jmeter.apache.org/usermanual/index.html) |
| Accessibility | [WAI fundamentals](https://www.w3.org/WAI/fundamentals/) · [axe-core](https://github.com/dequelabs/axe-core) · [Playwright accessibility testing](https://playwright.dev/docs/accessibility-testing) |
| OWASP Top 10 | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| ZAP | [ZAP docs](https://www.zaproxy.org/docs/) |
| OpenTelemetry | [OTel docs](https://opentelemetry.io/docs/) · [Java](https://opentelemetry.io/docs/languages/java/) · [JS](https://opentelemetry.io/docs/languages/js/) · [Python](https://opentelemetry.io/docs/languages/python/) |
| Cloud (pick AWS) | [AWS Skill Builder](https://skillbuilder.aws/) |
| Mobile when needed | [Appium docs](https://appium.io/docs/en/latest/) |

### Phase 8 — System design and AI-assisted testing (after the foundation)

| Topic | Link |
|---|---|
| Test architecture | Fowler pyramid (Phase 0) + your own writeup of “how I would test X” |
| Playwright MCP | [playwright-mcp](https://github.com/microsoft/playwright-mcp) · [playwright.dev](https://playwright.dev) |
| Model Context Protocol | [MCP specification](https://modelcontextprotocol.io/) |
| Testing ML/LLM systems | [OpenAI evals](https://platform.openai.com/docs/guides/evals) · [promptfoo](https://www.promptfoo.dev/docs/intro/) |

Do this **last**. Interviews still fail people who cannot design an API suite or a pipeline.

---

## Suggested calendar (same stack, three languages)

| Block | Focus | Main links |
|---|---|---|
| 1 | Java JUnit + REST Assured + Maven | JUnit 5, REST Assured wiki, Baeldung |
| 2 | GitHub Actions + Docker for that suite | GHA quickstart, Docker get started |
| 3 | TypeScript Handbook + Playwright intro → best practices → CI | TS Handbook, playwright.dev |
| 4 | Python tutorial + pytest + httpx against the same API | Python tutorial, pytest, httpx |
| 5 | Testcontainers in **one** language | Testcontainers Java or Python |
| 6 | k6 or Locust + axe on the Playwright suite | k6, Playwright a11y |
| 7 | Pact or OpenAPI checks + Allure | Pact, OpenAPI learn, Allure |
| 8 | Capstone README: pyramid, gates, how to run locally/CI | your repo |

---

## Practice apps

- [The Internet (Heroku)](https://the-internet.herokuapp.com/) — classic UI playground
- [Restful Booker](https://restful-booker.herokuapp.com/) — API
- [JSONPlaceholder](https://jsonplaceholder.typicode.com/) — fake REST
- [Swagger Petstore](https://petstore.swagger.io/) — OpenAPI
- [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) — security + e2e (use legally, locally)

---

## Communities

- [Ministry of Testing](https://www.ministryoftesting.com/)
- [Test Automation University](https://testautomationu.applitools.com/)
- [Playwright Discord](https://aka.ms/playwright/discord) (linked from [playwright.dev](https://playwright.dev))
- [Stack Overflow](https://stackoverflow.com/questions/tagged/selenium) — tags: `selenium`, `playwright`, `pytest`, `rest-assured`

Prefer **one question after you have a failing test and a stack trace**, not “how do I become SDET.”

---

**Rule of thumb:** if a site is not in this list, use it only as a supplement. The systematic path is **Handbook/docs → TAU if you want video → your repo → CI**. That combination is what reads as SDET; a folder of unfinished courses does not.

Do not try to become a 10/10 in all three languages at once. **Java depth + TS Playwright fluency + Python pytest fluency** is the marketable combination from a Java Selenium starting point.
