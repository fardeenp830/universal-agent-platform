version: "3.9"

services:
  app:
    build: .
    container_name: universal-agent-app
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - redis
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000

  redis:
    image: redis:7
    container_name: universal-agent-redis
    ports:
      - "6379:6379"

  worker:
    build: .
    container_name: universal-agent-worker
    env_file:
      - .env
    depends_on:
      - redis
    command: celery -A app.workers.tasks worker --loglevel=info
