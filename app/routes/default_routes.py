from datetime import datetime

from fastapi import APIRouter

from ..config.settings import settings

default_routes = APIRouter()


@default_routes.get('/')
@default_routes.get('/health-check')
def health_check():
    return {
        'success': True,
        'status': 200,
        'message': f'Hola Mundo! Bienvenida a {settings.app_name}.',
        'time': datetime.now(),
        'database': 'connected',
    }
