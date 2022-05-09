import logging
import requests

import settings

LOGGER = logging.getLogger('sLogger')


class Riot():

    def __init__(self) -> None:
        self.host = settings.RIOT_HOST
        self.token = settings.RIOT_TOKEN 

    def get_content(self):
        response = requests.get(
            url=f'{self.host}/val/content/v1/contents',
            headers={
                'X-Riot-Token': self.token
            }
        )

        if response.status_code == 200:
            return response.json()
        LOGGER.info(response)
        raise requests.RequestException(response=response)
