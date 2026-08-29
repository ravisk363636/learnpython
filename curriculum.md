# Playwright Automation Mastery — Curriculum

**Course:** Playwright Automation Mastery with JavaScript / TypeScript + AI  
**Source syllabus:** [class.thetestingacademy.com/playwright-automation-mastery-course](https://class.thetestingacademy.com/playwright-automation-mastery-course)  
**Paid LMS (live recordings):** [courses.thetestingacademy.com/courses/playwright-automation-mastery](https://courses.thetestingacademy.com/courses/playwright-automation-mastery)

This file is a self-study map of the advertised 90-day syllabus. Paid videos are behind The Testing Academy LMS. Public GitHub labs, YouTube roadmaps, and official Playwright docs cover the same skills.

---

## Course snapshot

| Item | Detail |
|------|--------|
| Duration | 90 days (~75+ hours) |
| Next live batch (from landing page) | Starts 7 July 2026 |
| Schedule | Tue, Thu, Sat — 7:00–8:15 AM IST |
| Doubt sessions | Friday 8:00 PM IST, biweekly |
| Instructor | Pramod Dutta, The Testing Academy |
| Launch discount (advertised) | Code `PROMODE` (up to 10% off) |
| LMS price (listed) | ~15,000 INR |

**Included (paid program):** HD video lessons, source code, AI-integrated teaching, 5+ bonuses + Gen AI course, SDET club, n8n, Jenkins, GitHub, GitLab, job-board assistance.

---

## Official hubs

| What | Link |
|------|------|
| Landing / public syllabus | https://class.thetestingacademy.com/playwright-automation-mastery-course |
| Paid LMS | https://courses.thetestingacademy.com/courses/playwright-automation-mastery |
| Academy site | https://thetestingacademy.com |
| App / 90-day plan (mentioned on YouTube) | https://app.thetestingacademy.com |
| YouTube | https://youtube.com/@thetestingacademy |
| 90-day Playwright + MCP roadmap (free) | https://www.youtube.com/watch?v=r0GclERO0XE |
| Career roadmap video | https://www.youtube.com/watch?v=zXA1clEEyBc |
| Instructor LinkedIn | https://www.linkedin.com/in/pramoddutta/ |

### Instructor GitHub (practical labs)

- [PramodDutta/LearningPlaywrightBatch](https://github.com/PramodDutta/LearningPlaywrightBatch) — JS chapters 1–17, TS 18–22, Playwright fundamentals, CLI / AI agents / MCP lectures
- [PramodDutta/LearningPlaywrightTS](https://github.com/PramodDutta/LearningPlaywrightTS) — 90-day lab roadmap (JS → TS → PW → POM → BDD → Docker/Jenkins/GitHub Actions → AI/MCP)
- [PramodDutta/AdvancePlaywrightFramework1x](https://github.com/PramodDutta/AdvancePlaywrightFramework1x) — production-style TypeScript framework

```bash
git clone https://github.com/PramodDutta/LearningPlaywrightBatch.git
cd LearningPlaywrightBatch
npm install
npx playwright install
```

---

## 90-day syllabus + how to complete it

### Module 1 — JavaScript fundamentals (days 1–12)

Master core JavaScript for test automation: variables and types through promises and async.

| Day | Topic | Subtopics |
|-----|--------|-----------|
| 1 | Variables, data types & operators | `let`, `const`, `var`; primitive & reference types; operators & expressions |
| 2 | Practice — variables & types | Hands-on; type conversion; scoping |
| 3 | Conditionals & loops | If/else; switch; for & while |
| 4 | Practice — loops | Loop patterns; nested conditions; break & continue |
| 5 | Functions | Declarations; arrow functions; parameters |
| 6 | Practice — functions | Higher-order functions; return values; function scope |
| 7 | Arrays & callbacks | `map`, `filter`, `reduce`; callbacks; iteration |
| 8 | Practice — arrays | Complex operations; method chaining; callback patterns |
| 9 | Promises | Basics; `then` / `catch` / `finally`; chaining |
| 10 | Async / await | `async` & `await`; error handling; parallel promises |
| 11 | ES6 deep dive | Destructuring; spread; template literals |
| 12 | Final review | Exercises; code challenges; module assessment |

**Resources**

- Repo: `LearningPlaywrightBatch` chapters 1–15
- [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
- [javascript.info](https://javascript.info/)
- [freeCodeCamp JavaScript](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/)
- [Exercism JavaScript](https://exercism.org/tracks/javascript)

---

### Module 2 — Introduction to Playwright (days 13–22)

Setup, architecture, first tests, selectors/locators, basic actions.

| Day | Topic | Subtopics |
|-----|--------|-----------|
| 13 | Setting up a Playwright project | Installation; project structure; configuration |
| 14 | Project setup — practice | Test files; first runs; debug config |
| 15 | Playwright architecture | Browser contexts; page objects; test isolation |
| 16 | Architecture — deep dive | Multi-browser; headless; automation model |
| 17 | First test script | Test structure; assertions; organization |
| 18 | Test script best practices | Clean code; reusability; error handling |
| 19 | Selectors & locators — CSS | CSS selectors; identification; strategies |
| 20 | Selectors & locators — advanced | Role, text, and label selectors |
| 21 | Basic actions — clicking & typing | Click; fill; keyboard |
| 22 | Basic actions — practice | Forms; buttons; navigation |

**Resources**

- [Installation](https://playwright.dev/docs/intro)
- [Writing tests](https://playwright.dev/docs/writing-tests)
- [Locators](https://playwright.dev/docs/locators)
- [Actions / input](https://playwright.dev/docs/input)

**Practice sites**

- [playwright.dev](https://playwright.dev)
- [the-internet.herokuapp.com](https://the-internet.herokuapp.com/)
- [demoqa.com](https://demoqa.com/)
- [saucedemo.com](https://www.saucedemo.com/)

---

### Module 3 — TypeScript fundamentals (days 23–32)

Type safety and tooling for automation code.

| Day | Topic | Subtopics |
|-----|--------|-----------|
| 23 | Introduction to TypeScript | Why TS; benefits for testing; vs JavaScript |
| 24 | TypeScript fundamentals | Syntax; compilation; `tsconfig.json` |
| 25 | Installation & configuration | Setup; IDE; compiler options |
| 26 | TypeScript project setup | Structure; build tools; modules |
| 27 | Types and type inference | Annotations; inference; union types |
| 28 | Advanced types | Intersection; type guards; conditional types |
| 29 | Type annotations in functions | Parameter / return / optional types |
| 30 | Function types — advanced | Overloads; generics; rest parameters |
| 31 | Enums & array type annotations | Enums; array types; tuples |
| 32 | Type assertion & casting | Assertions; `as`; non-null assertion |

**Resources**

- Repo: Batch chapters 18–22
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- [Playwright TypeScript intro](https://playwright.dev/docs/intro#installing-playwright)

---

### Module 4 — Advanced Playwright (days 33–42)

Synchronization, assertions, alerts, frames, multi-page and multi-user contexts.

| Day | Topic | Subtopics |
|-----|--------|-----------|
| 33 | Synchronization & auto-waiting | Auto-wait; timeouts; wait strategies |
| 34 | Advanced synchronization | Custom waits; network idle; element states |
| 35 | Synchronization best practices | Avoiding brittle explicit waits; reliability |
| 36 | Assertions with expect | Basic, element, and text assertions |
| 37 | Advanced assertions | Custom matchers; soft assertions; snapshots |
| 38 | Assertion patterns | Best practices; error messages; organization |
| 39 | Handling alerts | Dialogs; confirm; prompt |
| 40 | Working with frames | Frame locators; switching; nested frames |
| 41 | Multi-page testing | Multiple pages; navigation; page events |
| 42 | Multi-user context | Browser contexts; isolated sessions; parallel |

**Resources**

- [Auto-waiting / actionability](https://playwright.dev/docs/actionability)
- [Assertions](https://playwright.dev/docs/test-assertions)
- [Dialogs](https://playwright.dev/docs/dialogs)
- [Frames](https://playwright.dev/docs/frames)
- [Browser contexts](https://playwright.dev/docs/browser-contexts)
- [Pages](https://playwright.dev/docs/pages)

---

### Module 5 — Playwright Test Runner (days 43–52)

Data, config, runner features, traces, codegen, inspector.

| Day | Topic | Subtopics |
|-----|--------|-----------|
| 43 | Reading data from `.env` | Env files; variables; secrets |
| 44 | JSON and CSV | Parsing; test data management |
| 45 | Test configuration — test level | Annotations; hooks; metadata |
| 46 | Test configuration — project level | `playwright.config.ts`; projects; globals |
| 47 | Test runner basics | Running; organization; filtering |
| 48 | Test runner — advanced | Grouping; dependencies; conditional tests |
| 49 | Filtering & retries | Selection; retry; flaky tests |
| 50 | Video recording | Video; screenshots; traces |
| 51 | Code generation | Codegen; generated tests; selector recording |
| 52 | Playwright Inspector | Debug mode; step-through; inspector |

**Resources**

- [Test configuration](https://playwright.dev/docs/test-configuration)
- [Annotations](https://playwright.dev/docs/test-annotations)
- [Retries](https://playwright.dev/docs/test-retries)
- [Trace viewer](https://playwright.dev/docs/trace-viewer)
- [Codegen](https://playwright.dev/docs/codegen)
- [Debugging](https://playwright.dev/docs/debug)
- [dotenv](https://github.com/motdotla/dotenv)

---

### Module 6 — API testing with Playwright (days 53–62)

Request context, REST methods, intercept and mock.

| Day | Topic | Subtopics |
|-----|--------|-----------|
| 53 | Introduction to API testing | Fundamentals; REST; strategy |
| 54 | Why API testing matters | Benefits; use cases; integration |
| 55 | API testing with Playwright | Request context; fixtures; setup |
| 56 | GET and POST | GET; POST; query parameters |
| 57 | PUT and DELETE | PUT; DELETE; PATCH |
| 58 | Advanced API methods | Headers; authentication; config |
| 59 | Handling API requests | Builders; serialization; errors |
| 60 | Handling API responses | Parsing; status codes; validation |
| 61 | Network interception — basics | Routes; modify requests; mock responses |
| 62 | Network interception — advanced | Complex scenarios; performance; error simulation |

**Resources**

- [API testing](https://playwright.dev/docs/api-testing)
- [Network mocking](https://playwright.dev/docs/mock)
- [Network](https://playwright.dev/docs/network)

**Practice APIs**

- [reqres.in](https://reqres.in/)
- [jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com/)
- [restful-booker.herokuapp.com](https://restful-booker.herokuapp.com/)

---

### Module 7 — OOPs, TypeScript & POM (days 63–74)

Classes, inheritance, Page Object Model, clean code.

| Day | Topic | Subtopics |
|-----|--------|-----------|
| 63 | Classes in TypeScript | Syntax; constructors; members |
| 64 | Constructors & access modifiers | Parameters; public / private / protected; readonly |
| 65 | Advanced class features | Static; getters/setters; abstract classes |
| 66 | Inheritance | `extends`; `super`; overriding |
| 67 | Polymorphism | Methods; interfaces; types |
| 68 | Encapsulation | Data hiding; access control |
| 69 | Introduction to POM | Concept; benefits; structure |
| 70 | POM design patterns | Page classes; locators; actions |
| 71 | Refactoring with POM — part 1 | Refactor tests; organization |
| 72 | Refactoring with POM — part 2 | Advanced patterns; reusable components |
| 73 | Base pages & common actions | Base classes; shared methods |
| 74 | Clean code best practices | Naming; quality; documentation |

**Resources**

- [Page Object Model](https://playwright.dev/docs/pom)
- [Fixtures](https://playwright.dev/docs/test-fixtures)
- [Best practices](https://playwright.dev/docs/best-practices)
- LMS also covers data-driven tests with [Faker](https://fakerjs.dev/)

---

### Module 8 — Automation framework & CI/CD (days 75–88)

Framework design, GitHub, GitHub Actions, Jira, device/geo/visual testing, reporters. LMS also covers Jenkins.

| Day | Topic | Subtopics |
|-----|--------|-----------|
| 75 | Framework architecture | Design principles; components; scalability |
| 76 | Test runner in the framework | Execution; suites; parallel |
| 77 | Framework best practices | Organization; maintainability; docs |
| 78 | GitHub integration | Git basics; repo; version control |
| 79 | GitHub Actions — setup | Workflows; actions; triggers |
| 80 | GitHub Actions — CI/CD pipeline | Automated tests; CI |
| 81 | Jira integration — setup | Jira API; issues; test management |
| 82 | Jira integration — reporting | Results; defects; status |
| 83 | Device emulation | Mobile; responsive; device profiles |
| 84 | Geo-location & console logs | Location; console; debug |
| 85 | Visual testing | Screenshots; visual regression |
| 86 | Custom reporters | Generation; formats; integration |
| 87 | Framework review | Review; optimization; performance |
| 88 | Framework optimization | Speed; resources; practices |

**Resources**

- Framework repo: [AdvancePlaywrightFramework1x](https://github.com/PramodDutta/AdvancePlaywrightFramework1x)
- [CI intro (GitHub Actions)](https://playwright.dev/docs/ci-intro)
- [Emulation](https://playwright.dev/docs/emulation)
- [Visual comparisons](https://playwright.dev/docs/test-snapshots)
- [Reporters](https://playwright.dev/docs/test-reporters)
- [Pro Git book](https://git-scm.com/book/en/v2)
- [GitHub Actions docs](https://docs.github.com/en/actions)
- [Jenkins docs](https://www.jenkins.io/doc/)
- [GitLab CI](https://docs.gitlab.com/ee/ci/)

---

### Module 9 — Career development (days 89–90)

| Day | Topic | Subtopics |
|-----|--------|-----------|
| 89 | Resume & LinkedIn | Resume tips; profile; personal branding |
| 90 | Interview prep & course completion | Interview questions; technical discussion; career guidance |

**Resources**

- `Task_Interview_Coding_Questions` in [LearningPlaywrightBatch](https://github.com/PramodDutta/LearningPlaywrightBatch)
- [Playwright best practices](https://playwright.dev/docs/best-practices) (interview-relevant)

---

## AI extras advertised on the course

LMS titles include GenAI for testers, Claude Code + Ollama, Playwright MCP, Playwright CLI, Selenium → Playwright MCP, RAG, AI agents, Cucumber.

| Topic | Where to learn |
|-------|----------------|
| Playwright MCP | [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) · Batch folder `Lecture_Playwright_MCP` |
| Codegen / CLI | [CLI](https://playwright.dev/docs/test-cli) · Batch `Lecture_Playwright_CLI` |
| VS Code | [Playwright VS Code](https://playwright.dev/docs/getting-started-vscode) |
| Cucumber / BDD | LearningPlaywrightTS section 06 · [Cucumber docs](https://cucumber.io/docs/guides/) |
| n8n (bonus) | https://docs.n8n.io |

---

## LMS recording titles (paid course outline)

These titles appear on the LMS curriculum (dates from the 2026 batch). Use them as a checklist against GitHub labs and docs.

- GenAI for Software Tester (parts 1–2)
- Introduction class; AI classes (parts 1–3)
- Build a 24/7 AI tester (OpenClaw / VPS)
- JavaScript basics (multiple days); variables; operators; if/else; loops
- GitHub session 1; how to push code
- Building 3+ QA testing tools using Antigravity
- What is Playwright; Playwright architecture
- Arrays, functions, strings, objects, multi-dimensional arrays
- Playwright MCP Server master class
- Selenium MCP + Playwright AI agent
- JavaScript advanced topics; promises; async/await
- Playwright CLI master class
- Inheritance; TypeScript-only features; interface; generics
- Selenium to Playwright MCP migration (parts 1–2)
- Playwright introduction and fundamentals
- RAG tutorial
- Advance locator strategy and live projects
- Session state; multiple element filters on a real login UI
- Web tables; frames/windows/keyboard; mouse; JS alerts
- SVG & Shadow DOM; file upload/download; scroll
- Assertions; test modifiers (hooks); `expect()`
- Data-driven testing; POM; fixtures; Faker.js
- Advance Playwright framework (folder-by-folder, multiple sessions)
- Jenkins jobs (parts 1–2)
- Playwright API testing (parts 1–3); advance API framework + fixtures
- AI agents; Cucumber (two sessions)
- Claude 101 master class (part 1)
- Claude Code + Ollama (free-tagged days on LMS)

---

## Suggested weekly rhythm (self-study)

1. Watch the matching YouTube/LMS lesson, or read official docs if unpaid.
2. Run the matching GitHub chapter.
3. Automate one flow on Sauce Demo, the-internet, or DemoQA.
4. Push to GitHub every week (start Module 8 habits early).
5. From week 6, add API tests and one GitHub Actions workflow.

That path is: **JS → Playwright → TypeScript → advanced PW → runner → API → POM → CI/CD → AI**. Paid videos add live teaching, doubt sessions, SDET club, job board, and GenAI/n8n/Jenkins bonuses—not a different core curriculum.

---

## Copyright note

Course branding, live recordings, and paid LMS material belong to The Testing Academy. This file restates the **public syllabus** from their landing page and points to **public** docs and GitHub repos. It is not a dump of paid video content.
