DOCKER_COMPOSE = docker-compose.yml

.PHONY: start stop

start:
	docker compose -f $(DOCKER_COMPOSE) up

stop:
	docker compose -f $(DOCKER_COMPOSE) down


build:
	docker compose -f $(DOCKER_COMPOSE) build