from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.config import settings

app = FastAPI(title=settings.APP_NAME, version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
async def root():
    return {"app": settings.APP_NAME, "status": "ok", "environment": settings.APP_ENV}


@app.get("/health")
async def healthcheck():
    return {"status": "healthy", "service": settings.APP_NAME}
