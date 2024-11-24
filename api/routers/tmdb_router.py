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
async def search_movie(
    search: str, of_type: TypeParams = TypeParams.movie, year: int | None = None
):
    """
    ## Searches for movies with a query string

    :param search: Movie title to search for.
    :param type: specifies the type of result to return, whether to return a **series**, **movie** or an **episode**
    :param year: the year of release
    """

    search_result = await api.search(search, of_type=of_type, year=year)
    # if of_type:
    #     search_result = await api.search(search, of_type=of_type)

    # if year:
    #     search_result = await api.search(search, year=year)

    return search_result
