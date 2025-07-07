.PHONY: dev migrations migrate upgrade downgrade history current heads show

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

