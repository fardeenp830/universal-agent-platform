services:
  - type: web
    name: universal-agent-platform
    env: python
    plan: free
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn app.main:app --host 0.0.0.0 --port 10000
    envVars:
      - key: APP_NAME
        value: Universal Agent Platform
      - key: APP_ENV
        value: production
      - key: PORT
        value: 10000
      - key: REDIS_URL
        sync: false
