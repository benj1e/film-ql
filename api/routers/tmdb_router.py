from fastapi import APIRouter
from ..handler.classes import TMDBApi
from ..errors.api_exception import InvalidMethodType
from api.logger import get_logger
from contextlib import asynccontextmanager
from enum import Enum
from slugify import slugify


class TypeParams(str, Enum):
    movie = "movie"
    series = "series"
    episode = "episode"


api = TMDBApi()
logger = get_logger("TMDB_Router", "tmdb.log")


@asynccontextmanager
async def lifespan(app):
    await api.init_session()
    try:
        yield
    finally:
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
