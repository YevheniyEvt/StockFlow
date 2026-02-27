DEV_FILE=docker-compose-dev.yml
PROD_FILE=docker-compose-prod.yml

.PHONY: dev prod dev-down prod-down rebuild-dev rebuild-prod logs-dev logs-prod

dev:
	docker compose -f $(DEV_FILE) up --build

prod:
	docker compose -f $(PROD_FILE) up -d --build

dev-down:
	docker compose -f $(DEV_FILE) down

prod-down:
	docker compose -f $(PROD_FILE) down

rebuild-dev:
	docker compose -f $(DEV_FILE) down
	docker compose -f $(DEV_FILE) up --build

rebuild-prod:
	docker compose -f $(PROD_FILE) down
	docker compose -f $(PROD_FILE) up -d --build

logs-dev:
	docker compose -f $(DEV_FILE) logs -f

logs-prod:
	docker compose -f $(PROD_FILE) logs -f