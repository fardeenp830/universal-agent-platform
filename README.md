# Universal Agent Platform

A cloud-ready multi-agent platform for autonomous work, coding, research, GitHub tasks, AI workflows, and scheduled background execution.

## Features

- Multi-agent orchestration across many domains
- Coding/debugging agent
- Research and analysis agent
- GitHub automation agent
- Finance and strategy agent
- Math, science, robotics, quantum, biotech, film, and DevOps agents
- Memory and retrieval layer for contextual continuity
- Task persistence and execution history
- Celery + Redis background workers
- FastAPI deployment-ready API
- Docker and Render-friendly configuration

## Local run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Start Redis:

```bash
docker run -d --name universal-agent-redis -p 6379:6379 redis:7
```

Start API:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Start worker in another terminal:

```bash
celery -A app.workers.tasks worker --loglevel=info
```

Test:

```bash
curl http://localhost:8000/health
curl -X POST http://localhost:8000/api/orchestrate \
  -H "Content-Type: application/json" \
  -d '{"task":"debug a Python TypeError in a Flask app","user_id":"demo"}'
```

## Deployment

This repo is ready for Render deployment with:
- Web service for FastAPI
- Worker service for Celery
- Redis service for queueing

## Environment variables

Example values are in `.env.example`.

Required for live LLM features:
- OPENAI_API_KEY
- ANTHROPIC_API_KEY

Optional:
- REDIS_URL
- GITHUB_TOKEN
- GITHUB_OWNER
- GITHUB_REPO

## Notes

- If no LLM keys are configured, the app runs in fallback mode.
- Redis is required for scheduled work and background execution.
- The memory layer is lightweight and portable for local or hosted deployments.
