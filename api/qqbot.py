from configparser import ConfigParser
from logging import getLogger
from urllib.parse import urljoin

from requests import post

# Initialize the logger
logger = getLogger(__name__)

config = ConfigParser()
config.read('config.ini')


def post_to_channel(
        name: str,
        number: str,
        link: str
):
    try:
        response = post(
            url=urljoin(config['qqbot']['base_url'], '/sendGroupMessage'),
            headers={
                'Content-Type': 'application/json'
            },
            json={
                'target': config['qqbot']['group_id'],
                'messageChain': [{
                    'type': 'Plain',
                    'text': f'{name}更新第{number}集啦！\n点此链接观看：{link}'
                }]
            }
        )
        if response.status_code == 200:
            logger.info(f'Successfully posted to channel: {name} Episode {number}')
        else:
            logger.error(f'Failed to post to channel. Status code: {response.status_code}')
    except Exception as e:
        logger.error(f'Exception occurred while posting to channel: {e}')
