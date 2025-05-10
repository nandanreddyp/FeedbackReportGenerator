# Feedback Report Generator

A reporting service that processes student event data to generate an HTML and PDF report asynchronously, stores the reports in a database, and provides endpoints to retrieve the report or check the task status.

## **App Structure Overview**

* `report_generator` manages the global settings and routing.
* `apis` handles the API communication for generating and retrieving reports.
* `reports` manages the report generation logic and storage.
* `tasks` processes the report generation asynchronously using Celery.

report_generator/
    ├── apis/ # for api calls
    ├── tasks/ # for celery tasks
    ├── reports/ # for creating and storing reports
    └── report_generator/ # main project settings
        └── settings.py

# Setup

### Setup virtual environment

```bash
pipx install poetry==2.1.3
poetry install
```

### Create database and user

```
-- Open PostgreSQL shell:
sudo -u postgres psql

-- Create database
CREATE DATABASE reports_db;

-- Create user
CREATE USER developer WITH PASSWORD 'helloworld';

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE reports_db TO developer;
\c reports_db
GRANT ALL PRIVILEGES ON SCHEMA public TO developer;

-- Exit PostgreSQL shell
\q
```

### Migrate database

```
python manage.py makemigrations
python manage.py migrate
```

### Run Redis and celery

```
-- Install redis
sudo apt install redis

-- Start redis
redis-server

-- Check if running
redis-cli ping # should return PONG

-- Turn on celery
celery -A tasks worker --loglevel=info
-- Turn on flower
celery -A tasks flower
```
