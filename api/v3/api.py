from fastapi import APIRouter, Depends
from api.v3 import (
    actors_router, calendar_router, email_router, images_router,
    plays_router, search_router, translations_router, upload_router
)
from dependencies import get_locale

api_router = APIRouter(
    prefix='/api',
    tags=[],
    dependencies=[Depends(get_locale)],
    responses={}
)

api_router.include_router(actors_router.router)
api_router.include_router(calendar_router.router)
api_router.include_router(email_router.router)
api_router.include_router(images_router.router)
api_router.include_router(plays_router.router)
api_router.include_router(search_router.router)
api_router.include_router(translations_router.router)
api_router.include_router(upload_router.router)
