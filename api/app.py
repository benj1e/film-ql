from fastapi import FastAPI, Request
import uvicorn
from .logger import get_logger
from .routers.tmdb_router import router
from .middleware import logging_middleware
from starlette.middleware.base import BaseHTTPMiddleware

logger = get_logger("App", "app.log")


async def lifespan(app):
    logger.info("Application started!")
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(BaseHTTPMiddleware, dispatch=logging_middleware)


@app.get("/", status_code=418)
async def index():
    return {"message": "Hello World"}


app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
