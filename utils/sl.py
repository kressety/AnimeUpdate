from os.path import exists
from pickle import load, dump
from logging import getLogger

# Initialize the logger
logger = getLogger(__name__)


def load_record():
    if exists('anime_record.pkl'):
        try:
            with open('anime_record.pkl', 'rb') as file:
                anime_record = load(file)
            logger.info('Anime record loaded successfully')
            return anime_record
        except Exception as e:
            logger.error(f'Error occurred while loading anime record: {e}')
            return {}
    else:
        logger.info('Anime record file does not exist, returning empty record')
        return {}


def save_record(obj):
    logger.info('Saving anime record')
    anime_record = load_record()
    for item in obj:
        anime_record_exists = anime_record.get(item['name'], [])
        if item['number'] not in anime_record_exists:
            anime_record_exists.append(item['number'])
            logger.info(f'Added new entry: {item["name"]} Episode {item["number"]}')
        anime_record[item['name']] = anime_record_exists
    try:
        with open('anime_record.pkl', 'wb') as file:
            dump(anime_record, file)
        logger.info('Anime record saved successfully')
    except Exception as e:
        logger.error(f'Error occurred while saving anime record: {e}')
