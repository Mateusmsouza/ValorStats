from fastapi import APIRouter

from controllers.agents_controller import AgentsController

router = APIRouter()

@router.get("/agents")
async def get_agents():
    return AgentsController().get_agents()