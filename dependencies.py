import secrets
import time
from typing import Annotated
from fastapi import Depends, Header, HTTPException, status
from fastapi.security import HTTPBasicCredentials
import httpx
import pendulum
from sqlmodel import Session
from werkzeug.datastructures import LanguageAccept
from werkzeug.http import parse_accept_header
from app_config import settings
from babel_config import babel, LANGUAGES
from database import engine


# Global dependency to set the preferred locale according to Accept-Language
async def get_locale(
        accept_language: Annotated[str | None, Header()] = None,
        x_user_locale: Annotated[str | None, Header()] = None):

    babel.locale = (
            x_user_locale or
            LanguageAccept(parse_accept_header(accept_language)).best_match(LANGUAGES) or
            'bg'
    )

    pendulum.set_locale(babel.locale)

    # Uncomment below for testing
    # babel.locale = 'bg'
    # pendulum.set_locale('bg')


# Get user timezone for pendulum
async def get_user_timezone(x_user_timezone: Annotated[str | None, Header()] = None):
    if x_user_timezone == 'Europe/Kyiv':
        tz = 'Europe/Kiev'
        return tz

    return x_user_timezone


# Get session dependency to use with all models
async def get_session() -> Session:
    with Session(engine) as session:
        yield session


async def get_basic_credentials(credentials: Annotated[HTTPBasicCredentials, Depends(settings.basic_security)]):
    current_username_bytes = credentials.username.encode('UTF-8')
    correct_username_bytes = settings.basic_user.encode('UTF-8')
    is_correct_username = secrets.compare_digest(current_username_bytes, correct_username_bytes)

    current_password_bytes = credentials.password.encode('UTF-8')
    correct_password_bytes = settings.basic_pass.encode('UTF-8')
    is_correct_password = secrets.compare_digest(current_password_bytes, correct_password_bytes)

    if not (is_correct_username and is_correct_password):
        time.sleep(3)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    return True


async def entase_http_basic():
    api_key = settings.entase_api_key
    auth = httpx.BasicAuth(api_key, '')
    return auth


async def get_entase_raw_data():
    auth = await entase_http_basic()
    entase_api_url = (f'https://api.entase.com/v2/events?'  # f'&filter[productionID]={play.entase_id}'
                      f'filter[status][0]=1'
                      f'&extend[0]=productionTitle')

    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(entase_api_url, auth=auth)
            entase_data = r.json()
    except httpx.HTTPError as exc:
        print(f'HTTP exception for {exc.request.url} - {exc}')

    return entase_data
