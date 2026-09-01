# Day-by-day links (docs + video + hands-on)

Open this file **every morning**. Rule: **docs first → watch only if stuck → code in `sdet-lab` the same day**. Do not binge a whole TAU course in one sitting unless the row says so.

**Plan:** [`sdet.md`](../sdet.md) (12 weeks). **Lab:** this folder.

**Video hubs (subscribe once):**

| Hub | URL |
|---|---|
| Test Automation University (free, enroll) | https://testautomationu.applitools.com/ |
| Playwright (Microsoft) | https://www.youtube.com/@Playwrightdev |
| Docker | https://www.youtube.com/@docker |
| GitHub | https://www.youtube.com/@GitHub |
| Grafana k6 | https://grafana.com/docs/k6/latest/ |

**Practice targets (reuse all 12 weeks):**

| Kind | URL |
|---|---|
| UI | https://the-internet.herokuapp.com/ |
| API | https://jsonplaceholder.typicode.com/ · https://restful-booker.herokuapp.com/ |
| OpenAPI | https://petstore.swagger.io/ |
| DSA | https://leetcode.com/explore/interview/card/top-interview-questions-easy/ · https://neetcode.io/practice |

If a TAU chapter is longer than 25 minutes, **pause, write the matching test, then resume**.

---

## Month 1 — Java + HTTP + CI

### Week 1 — JUnit 5 + pyramid

| Day | Docs (required) | Video / interactive | Hands-on in `sdet-lab` |
|---|---|---|---|
| Mon | [Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html) | TAU catalog: search “Introduction to Test Automation” **or** skip video | Run `java-api/./mvnw test`. Add 2 cases to `TextUtilsTest`. Commit. |
| Tue | [JUnit 5 User Guide — writing tests](https://junit.org/junit5/docs/current/user-guide/#writing-tests) | [Baeldung JUnit 5](https://www.baeldung.com/junit-5) (read + copy patterns, not copy-paste whole class) | New helper class + tests (list/map). |
| Wed | [JUnit 5 parameterized](https://junit.org/junit5/docs/current/user-guide/#writing-tests-parameterized-tests) | [Baeldung parameterized tests](https://www.baeldung.com/parameterized-tests-junit-5) | `@CsvSource` on `TextUtils`. |
| Thu | [AssertJ](https://assertj.github.io/doc/#assertj-core-quick-start) | — | Convert asserts to AssertJ. |
| Fri | [Mockito JUnit 5](https://www.baeldung.com/mockito-junit-5-extension) · [Mockito docs](https://site.mockito.org/) | — | Mock a tiny `Clock`/`Repo` dependency. |
| Sat | [dev.java/learn](https://dev.java/learn/) (streams/collections refresh) | TAU [Java Programming](https://testautomationu.applitools.com/java-programming/) ch. you still need | README: how to run `./mvnw test`. |
| Sun | Review your git log | [NeetCode arrays](https://neetcode.io/practice) Easy only | 5 Java Easy problems, talk aloud. |

**AI lab:** quiz from JUnit user guide; you type the tests.

### Week 2 — REST Assured + HTTP

| Day | Docs | Video / course | Hands-on |
|---|---|---|---|
| Mon | [MDN HTTP overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview) · [status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) | TAU [Exploring Service APIs](https://testautomationu.applitools.com/exploring-service-apis-through-test-automation/) ch. 1 | Open [JSONPlaceholder](https://jsonplaceholder.typicode.com/posts/1) in browser; add header asserts in `JsonPlaceholderApiTest`. |
| Tue | [REST Assured Usage wiki](https://github.com/rest-assured/rest-assured/wiki/Usage) | TAU [REST Assured](https://testautomationu.applitools.com/automating-your-api-tests-with-rest-assured/) ch. 1–2 | Given/when/then + `log().all()` on GET. |
| Wed | Same wiki: JSON path / body | TAU REST Assured ch. 2 (body) | Nested JSON + list size. |
| Thu | MDN [query string](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams) | TAU REST Assured ch. 3 (parameters) | Query + path params; 404 test. |
| Fri | REST Assured `RequestSpecification` (wiki “Specifications”) | TAU REST Assured ch. 4 | Base URI from env var. |
| Sat | [jsonplaceholder guide](https://jsonplaceholder.typicode.com/guide/) | Optional playlist [REST Assured Java](https://www.youtube.com/playlist?list=PLMer2TvhZIw-8KszaIZFsOrE8MEJXVYoY) **after** 8 green tests | POST/PUT extra cases. |
| Sun | [HTTP methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) | — | 5 interview Qs out loud + 5 Java Easy. |

**App:** https://jsonplaceholder.typicode.com/

### Week 3 — Auth, POJOs, OpenAPI, Booker

| Day | Docs | Video / course | Hands-on |
|---|---|---|---|
| Mon | [JWT introduction](https://jwt.io/introduction) | TAU Exploring APIs ch. 3.4 Security | Inspect a JWT on jwt.io (public demo tokens only). |
| Tue | [OAuth 2.0](https://www.oauth.com/oauth2-servers/accessing-data/authorization/) skim | TAU Exploring APIs ch. 2 Postman | Postman GET/POST [Restful Booker](https://restful-booker.herokuapp.com/apidoc/index.html) then **automate in Java**. |
| Wed | [Baeldung REST Assured object mapping](https://www.baeldung.com/rest-assured-tutorial) | TAU REST Assured ch. 6 serialization | POJO for a booking/post. |
| Thu | MDN [401/403](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401) | TAU Exploring APIs ch. 3.5 Errors | 400/401 tests on Booker. |
| Fri | [Learn OpenAPI](https://learn.openapis.org/) · [Swagger Petstore](https://petstore.swagger.io/) | TAU Exploring APIs ch. 4.1 first test | One test from an OpenAPI path. |
| Sat | [Restful Booker apidoc](https://restful-booker.herokuapp.com/apidoc/index.html) | TAU Exploring APIs ch. 4.2–4.4 Newman (ideas only; your CI is Maven) | Auth token → create booking. |
| Sun | [Spring Testing](https://docs.spring.io/spring-framework/reference/testing.html) optional | [Spring Guides](https://spring.io/guides) if JD is Spring | Design: test a login API (1 page). |

### Week 4 — Git, Docker, GitHub Actions

| Day | Docs | Video / interactive | Hands-on |
|---|---|---|---|
| Mon | [Pro Git ch. 2](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository) · [ch. 3](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell) | [Learn Git Branching](https://learngitbranching.js.org/) | Feature branch + PR hygiene on this repo. |
| Tue | [Docker Get Started](https://docs.docker.com/get-started/) | [Docker YouTube](https://www.youtube.com/@docker) “Get Started” / intro | `Dockerfile` in `java-api` that runs `mvn test`. |
| Wed | [GHA quickstart](https://docs.github.com/en/actions/writing-workflows/quickstart) · [setup-java](https://github.com/actions/setup-java) | TAU [GitHub Actions for Testing](https://testautomationu.applitools.com/github-actions-for-testing/) ch. 1 | Read `.github/workflows/sdet-lab.yml`; add a comment + improve a step. |
| Thu | [Understanding GitHub Actions](https://docs.github.com/en/actions/get-started/understand-github-actions) | TAU GHA ch. 2 · [GitHub Skills](https://skills.github.com/) Actions course | Maven cache + upload surefire artifact. |
| Fri | [Allure docs](https://allurereport.org/docs/) **or** keep JUnit XML | TAU GHA later chapters (pipeline) | Publish report artifact. |
| Sat | [Dockerfile reference](https://docs.docker.com/reference/dockerfile/) | Docker video: run your image locally | `docker build` + run tests in container. |
| Sun | Write quality gates in README | [GitHub official channel](https://www.youtube.com/@GitHub) search “Actions” | 5 Java coding Qs; Jenkins vs GHA paragraph. |

---

## Month 2 — TypeScript, Playwright, Python

### Week 5 — TypeScript, then Playwright init (Friday)

| Day | Docs | Video / interactive | Hands-on |
|---|---|---|---|
| Mon | [TS Handbook — Everyday Types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html) | [Total TypeScript tutorials](https://www.totaltypescript.com/tutorials) (one free) | `playwright-ts/` or a `ts-scratch/` file; `tsc --strict`. |
| Tue | [Narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html) | Same | Type a JSONPlaceholder `Post`. |
| Wed | [javascript.info Promises](https://javascript.info/promise-basics) · [async/await](https://javascript.info/async-await) | javascript.info tasks on those pages | Rewrite one callback to async/await. |
| Thu | [More on functions](https://www.typescriptlang.org/docs/handbook/2/functions.html) | Total TypeScript another short tutorial | Fix 5 intentional type errors. |
| Fri | [Playwright intro](https://playwright.dev/docs/intro) | TAU [Introduction to Playwright](https://testautomationu.applitools.com/playwright-intro/) ch. 1 · [Microsoft Learn Playwright](https://learn.microsoft.com/en-us/training/modules/build-with-playwright/) | `cd playwright-ts && npm init playwright@latest` — run generated tests. |
| Sat | [Installation](https://playwright.dev/docs/intro) | [Playwright YouTube](https://www.youtube.com/@Playwrightdev) first “getting started” video | VS Code Playwright extension; headed run. |
| Sun | Write 10 lines Selenium vs Playwright | [Selenium WebDriver with Java](https://testautomationu.applitools.com/selenium-webdriver-tutorial-java/) **refresh only** (you already know this) | 5 TS type puzzles. |

### Week 6 — Playwright core (code every day on the-internet)

| Day | Docs | Video | Hands-on |
|---|---|---|---|
| Mon | [Writing tests](https://playwright.dev/docs/writing-tests) | TAU Playwright intro ch. 2 · @Playwrightdev | Tests on https://the-internet.herokuapp.com/ `getByRole`. |
| Tue | [Locators](https://playwright.dev/docs/locators) · [Assertions](https://playwright.dev/docs/test-assertions) | TAU Playwright ch. 2–3 | Delete any `waitForTimeout`. |
| Wed | [Test configuration](https://playwright.dev/docs/test-configuration) · hooks in writing-tests | @Playwrightdev config video if needed | `beforeEach`; isolated context. |
| Thu | [Trace viewer](https://playwright.dev/docs/trace-viewer) · [UI mode](https://playwright.dev/docs/test-ui-mode) | @Playwrightdev trace video | Fail a test; open the trace. |
| Fri | [Best practices](https://playwright.dev/docs/best-practices) · [POM](https://playwright.dev/docs/pom) | TAU Playwright remaining chapters | POM for 2 pages (login + another). |
| Sat | [Codegen](https://playwright.dev/docs/codegen) | @Playwrightdev codegen | Record then **rewrite** locators to getByRole. |
| Sun | [Auth](https://playwright.dev/docs/auth) skim | — | 5 “explain this snippet” from your repo. |

### Week 7 — Playwright framework + CI

| Day | Docs | Video | Hands-on |
|---|---|---|---|
| Mon | [Fixtures](https://playwright.dev/docs/test-fixtures) | TAU Playwright / @Playwrightdev fixtures | `storageState` or API login then UI. |
| Tue | [API testing](https://playwright.dev/docs/api-testing) | @Playwrightdev API testing | Create via API, assert in UI (JSONPlaceholder or Booker). |
| Wed | [Mock APIs](https://playwright.dev/docs/mock) | @Playwrightdev network | Mock one route. |
| Thu | [Accessibility](https://playwright.dev/docs/accessibility-testing) · [WAI](https://www.w3.org/WAI/fundamentals/) | — | axe in one spec. |
| Fri | [CI](https://playwright.dev/docs/ci) · [CI intro](https://playwright.dev/docs/ci-intro) | TAU [GitHub Actions for Testing](https://testautomationu.applitools.com/github-actions-for-testing/) (Playwright job) | Copy official GHA; traces on failure. |
| Sat | [Sharding](https://playwright.dev/docs/test-sharding) | — | `@smoke` vs full job. |
| Sun | Architecture README | Design: checkout | Draw pyramid for your repo. |

### Week 8 — Python pytest + httpx

| Day | Docs | Video / course | Hands-on |
|---|---|---|---|
| Mon | [Python tutorial 3–5](https://docs.python.org/3/tutorial/introduction.html) | TAU [API Testing in Python](https://testautomationu.applitools.com/python-api-testing/) ch. 1 | `python-api` venv; `pytest` (starter already exists). |
| Tue | [Classes](https://docs.python.org/3/tutorial/classes.html) · [typing](https://docs.python.org/3/library/typing.html) | TAU Python API ch. 2 | Type a `Post` TypedDict/dataclass. |
| Wed | [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) · [parametrize](https://docs.pytest.org/en/stable/how-to/parametrize.html) | TAU Python API ch. 3 assertions | `conftest.py` + parametrize status codes. |
| Thu | [httpx Quickstart](https://www.python-httpx.org/quickstart/) | TAU Python API ch. 5 JSON | Booker GET/POST in httpx (same cases as Java). |
| Fri | [Pydantic](https://docs.pydantic.dev/latest/concepts/models/) | TAU Python API ch. 6 schema | Validate response with a model. |
| Sat | [pytest markers](https://docs.pytest.org/en/stable/how-to/mark.html) · [setup-python](https://github.com/actions/setup-python) | TAU Python API ch. 9 parallel (optional) | Confirm Python job in `sdet-lab.yml`. |
| Sun | Compare Java vs Python table in README | — | 5 Python list/dict drills. |

---

## Month 3 — Infra, quality, interviews

### Week 9 — Testcontainers, WireMock, SQL

| Day | Docs | Video / guide | Hands-on |
|---|---|---|---|
| Mon | [Testcontainers getting started](https://testcontainers.com/getting-started/) · [JUnit 5 quickstart](https://java.testcontainers.org/quickstart/junit_5_quickstart/) | [Docker Testcontainers JUnit 5 lifecycle](https://docs.docker.com/guides/testcontainers-java-lifecycle/) | Postgres **or** skip to WireMock. |
| Tue | [JUnit 5 integration](https://java.testcontainers.org/test_framework_integration/junit_5/) | Same Docker guide (singleton section) | Static vs instance `@Container`. |
| Wed | [WireMock JUnit](https://wiremock.org/docs/junit-jupiter/) · [getting started](https://wiremock.org/docs/quickstart/java-junit/) | WireMock docs examples | Stub JSON; REST Assured against localhost stub. |
| Thu | [Mode SQL](https://mode.com/sql-tutorial/) select/where | — | 20 minutes SQL exercises. |
| Fri | [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial-select.html) joins | — | Assert a row if you have Postgres container. |
| Sat | [Testcontainers Java](https://java.testcontainers.org/) | — | README: how to run infra tests. |
| Sun | SQL joins practice | Design payments service (draft) | 5 SQL interview Qs. |

### Week 10 — Contracts, reports, flakes

| Day | Docs | Video / course | Hands-on |
|---|---|---|---|
| Mon | [Pact docs](https://docs.pact.io/) · [Pact JVM](https://docs.pact.io/implementation_guides/jvm) | Pact “how pact works” on docs site | One consumer test **or** skip to OpenAPI. |
| Tue | [Schemathesis](https://schemathesis.readthedocs.io/) · [Learn OpenAPI](https://learn.openapis.org/) | — | One schema-based run vs Petstore or your spec. |
| Wed | [Allure](https://allurereport.org/docs/) | — | Allure on Java **or** Playwright HTML in README. |
| Thu | Write flake policy (your words) | Ministry of Testing search “flaky tests” https://www.ministryoftesting.com/ | Quarantine tag + owner. |
| Fri | Test data via API | — | Factory/Faker for users. |
| Sat | [Playwright Java intro](https://playwright.dev/java/docs/intro) optional | — | One Java Playwright smoke **or** rest. |
| Sun | Finish payments 1-pager | — | 5 system-design Qs. |

### Week 11 — Perf, security, OTel, Selenium

| Day | Docs | Video | Hands-on |
|---|---|---|---|
| Mon | [k6 first test](https://grafana.com/docs/k6/latest/get-started/write-your-first-test/) **or** [Locust quickstart](https://docs.locust.io/en/stable/quickstart.html) | Grafana k6 docs examples / k6 YouTube on grafana.com | 50 VUs vs JSONPlaceholder; record p95. |
| Tue | [OWASP Top 10](https://owasp.org/www-project-top-ten/) | — | Authz checklist vs Booker tests. |
| Wed | [Playwright a11y](https://playwright.dev/docs/accessibility-testing) | — | Fail CI on critical axe. |
| Thu | [OTel observability primer](https://opentelemetry.io/docs/concepts/observability-primer/) | — | README: how you’d attach a trace id. |
| Fri | [Selenium waits](https://www.selenium.dev/documentation/webdriver/waits/) · [Grid](https://www.selenium.dev/documentation/grid/) | TAU [Selenium WebDriver with Java](https://testautomationu.applitools.com/selenium-webdriver-tutorial-java/) **review** locators/waits only | 10 Selenium vs Playwright Qs written. |
| Sat | [Juice Shop](https://owasp.org/www-project-juice-shop/) **local only** | Juice Shop getting started on that page | List 3 findings; do not attack systems you do not own. Optional [AWS Skill Builder](https://skillbuilder.aws/). |
| Sun | Mock interview | Record yourself | 45 min coding + 30 min design. |

### Week 12 — Capstone + apply

| Day | Docs | Video | Hands-on |
|---|---|---|---|
| Mon | Your README + [Playwright CI](https://playwright.dev/docs/ci) recap | — | Green CI; 10-minute run instructions. |
| Tue | STAR method (search “STAR interview”) | Ministry of Testing career articles | 15 behavioral stories. |
| Wed | Re-read Fowler pyramid + your HTTP notes | — | 15 technical answers without notes. |
| Thu | [NeetCode](https://neetcode.io/practice) Medium × 2 | — | Talk while coding; 1 pytest fixture design. |
| Fri | Job descriptions (Java SDET + Playwright) | — | Apply 5–10 roles; paste GitHub link. |
| Sat | [Chat with your data](https://www.deeplearning.ai/short-courses/langchain-chat-with-your-data/) · [Playwright MCP](https://github.com/microsoft/playwright-mcp) · [MCP](https://modelcontextprotocol.io/) | HF [Agents course](https://huggingface.co/learn/agents-course) units you skipped | RAG over this repo; convert MCP exploration into tests. |
| Sun | Rest | Second mock interview | Keep applying. |

**AI extras (any Saturday):** [LangGraph agentic RAG](https://docs.langchain.com/oss/python/langgraph/agentic-rag) · [LangSmith RAG eval](https://docs.langchain.com/langsmith/evaluate-rag-tutorial) · [promptfoo](https://www.promptfoo.dev/docs/intro/) · [OpenAI evals](https://platform.openai.com/docs/guides/evals)

---

## If a link 404s

1. Use the **hub** (TAU catalog, playwright.dev search, docs.pytest.org search).
2. Prefer **official docs** over a random YouTube of the same title.
3. Still do the **hands-on** column; the lab is the source of truth.

## Daily 90-minute mode (if short on time)

Skip the video. Do **Docs + Hands-on** only. Catch the TAU chapter on Saturday.
