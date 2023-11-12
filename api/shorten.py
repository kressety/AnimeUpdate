from urllib.parse import urljoin
from logging import getLogger
from requests import post

BASE_URL = 'https://mealuet.com'

# Initialize the logger
logger = getLogger(__name__)


def shorten(url: str):
    try:
        logger.info(f"Attempting to shorten URL: {url}")
        response = post(
            url=BASE_URL,
            json={
                'url': url
            }
        )
        if response.status_code == 200:
            shortened_url = urljoin(BASE_URL, response.json()['key'])
            logger.info(f"URL shortened successfully: {shortened_url}")
            return shortened_url
        else:
            logger.error(f"Failed to shorten URL. Status code: {response.status_code}")
            return False
    except Exception as e:
        logger.error(f"Exception occurred while shortening URL: {e}")
        return False
