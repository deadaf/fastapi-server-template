import tomllib

import fastapi
from tortoise.contrib.fastapi import register_tortoise

from app.config import ENVIRONMENT, TORTOISE_ORM
from app.routers.v1 import router as v1_router


def get_metadata():
    with open("pyproject.toml", "rb") as f:
        pyproject = tomllib.load(f)
    return pyproject["tool"]["poetry"]


meta = get_metadata()

app = fastapi.FastAPI(
    title=meta["name"],
    description=meta["description"],
    version=meta["version"],
)

app.include_router(v1_router, prefix="/v1")

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,
    add_exception_handlers=True if ENVIRONMENT == "dev" else False,
)
