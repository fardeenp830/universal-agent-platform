# Universal Agent Platform

A cloud-ready multi-agent AI platform for autonomous execution, coding, GitHub automation, research, and task orchestration.

## Features

- Multi-agent architecture with specialized agents
- Cloud-native task execution via Celery + Redis
- FastAPI API for orchestration and scheduling
- GitHub automation tools
- Coding/debugging workflows
- Research and analysis workflows
- Scheduled jobs and background processing
- Environment-based configuration for local/cloud deployment

## Architecture

- `app/agents/`: specialized agents
- `app/core/`: orchestration and base agent classes
- `app/services/`: LLM, scheduler, and shared services
- `app/tools/`: external integrations (GitHub, web, etc.)
- `app/workers/`: asynchronous Celery tasks
- `app/main.py`: FastAPI app entrypoint

## Quick Start

### 1. Clone and install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure environment

Copy the example environment file and set your secrets:

```bash
cp .env.example .env
```

### 3. Start Redis (required for background jobs)

```bash
docker run -d --name universal-agent-redis -p 6379:6379 redis:7
```

### 4. Run the API server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 5. Start Celery worker (in another terminal)

```bash
celery -A app.workers.tasks worker --loglevel=info
```

### 6. Example API calls

```bash
curl http://localhost:8000/health
curl -X POST http://localhost:8000/orchestrate \
  -H "Content-Type: application/json" \
  -d '{"task":"Debug a Python function that is failing with a TypeError"}'
```

## Included Agents

- `CodingAgent`: bug fixing, code generation, improvements
- `ResearchAgent`: analysis, synthesis, and structured summaries
- `GitHubAgent`: repo-level task analysis, PR/issue support
- `ChatAgent`: conversational general assistant
- `FinanceAgent`: market and business analysis

## Deployment

This project is container-friendly and designed to run in cloud environments with:

- Docker
- Redis
- Celery workers
- managed LLM API access
- GitHub API token

## Example scheduled jobs

You can schedule jobs via the API or by adding tasks in the worker layer.

## Important Notes

- Without keys for OpenAI/Anthropic, the app will operate in a safe fallback mode with structured responses.
- Set `GITHUB_TOKEN` if you want GitHub automation features enabled.

## License

MIT
