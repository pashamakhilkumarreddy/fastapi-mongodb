POETRY := poetry
PYTHON := $(POETRY) run python
UVICORN := $(POETRY) run uvicorn

APP_MODULE := app.main:app
HOST := 127.0.0.1
PORT := 8000

.DEFAULT_GOAL := install

.PHONY: install
install:
	@$(POETRY) install

.PHONY: run
run:
	poetry shell
	@$(UVICORN) $(APP_MODULE) --host $(HOST) --port $(PORT) --reload

.PHONY: setup
setup: requirements.txt
	poetry export -f requirements.txt --output requirements.txt

.PHONY: test
test:
	@$(POETRY) run pytest

.PHONY: lint
lint:
	@$(POETRY) run flake8 .
	@$(POETRY) run blue --check .

.PHONY: format
format:
	@$(POETRY) run blue .

.PHONY: check
check: lint test  

.PHONY: install-git-hooks
install-git-hooks:
	pre-commit install --hook-type pre-commit
	pre-commit install --hook-type commit-msg

.PHONY: clean
clean:
	@find . -type d -name '__pycache__' -exec rm -r {} +
	@find . -type f -name '*.pyc' -delete
	@rm -rf .mypy_cache
	@rm -rf .pytest_cache
