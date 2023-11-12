from configparser import ConfigParser
from logging import getLogger
from os.path import join
from urllib.parse import urljoin, unquote, quote

from requests import post

from api.shorten import shorten

config = ConfigParser()
config.read('config.ini')
logger = getLogger(__name__)


def _authenticate():
    logger.info('Starting authentication process')
    response = post(
        url=urljoin(config['alist']['base_url'], '/api/auth/login'),
        json={
            'username': config['alist']['username'],
            'password': config['alist']['password']
        }
    )
    if response.status_code == 200:
        logger.info('Authentication successful')
        return response.json()['data']['token']
    else:
        logger.error('Authentication failed with status code: {}'.format(response.status_code))
        return False


def check_dir(name: str):
    logger.info('Checking directory: {}'.format(name))
    auth_token = _authenticate()
    if auth_token:
        response = post(
            url=urljoin(config['alist']['base_url'], '/api/fs/mkdir'),
            headers={
                'authorization': str(auth_token)
            },
            json={
                'path': join(config['alist']['root'], name)
            }
        )
        if response.status_code == 200:
            logger.info('Directory check successful')
            return True
        else:
            logger.error('Checking directory failed with status code: {}'.format(response.status_code))
            return False


def download(name: str, url: str):
    logger.info('Initiating download for URL: {}'.format(url))
    auth_token = _authenticate()
    if auth_token:
        response = post(
            url=urljoin(config['alist']['base_url'], '/api/fs/mkdir'),
            headers={
                'authorization': str(auth_token)
            },
            json={
                'urls': [
                    url
                ],
                'path': join(config['alist']['root'], name)
            }
        )
        if response.status_code == 200:
            logger.info('Download successful')
            return True
        else:
            logger.error('Downloading failed with status code: {}'.format(response.status_code))
            return False


def check_download(name: str, url: str):
    logger.info('Checking download for URL: {}'.format(url))
    auth_token = _authenticate()
    if auth_token:
        file_name = unquote(url).split('/')[-1].split('?')[0]
        response = post(
            url=urljoin(config['alist']['base_url'], '/api/fs/get'),
            headers={
                'authorization': str(auth_token)
            },
            json={
                'path': join(config['alist']['root'], name, file_name)
            }
        )
        if response.status_code == 200:
            logger.info('File check successful, file exists')
            return shorten(urljoin(config['alist']['base_url'], quote(join(config['alist']['root'], name, file_name))))
        else:
            logger.error('File check failed with status code: {}'.format(response.status_code))
            return False
