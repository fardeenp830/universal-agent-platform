# Universal Agent Platform

A cloud-ready multi-agent AI platform for autonomous work, coding, research, GitHub tasks, infrastructure automation, and scheduled execution.

## Included capabilities

- Multi-agent orchestration and routing
- Agent memory with lightweight vector-style recall
- Task history and execution persistence
- FastAPI HTTP API
- Celery + Redis worker queue
- Docker and cloud deployment support
- LLM integration support for OpenAI and Anthropic
- Domain agents for code, research, GitHub, finance, math, science, robotics, quantum, biotech, film, and DevOps

## Quick start

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

Run the API:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Run the background worker:

```bash
celery -A app.workers.tasks worker --loglevel=info
```

Health check:

```bash
curl http://localhost:8000/health
```

Task orchestration example:

```bash
curl -X POST http://localhost:8000/api/orchestrate \
  -H "Content-Type: application/json" \
  -d '{"task":"debug a Python TypeError in a Flask app","user_id":"demo-user"}'
```

Memory example:

```bash
curl -X POST http://localhost:8000/api/memory \
  -H "Content-Type: application/json" \
  -d '{"content":"AI agents benefit from memory, tool use, and verification loops."}'
```

## Deployment

This repo is configured for cloud deployment and containerized execution.

### Docker

```bash
docker-compose up --build
```

### Render

Use the included `render.yaml` file to deploy to Render.

### Heroku / Railway / similar PaaS

Use the included `Procfile` with the app start command.

## Environment variables

Example values are in `.env.example`.

Required for full LLM features:

- `OPENAI_API_KEY`
- `ANTHROPIC_API_KEY`

Optional:

- `REDIS_URL`
- `GITHUB_TOKEN`
- `GITHUB_OWNER`
- `GITHUB_REPO`

## Notes

- Without provider keys, the app runs in offline fallback mode.
- Redis is required for scheduled jobs and background execution.
- The memory layer is lightweight and intentionally portable for local or cloud use.
