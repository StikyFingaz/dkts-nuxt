from fastapi import APIRouter

router = APIRouter(
    prefix='/festival',
    tags=['festival'],
    dependencies=[],  # Add dependencies here
    responses={}  # Add responses here
)


@router.get('/')
async def fetch_festival_data():
    pass
