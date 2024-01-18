from datetime import datetime

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .config.settings import settings
from .routes.default_routes import default_routes
from .routes.user_routes import user_routes

app = FastAPI(title='FastAPI-Users-Backend', description='CRUD API')

app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*'])

app.mount('/static', StaticFiles(directory='static'), name='static')

app.include_router(user_routes, tags=['Users'], prefix='/api/v1/users')
app.include_router(default_routes)

if __name__ == '__main__':
    print(f'Application is up and running on {settings.host}:{settings.port}')
    uvicorn.run(app, host=settings.host, port=settings.port)
