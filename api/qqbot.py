from configparser import ConfigParser
from urllib.parse import urljoin
from logging import getLogger
from requests import post

# Initialize the logger
logger = getLogger(__name__)

config = ConfigParser()
config.read('../config.ini')

BASE_URL = 'https://sandbox.api.sgroup.qq.com'


# def post_to_channel(name: str, number: str, link: str):
#     try:
#         response = post(
#             url=urljoin(BASE_URL, f'/channels/{config["qqbot"]["channel_id"]}/messages'),
#             headers={
#                 'Content-Type': 'application/json',
#                 'Authorization': f'Bot {config["qqbot"]["app_id"]}.{config["qqbot"]["token"]}'
#             },
#             json={
#                 'content': f'{name}更新第{number}集啦！\n点此链接观看：{link}'
#             }
#         )
#         print(response.json())
#         if response.status_code == 200:
#             logger.info(f'Successfully posted to channel: {name} Episode {number}')
#         else:
#             logger.error(f'Failed to post to channel. Status code: {response.status_code}')
#     except Exception as e:
#         logger.error(f'Exception occurred while posting to channel: {e}')

def post_to_channel(
        name: str,
        number: str,
        link: str
):
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
    print(response.json())


post_to_channel('我们的雨色协议', '06', 'https://mealuet.com/yjrjy7')
