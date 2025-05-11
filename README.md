# **Feedback Report Generator**

A reporting service that processes student event data to generate an HTML and PDF report asynchronously, stores the reports in a database, and provides endpoints to retrieve the report or check the task status.

---

## **Docker Steps to Run the Project**

### 1. **Build and Start Docker Containers**

To build the containers and start all services in detached mode:

```bash
docker-compose up --build -d
```

### 2. **Start Containers Without Rebuilding (if no code changes or start again)**

If you haven't made any changes to the Docker configuration or code and just need to start the containers:

```bash
docker-compose up -d
```

### 3. **Check the Status of Containers**

To view the status of your running containers:

```bash
docker-compose ps
```

### 4. **Check Real-Time Logs of a Specific Service**

To follow logs from a specific service (e.g., `web` service):

```bash
docker-compose logs -f web
```

You can replace `web` with any service name (e.g., `celery`, `flower`, `redis`) to see their logs.

### 5. **Access the Shell of a Docker Container**

To enter the shell of the `web` container (for debugging, file inspection, etc.):

```bash
docker-compose exec web bash
```

You can replace `web` with any other container name if needed (e.g., `celery` or `flower`).

### 6. **Stop the Containers**

To stop and remove all the containers, networks, and volumes:

```bash
docker-compose down
```

---

## **Services Links to Open After Running**

* **Django (Web App)**: [localhost:8000](http://localhost:8000)
* **Flower (Asynchronous Tasks Monitor)**: [localhost:5555](http://localhost:5555)

---

## **App Structure Overview**

The application is structured as follows:

* **`report_generator/`** — Main Django project folder containing global settings and routing.

  * **`apis/`** — API layer that handles communication for generating and retrieving reports.
  * **`tasks/`** — Celery tasks for processing reports asynchronously.
  * **`reports/`** — Handles the logic for generating, storing, and managing reports.
  * **`report_generator/`** — Main project settings and configurations.

    * **`settings.py`** — Django settings file.

---

## **Setup Instructions**

### **1. Setup Virtual Environment**

If you don't have **Poetry** installed, you can install it using **pipx**:

```bash
pipx install poetry==2.1.3
```

Next, install the dependencies specified in the `pyproject.toml`:

```bash
poetry install
```

### **2. Create Database and User (PostgreSQL)**

#### Open the PostgreSQL shell:

```bash
sudo -u postgres psql
```

#### Create a new database and user:

```sql
-- Create database
CREATE DATABASE reports_db;

-- Create user
CREATE USER developer WITH PASSWORD 'helloworld';

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE reports_db TO developer;

-- Switch to the new database
\c reports_db

-- Grant privileges to schema
GRANT ALL PRIVILEGES ON SCHEMA public TO developer;

-- Exit PostgreSQL shell
\q
```

### **3. Migrate Database**

Run the Django migration commands:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## **Run Redis and Celery**

To run the asynchronous task processing with Redis and Celery, follow these steps:

### **1. Install Redis**

For local development, install Redis on your machine:

```bash
sudo apt install redis
```

### **2. Start Redis**

Start the Redis server:

```bash
redis-server
```

To check if Redis is running, use the following command:

```bash
redis-cli ping
```

This should return `PONG` if Redis is running successfully.

### **3. Start Celery**

Start the Celery worker to handle background tasks:

```bash
celery -A tasks worker --loglevel=info
```

### **4. Start Flower (Optional)**

Flower is a monitoring tool for Celery. You can start it to monitor your tasks:

```bash
celery -A tasks flower
```

Flower will be accessible at [localhost:5555](http://localhost:5555) for task monitoring.

---

## **Additional Notes:**

* You can **stop** Redis and Celery at any time using `Ctrl+C` or by stopping the Docker containers if you're using Docker to manage them.
* Make sure to have the Redis server running and accessible by the `web` and `celery` services in Docker or locally, depending on your setup.
* If you're using **Docker**, you don't need to manually start Redis or Celery; the `docker-compose.yml` file will manage the services for you.

---
