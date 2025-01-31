import logging
import os
import tomllib
from logging.handlers import RotatingFileHandler

import fastapi
from tortoise.contrib.fastapi import register_tortoise

from app.config import ENVIRONMENT, TORTOISE_ORM
from app.routers.v1 import router as v1_router


def get_metadata():
    with open("pyproject.toml", "rb") as f:
        pyproject = tomllib.load(f)
    return pyproject["tool"]["poetry"]


meta = get_metadata()

# Configure Logging
log_file = os.path.join("logs", f"{meta['name']}.log")
log_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# Rotating file handler (5MB per file, keep last 5 backups)
log_handler = RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024, backupCount=5)
log_handler.setFormatter(log_formatter)

# Root Logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

app = fastapi.FastAPI(
    title=meta["name"],
    description=meta["description"],
    version=meta["version"],
)


@app.middleware("http")
async def log_requests(request: fastapi.Request, call_next):
    """Middleware to log every incoming request"""
    response = await call_next(request)
    logger.info(f"{request.method} {request.url} - {response.status_code}")
    return response


@app.get("/log-test")
async def log_test():
    logger.info("Test log entry")
    return {"message": "Check logs!"}


app.include_router(v1_router, prefix="/v1")

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,
    add_exception_handlers=True if ENVIRONMENT == "dev" else False,
)
