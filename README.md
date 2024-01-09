### Run the server

make run

### conda activate environment

conda activate fintech_api_backend

### Run this if the environment variables cannot be recognized

poetry self add poetry-dotenv-plugin

### Create migration for alembic

poetry run alembic revision --autogenerate -m "First migration"

### Run migration

poetry run alembic upgrade head

### Load data into tables

poetry run python ./initial_data.py



