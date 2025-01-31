import tomllib

import fastapi
from tortoise.contrib.fastapi import register_tortoise

from app.config import ENVIRONMENT, TORTOISE_ORM


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

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,
    add_exception_handlers=True if ENVIRONMENT == "dev" else False,
)
