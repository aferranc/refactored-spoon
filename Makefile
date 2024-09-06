# Variables
SHELL := /bin/bash
VERSION := 1.7.0
BUILD_DIR := $(CURDIR)/build
VENV_DIR := $(CURDIR)/.venv

.PHONY: help all clean install update run release
.DEFAULT_GOAL: help

help: ## Show this help message.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

clean: ## Remove extraneous compiled files, caches, logs, etc.
	@echo "+ Remove extraneous compiled files, caches, logs, etc."
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info
	@find . -name '*.pyc' -exec rm -rf {} +
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type d -name '.pytest_cache' -exec rm -rf {} +
	@find . -type f -name '*.py[co]' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@rm -rf $(BUILD_DIR)/

env:
	@echo "+ Creating local virtualenv"
	@poetry env use python3.10
	@. $(VENV_DIR)/bin/activate

install: env ## Install dependencies.
	@echo "+ Installing dependencies"
	@poetry install

update: env ## Update dependencies via poetry.
	@echo "+ Updating dependencies"
	@poetry update

run: env ## Launch app.
	@echo "+ Launching app"
	@FLASK_APP=refactored_spoon/app.py FLASK_DEBUG=true flask run

release: ## Bump release version (patch|minor|major).
	@cz bump --yes
