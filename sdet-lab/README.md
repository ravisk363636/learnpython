# sdet-lab

Hands-on repo for the 12-week (3-month) plan in [`sdet.md`](../sdet.md). Study daily; every topic should land as a commit here.

| Folder | Plan weeks | Stack |
|---|---|---|
| `java-api/` | 1–4 | JUnit 5 + REST Assured vs JSONPlaceholder |
| `playwright-ts/` | 5–7 | TypeScript Playwright (init in week 5) |
| `python-api/` | 8 | pytest + httpx vs the same API |

CI: [`.github/workflows/sdet-lab.yml`](../.github/workflows/sdet-lab.yml) runs Java and Python on each push.

## Run locally

**Java**

```bash
cd java-api
./mvnw test
```

If the wrapper is missing, use Maven 3.9+ and `mvn test`.

**Python**

```bash
cd python-api
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

**Playwright (week 5)**

Follow `playwright-ts/README.md`.
