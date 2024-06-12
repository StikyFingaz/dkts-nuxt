from brotli_asgi import BrotliMiddleware
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from api.v2 import api as api_v2
from api.v3 import api as api_v3
from database import create_db

app = FastAPI()


@app.on_event('startup')
def on_startup():
    create_db()


# Include API routers here
app.include_router(api_v3.api_router)

# The default parameters used by the CORSMiddleware implementation are restrictive.
# Check documentation for origin and other CORS-related problems.
origins = [
    'http://127.0.0.1:3000',
    'http://127.0.0.1:3001',
    'http://192.168.1.4:3001',
    'https://dktshumen.com',
    'https://www.dktshumen.com',
    'https://nuxt.dktshumen.com',
    'https://test.dktshumen.com',
    'https://festival.dktshumen.com',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Add BrotliMiddleware to enable brotli compression
app.add_middleware(BrotliMiddleware)
