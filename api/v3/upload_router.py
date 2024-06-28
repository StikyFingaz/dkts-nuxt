from b2sdk.v2 import *
from fastapi import APIRouter, UploadFile
from app_config import settings

router = APIRouter(
    prefix='/uploads',
    tags=['uploads'],
    dependencies=[],  # Add dependencies here
    responses={}  # Add responses here
)

info = InMemoryAccountInfo()
b2_api = B2Api(info)
application_key_id = settings.b2_app_id
application_key = settings.b2_app_key
# Breaks the app with wrong credentials
# b2_api.authorize_account('production', application_key_id, application_key)


@router.post('/upload')
async def upload_files(file: UploadFile):
    contents = await file.read()
    bucket = b2_api.get_bucket_by_name('dkts-test')

    bucket.upload_bytes(
        data_bytes=contents, file_name=file.filename,
        content_type=file.content_type
    )

    return {'filenames': file.filename}
