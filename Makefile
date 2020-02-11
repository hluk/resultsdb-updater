# Use podman-compose by default if available.
ifeq (, $(shell which podman-compose))
    COMPOSE := docker-compose
    PODMAN := docker
else
    COMPOSE := podman-compose
    PODMAN := podman
endif

SERVICE := dev

.PHONY: up down exec

up:
	$(COMPOSE) up -d

down:
	$(COMPOSE) down

# Executes $CMD in dev container.
exec:
	$(PODMAN) exec resultsdb-updater_$(SERVICE)_1 bash -c '$(CMD)'

test:
	$(MAKE) exec CMD="python3 /scripts/publish.py ${ARGS}"
