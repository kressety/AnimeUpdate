from time import sleep
from logging import getLogger, basicConfig, INFO

from api.alist import check_dir, download, check_download
from api.ani import get_animes
from api.qqbot import post_to_channel
from utils.sl import load_record, save_record

# Initialize the logger
basicConfig(level=INFO)
logger = getLogger(__name__)

if __name__ == '__main__':
    logger.info('Starting the process to fetch and post animes')
    animes = get_animes()
    animes_record = load_record()

    for anime in animes:
        anime_record_exists = animes_record.get(anime['name'])
        if (anime_record_exists is None) or (anime['number'] not in anime_record_exists):
            logger.info(f'Processing new anime: {anime["name"]} Episode: {anime["number"]}')
            check_dir(anime['name'])
            download(anime['name'], anime['link'])

    save_record(animes)
    logger.info('Waiting for 7200 seconds before checking download status')
    sleep(7200)

    for anime in animes:
        anime_record_exists = animes_record.get(anime['name'])
        if (anime_record_exists is None) or (anime['number'] not in anime_record_exists):
            result = check_download(anime['name'], anime['link'])
            if result:
                logger.info(f'Posting to channel: {anime["name"]} Episode: {anime["number"]}')
                post_to_channel(anime['name'], anime['number'], result)
            else:
                logger.warning(f'Download check failed for {anime["name"]} Episode: {anime["number"]}')

    logger.info('Process completed')
