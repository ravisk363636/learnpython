.PHONY: install lint test test-smoke test-parallel reports clean

PYTHON ?= python3

install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -e ".[dev]"

lint:
	ruff check src tests
	ruff format --check src tests

format:
	ruff format src tests

test:
	$(PYTHON) -m pytest tests --alluredir=reports/allure-results

test-smoke:
	$(PYTHON) -m pytest tests -m smoke --alluredir=reports/allure-results

test-parallel:
	$(PYTHON) -m pytest tests -n auto --reruns 1 --alluredir=reports/allure-results

reports:
	$(PYTHON) -m pytest tests --html=reports/report.html --self-contained-html --alluredir=reports/allure-results

clean:
	rm -rf reports screenshots logs .pytest_cache .ruff_cache src/*.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} +
