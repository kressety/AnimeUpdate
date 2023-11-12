from re import search
from logging import getLogger

from feedparser import parse
from utils.trad2simp import trad2simp

# Initialize the logger
logger = getLogger(__name__)


def get_animes():
    logger.info('Fetching anime list from feed')
    animes_list = []
    try:
        feed = parse('https://api.ani.rip/ani-download.xml')
        for entry in feed.entries:
            match = search(r'\[ANi] (.+?) - (\d+) \[.*?]', entry.title)
            if match:
                show_name = match.group(1)
                episode_number = match.group(2)
                anime = {
                    'name': trad2simp(show_name.strip()),
                    'number': episode_number.strip(),
                    'link': entry.link
                }
                animes_list.append(anime)
                logger.info(f"Found anime: {anime['name']} Episode: {anime['number']}")
        logger.info('Anime list fetching complete')
    except Exception as e:
        logger.error(f'Error while fetching anime list: {e}')

    return animes_list
