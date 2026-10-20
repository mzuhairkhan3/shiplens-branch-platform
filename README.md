# ShipLens Challenge #01
## Branch-to-Head-Office Management Platform

Production-grade web platform that connects volunteer branches to head office and runs the organisation's public website.

**Live URL:** (coming soon – will be deployed on Render)  
**Stack:** Django 5 + PostgreSQL + Docker + GitHub Actions  
**Languages:** English + Urdu (RTL)

---

### Quick Start (Local)

```bash
# 1. Clone
git clone https://github.com/mzuhairkhan3/shiplens-branch-platform.git
cd shiplens-branch-platform

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Copy environment file
cp .env.example .env
# Edit .env if needed

# 5. Start Postgres (easiest with Docker)
docker compose up -d db

# 6. Run migrations (after we create models)
python manage.py migrate

# 7. Create superuser (later)
python manage.py createsuperuser

# 8. Run the server
python manage.py runserver
```

Health check: http://localhost:8000/health/

---

### Required Environment Variables

See `.env.example`

---

### Project Structure (will grow)

```
├── apps/
│   └── core/          # Health + shared utilities
├── config/            # Django settings & URLs
├── docs/              # ADRs, permissions table, handover
├── templates/         # Public website templates
├── locale/            # English & Urdu translations
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

### Test Logins (will be added later)

One test account per role will be listed here once created.

---

### AI Usage

See `AI-USAGE.md` (to be created).

---

Built for ShipLens by EchoLens Digital – Challenge #01
