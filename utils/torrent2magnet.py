from base64 import b32encode
from hashlib import sha1

from bencodepy import decode, encode
from requests import get


def torrent2magnet(
        url: str
):
    response = get(url)
    torrent_data = decode(response.content)
    info_hash = sha1(encode(torrent_data[b'info'])).digest()
    magnet_hash = b32encode(info_hash).decode()
    magnet_link = f'magnet:?xt=urn:btih:{magnet_hash}'
    return magnet_link
