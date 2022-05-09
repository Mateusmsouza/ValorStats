import json
import logging

from api.riot import Riot
from connections.redis import Cache

LOGGER = logging.getLogger('sLogger')
AGENT_NAMES_TO_EXCCLUDE = ['Null UI Data!']

class AgentsService():

    def get_agents(self, language: str) -> list[dict]:
        agents = []
        cache = Cache()

        riot_content = cache.get('riot_content')
        if not riot_content:
            LOGGER.debug('reaching out Riot API...')
            riot_content = Riot().get_content()
            cache.set(key='riot_content', data=json.dumps(riot_content), ttl=300)
        else:
            LOGGER.debug('found cached Riot content')
            riot_content = json.loads(riot_content)

        for agent in riot_content['characters']:
            if agent['name'] not in AGENT_NAMES_TO_EXCCLUDE:
                agents.append({
                    'name': agent['localizedNames'][language],
                    'id': agent['id']
                })
        return agents