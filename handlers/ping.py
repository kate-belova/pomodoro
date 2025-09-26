from fastapi import APIRouter

from settings import Settings

ping_router = APIRouter(prefix='/ping', tags=['ping'])


@ping_router.get('/db')
async def ping():
    settings = Settings()
    return {'message': settings.GOOGLE_TOKEN_ID}


@ping_router.get('/app')
async def ping_app():
    return {'text': 'app is working'}
