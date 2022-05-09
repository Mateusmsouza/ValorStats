import logging
import traceback
from typing import Dict, List, Optional

from services.agents_service import AgentsService

LOGGER = logging.getLogger('sLogger')

class AgentsController:

    def get_agents(self, language: str) -> List[Optional(Dict)]:
        try:
            agents = AgentsService().get_agents(language=language)
            LOGGER.info('sucessfully retrieved agents')
            return agents
        except Exception:
            LOGGER.critical(traceback.format_exc())