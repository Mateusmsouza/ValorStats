from typing import Optional

from fastapi import APIRouter, Header

from controllers.agents_controller import AgentsController

router = APIRouter()

@router.get("/agents")
async def get_agents(language: Optional[str] = Header(default='en-US')):
    return AgentsController().get_agents(language=language)