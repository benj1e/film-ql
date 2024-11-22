from fastapi import APIRouter
from ..handler.classes import TMDBApi
import aiohttp
from contextlib import asynccontextmanager
from enum import Enum
from slugify import slugify


class TypeParams(str, Enum):
    movie = "movie"
    series = "series"
    episode = "episode"


api = TMDBApi()


@asynccontextmanager
async def lifespan(app):
    print("Session opened")
    await api.init_session()
    try:
        yield
    finally:
        print("Session closed")
        await api.close_session()


router = APIRouter(prefix="/movies", lifespan=lifespan)


@router.get("/")
async def get_movie(q: int | str):
    """Gets a single movie with its details from the API"""

    movie = await api.get(q)
    return {"movie": movie}


@router.get("/search")
async def search_movie(search: str, type: TypeParams = TypeParams.movie):
    """
    ## Searches for movies with a query string

    **Attributes:**\n
    `search` -- Movie title to search for. (no default)\n
    `type` -- specifies the type of result to return, whether to return a **series**, **movie** or an **episode**\n
    `year` -- the year of release\n
    """
