# sdet-lab

Hands-on repo for the 8-week plan in [`sdet.md`](../sdet.md). Study daily; every topic should land as a commit here.

| Folder | Plan week | Stack |
|---|---|---|
| `java-api/` | 1–2 | JUnit 5 + REST Assured vs JSONPlaceholder |
| `python-api/` | 5 | pytest + httpx vs the same API |
| `playwright-ts/` | 3–4 | Scaffold only until you start Playwright |

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

**Playwright (week 3)**

Follow `playwright-ts/README.md`.
