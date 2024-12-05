from authlib.integrations.starlette_client import OAuth
from config import config


"""Storing the configuration into the `auth0_config` variable for later usage"""

auth0_config = config['AUTH0']

oauth = OAuth()
oauth.register(
    "auth0",
    client_id=auth0_config['CLIENT_ID'],
    client_secret=auth0_config['CLIENT_SECRET'],
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{auth0_config["DOMAIN"]}/.well-known/openid-configuration'
)