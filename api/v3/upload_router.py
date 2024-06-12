from b2sdk.v2 import *
from fastapi import APIRouter, UploadFile

router = APIRouter(
    prefix='/uploads',
    tags=['uploads'],
    dependencies=[],  # Add dependencies here
    responses={}  # Add responses here
)

info = InMemoryAccountInfo()
b2_api = B2Api(info)
application_key_id = '004d9f1a6c08abf0000000004'
application_key = 'K004dGp6Mh5VPKMm+BepXyl8/yJFcWg'
b2_api.authorize_account('production', application_key_id, application_key)


@router.post('/upload')
async def upload_files(file: UploadFile):
    contents = await file.read()
    bucket = b2_api.get_bucket_by_name('dkts-test')

    bucket.upload_bytes(
        data_bytes=contents, file_name=file.filename,
        content_type=file.content_type
    )

    return {'filenames': file.filename}
