# app
run:
	PYTHONPATH=. poetry run uvicorn app.app:app --reload --port 8000