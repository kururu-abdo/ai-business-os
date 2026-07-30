# Architecture Documentation

## Tech Stack
* **Framework:** FastAPI (Asynchronous execution)
* **Database:** PostgreSQL 16
* **ORM:** SQLAlchemy 2.0 (Async extension)
* **Migrations:** Alembic
* **Logging:** Structlog (Structured JSON production formatting)

## Component Communication
1. Client issues requests to FastAPI container (Port 8000).
2. FastAPI processes routes asynchronously.
3. Database persistence layer maps queries natively via `asyncpg` drivers.
