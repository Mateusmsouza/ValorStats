import os

SERVICE_PORT = os.getenv('SERVICE_PORT', '8000')
SERVICE_HOST = os.getenv('SERVICE_HOST', '0.0.0.0')
WORKERS_AMOUNT = os.getenv('WORKERS_AMOUNT', '4')
REDIS_HOST = os.getenv('REDIS_HOST')
RIOT_HOST = os.getenv('RIOT_HOST')
RIOT_TOKEN = os.getenv('RIOT_TOKEN')