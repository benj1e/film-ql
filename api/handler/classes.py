from ..errors.api_exception import InvalidMethodType
from api.logger import get_logger
from pprint import pprint
from urllib.parse import quote_plus
from dotenv import load_dotenv, find_dotenv
import aiohttp, os

load_dotenv(find_dotenv())
logger = get_logger("TMDBApi", "omdb-api.log")


class TMDBApi:
    def __init__(
        self, api_key: str | None = None, session: aiohttp.ClientSession = None
    ):
        # Allow passing an API key or fallback to environment variable
        self.api_key = api_key or os.getenv("API_KEY")
        if not self.api_key:
            raise ValueError("No API key found")

        self.session = session

    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, value):
        if not value:
            raise ValueError("API key cannot be None")
        self._api_key = value

    async def init_session(self):
        """Initialises an aiohttp session"""
        logger.info("Initialising session")
        self.session = aiohttp.ClientSession()

    async def close_session(self):
        """Closes an aiohttp session."""
        logger.info("Closing session")
        await self.session.close()

    async def get_session(self):
        async with aiohttp.ClientSession() as session:
            return session

    async def get(self, search_query: str | int = None) -> list:
        """This method makes a **GET** request to the TMDB API with a search parameter"""
        if isinstance(search_query, str) and search_query:
            # Adds '+' in between empty spaces
            search_query = quote_plus(str(search_query))

        # Use TMDB API URL, assuming `t` is the movie title
        url = f"http://www.omdbapi.com/?t={search_query}&apikey={self.api_key}"

        async with self.session.get(url) as response:
            return [await response.json()]
