.DEFAULT_GOAL := help

HOST ?= 127.0.0.1
PORT ?= 8000

run: ## Run app
	uvicorn main:app --host $(HOST) --port $(PORT) --reload --env-file .prod.env

install: ## Install new package (LIBRARY=...)
	@echo "Installing dependency $(LIBRARY)"
	poetry add $(LIBRARY)

uninstall: ## Remove package (LIBRARY=...)
	@echo "Uninstalling dependency $(LIBRARY)"
	poetry remove $(LIBRARY)

migrate-create: ## Create migration file
	alembic revision --autogenerate -m "$(MIGRATION)"

migrate-apply: ## Apply migrations
	alembic upgrade head

update: ## Update package (LIBRARY=...)
	@echo "Updating dependency $(LIBRARY)"
	poetry update $(LIBRARY)

help: ## Show this message
	@python -c "import re; \
targets = []; \
[targets.append((t,d)) for l in open('Makefile', encoding='utf-8') \
 if (m:=re.match(r'^([a-zA-Z_-]+):.*## (.*)', l)) for t,d in [m.groups()]]; \
print('Usage: make [command]\\n'); \
print('Commands:'); \
[print(f'  {t:<12} {d}') for t,d in sorted(targets)]"





