import httpx

from typing import TypedDict
from config import config


class MessageServiceType(TypedDict):
    text: str


def make_request(path, access_token=None):
    url = f"{config['API']['API_SERVER_URL']}{path}"
    if access_token is None:
        headers = {}
    else:
        headers = {
            'authorization': 'Bearer {}'.format(access_token)
        }

    r = httpx.get(url, headers=headers)
    return r.json()


class MessageService:

    def public_message(self) -> MessageServiceType:
        return {
            'text': 'This is a public message.'
        }

    def protected_message(self, access_token):
        return make_request('/api/messages/protected', access_token)

    def admin_message(self, access_token):
        return make_request('/api/messages/admin', access_token)