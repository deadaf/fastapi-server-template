ENVIRONMENT = "dev"

TORTOISE_ORM = {
    "use_tz": True,
    "timezone": "UTC",
    "connections": {
        "main": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "database": "",
                "host": "",
                "password": "",
                "port": ...,
                "user": "",
            },
        },
    },
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],
            "default_connection": "main",
        },
    },
}
