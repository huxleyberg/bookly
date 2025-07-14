.PHONY: dev migrations migrate upgrade downgrade history current heads show freeze env-example celery flower up down rebuild logs-celery test

# Run development server
dev:
	fastapi dev src/

# Create a new migration (requires MIGRATION_MSG)
migrations:
	@if [ -z "$(m)" ]; then \
		echo "⚠️  Usage: make migrations m='your message'"; \
	else \
		alembic revision --autogenerate -m "$(m)"; \
	fi

# Apply latest migration
migrate:
	alembic upgrade head

# Upgrade to specific version (use: make upgrade REV=revision_id)
upgrade:
	@if [ -z "$(REV)" ]; then \
		echo "⚠️  Usage: make upgrade REV=revision_id"; \
	else \
		alembic upgrade $(REV); \
	fi

# Downgrade to previous migration (or specific one: make downgrade REV=xxxx)
downgrade:
	@if [ -z "$(REV)" ]; then \
		alembic downgrade -1; \
	else \
		alembic downgrade $(REV); \
	fi

# Show migration history
history:
	alembic history --verbose

# Show current database revision
current:
	alembic current

# Show unapplied heads
heads:
	alembic heads

# Show full migration script for a given revision
show:
	@if [ -z "$(REV)" ]; then \
		echo "⚠️  Usage: make show REV=revision_id"; \
	else \
		alembic show $(REV); \
	fi

# Freeze current environment packages into requirements.txt
freeze:
	pip freeze > requirements.txt

# Generate .env.example from .env (remove values)
env-example:
	@echo "Generating .env.example..."
	@cat .env | grep -v '^#' | sed 's/=.*$$/=/' > .env.example

# Start Docker Compose environment
up:
	docker-compose up --build

# Stop Docker Compose services
down:
	docker-compose down

# Rebuild and recreate containers
rebuild:
	docker-compose up --build --force-recreate

# Start Celery worker
celery:
	docker-compose run --rm celery

# Start Flower monitoring dashboard
flower:
	docker-compose run --rm \
		-p 5555:5555 \
		celery \
		celery -A src.celery_tasks.c_app flower --port=5555

# View Celery logs
logs-celery:
	docker-compose logs -f celery

# Run tests using pytest
test:
	pytest --tb=short -q
