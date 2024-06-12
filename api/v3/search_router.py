from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import load_only
from sqlmodel import select, Session
from babel_config import babel
from dependencies import get_session
from models.actor import Actor, ActorTranslations
from models.play import Play, PlayTranslations

router = APIRouter(
    prefix='/search',
    tags=['search'],
    dependencies=[],  # Add dependencies here
    responses={}  # Add responses here
)


class ActorResult(BaseModel):
    name: str
    nickname: str
    type: str = 'actor'
    param: str = 'nickname'


class PlayResult(BaseModel):
    name: str
    slug: str
    type: str = 'play'
    param: str = 'slug'


class SearchResults(BaseModel):
    actors: list[ActorResult]
    plays: list[PlayResult]


def fetch_actor_data(session: Session):
    actor_ids = session.exec(
        select(Actor).where(Actor.current).options(
            load_only(Actor.id)
        )
    ).all()

    if babel.locale != 'en':
        actors = session.exec(
            select(ActorTranslations).where(
                ActorTranslations.actor_id.in_([actor.id for actor in actor_ids])
            )
        ).all()
    else:
        actors = session.exec(select(Actor).where(Actor.current)).all()

    return actors


def fetch_play_data(session: Session):
    if babel.locale != 'en':
        plays = session.exec(select(PlayTranslations)).all()
    else:
        plays = session.exec(select(Play)).all()

    return plays


@router.get('/', response_model=SearchResults)
async def fetch_search_data(session=Depends(get_session)):
    actors = fetch_actor_data(session)
    plays = fetch_play_data(session)

    return {'actors': actors, 'plays': plays}
