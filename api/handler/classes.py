from ..errors.api_exception import InvalidMethodType
from api.logger import get_logger
from urllib.parse import quote_plus, urlencode, urlparse, parse_qs, urlunparse
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

    async def get(self, query: str = None) -> list:
        """This method gets only one movie from the API"""
        if isinstance(query, str) and query:
            # Adds '+' in between empty spaces
            query = quote_plus(str(query))

        # Use TMDB API URL, assuming `t` is the movie title
        url = f"http://www.omdbapi.com/?t={query}&apikey={self.api_key}"

        async with self.session.get(url) as response:
            return [await response.json()]

    async def search(
        self, query: str, of_type: str | None = None, year: str | None = None
    ):
        """This method searches for a query from the API"""

        query = quote_plus(str(query.lower()))

        url = f"http://www.omdbapi.com/?s={query}&apikey={self.api_key}"

        # Parse the url
        parsed_url = urlparse(url)

        # Update query params
        query_params = parse_qs(parsed_url.query)
        if of_type:
            query_params["type"] = of_type

        if year:
            query_params["y"] = year

        # Build updated url query string
        updated_query = urlencode(query_params, doseq=True)

        # Recontruct the URL with the new query string
        new_url = urlunparse(parsed_url._replace(query=updated_query))

        async with self.session.get(new_url) as response:
            return [await response.json()]
