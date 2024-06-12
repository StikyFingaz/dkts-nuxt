from pathlib import Path
from fastapi import APIRouter
from fastapi.responses import FileResponse
from app_config import settings

router = APIRouter(
    prefix='/seo',
    tags=['seo'],
    dependencies=[],  # Add dependencies here
    responses={}  # Add responses here
)


@router.get('/sitemap.xml')
async def get_sitemap():
    sitemap_path = Path(settings.root_dir) / 'VueFrontend/dist/sitemap.xml'
    return FileResponse(sitemap_path, media_type='application/xml')
