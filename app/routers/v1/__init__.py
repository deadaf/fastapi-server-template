import fastapi

router = fastapi.APIRouter()


@router.get("/")
async def index():
    return {"message": "Hello, world!"}
