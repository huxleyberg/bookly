# 📚 Bookly – FastAPI Project

Bookly is a fully asynchronous, production-ready API built using **FastAPI** and **SQLModel**. This project goes far beyond simple CRUD, showcasing how to build secure, scalable, and maintainable APIs with modern Python tooling.

---

## 🚀 Features

- ✅ RESTful API with FastAPI & SQLModel
- ⚡️ Asynchronous database operations
- 🔐 JWT Authentication & Role-Based Access Control (RBAC)
- 🧩 Modular architecture using Routers, Services, and Repositories
- 🧪 Testing with Pytest, Unittest Mock, and Schemathesis
- 🔄 Alembic for DB Migrations
- 📦 Dependency Injection with `Depends`
- 🛠️ Custom exception handlers & error responses
- 📬 Email verification & password reset with Celery + Redis
- 🪄 Real-time background tasks monitoring via Flower
- 📄 API Docs with Swagger UI and ReDoc
- ☁️ CI/CD via GitHub Actions
- 🌍 Deployment-ready (Render-compatible)

---

## 🧪 Local Development

### 1. Clone the repo

```bash
git clone https://github.com/huxleyberg/bookly.git
cd bookly
```

### 2. Set up environment

```bash
cp .env.example .env
# Edit `.env` to match your local DB config
```

### 3. Create and activate a virtualenv

```bash
python -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
make freeze
```

### 5. Run DB migrations

```bash
make migrate
```

### 6. Run development server

```bash
make dev
```

---

## 📜 Makefile Commands

```makefile
make dev              # Run FastAPI dev server
make migrations m="msg" # Generate migration
make migrate          # Apply latest migration
make test             # Run tests
make freeze           # Export requirements.txt
```

---

## 🧪 Running Tests

```bash
pytest
```

Or via Make:

```bash
make test
```

---

## ✅ CI/CD: GitHub Actions

- Runs tests on GitHub-hosted PostgreSQL service
- Runs secondary tests on external DB before deploy
- Alembic migrations are applied automatically
- Environment variables are managed via GitHub Secrets

---

## ☁️ Deployment

Bookly is ready to deploy to platforms like **Render**, **Railway**, or **Fly.io**.

Set your `DATABASE_URL`, `SECRET_KEY`, and other env variables in the hosting dashboard.

---

## 🔐 Generate a Secret Key

To generate a secure random secret key for use in environment variables like `SECRET_KEY`, run the following in your terminal using Python 3:

```bash
python3 -c "import secrets; print(secrets.token_hex(16))"

---

## 📁 `.env.example` Generation

You can generate a clean `.env.example` file (without secrets or values) based on your local `.env` file:

```bash
make env-example
