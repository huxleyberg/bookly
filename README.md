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

## 📘 Learning Outcomes from *FastAPI Beyond CRUD*

This project covers:

- ✅ SQLModel & async engines
- ✅ Path/query/body handling
- ✅ Settings management via Pydantic
- ✅ Auth with JWTs & OAuth2
- ✅ Middleware & exception design
- ✅ Background tasks with Celery
- ✅ Full test coverage: unit, integration, property-based
- ✅ Production deployment strategy


