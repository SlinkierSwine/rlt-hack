# rlt-hack
## How to start backend
1. Create db (Postgres)
2. Clone repo
3. cd to project folder
4. `python -m venv venv`
5. `pip install - requirements.txt`
6. Activate venv
7. Create `.env` file and fill it like in `.example.env`
8. `alembic update head`
9. `uvicorn backend.main:app`
10. Go to `http://localhost:8000`
