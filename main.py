import logging
from logging.config import fileConfig

from fastapi import FastAPI
import uvicorn

from routers.agents_router import router as agents_routers
import settings

fileConfig('config/logging_config.ini')
LOGGER = logging.getLogger('sLogger')

app = FastAPI()
app.include_router(agents_routers)

def main():
    LOGGER.info(f"running server on port {settings.SERVICE_PORT}")
    uvicorn.run(
        "main:app",
        host=settings.SERVICE_HOST,
        port=int(settings.SERVICE_PORT),
        workers=int(settings.WORKERS_AMOUNT)
    )

if __name__ == '__main__':
    main()
