import logging
import traceback

from services.agents_service import AgentsService

LOGGER = logging.getLogger('sLogger')

class AgentsController:

    def get_agents(self):
        try:
            return AgentsService().get_agents()
        except Exception:
            LOGGER.critical(traceback.format_exc())