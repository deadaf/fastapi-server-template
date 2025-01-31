import fastapi
from tortoise.contrib.fastapi import register_tortoise

from app.config import ENVIRONMENT, TORTOISE_ORM

app = fastapi.FastAPI()

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,
    add_exception_handlers=True if ENVIRONMENT == "dev" else False,
)
