from typing import Optional
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlmodel import and_, select, Session
from babel_config import babel
from dependencies import get_entase_raw_data, get_session
from models.actor import Actor, ActorBase, ActorRead, ActorTranslations
from models.play import PlayRead, PlayTranslations
from .plays_router import get_entase_data

router = APIRouter(
    prefix='/actors',
    tags=['actors'],
    dependencies=[],  # Add dependencies here
    responses={}  # Add responses here
)


class ReadActor(ActorBase):
    id: int
    plays: Optional[list[PlayRead]] = None
    translation: Optional[dict] = None


# @router.post('/')
# def insert_actor(actor: ActorCreate, session: Session = Depends(get_session)):
#     actor_entry = Actor.from_orm(actor)
#     session.add(actor_entry)
#     return actor_entry


@router.get('/', response_model=list[ActorRead])  # response_model=list[ActorRead]
def fetch_actors(session: Session = Depends(get_session)):
    actors = session.exec(select(Actor).where(Actor.current)).all()
    actors_dict = jsonable_encoder(actors)

    actor_translations = None
    if babel.locale != 'en':
        actor_translations = session.exec(select(ActorTranslations).where(
            ActorTranslations.lang_code == babel.locale
        )).all()
        actor_translations = {translation.actor_id: translation for translation in actor_translations}

    for i, actor in enumerate(actors):
        actors_dict[i]['translation'] = jsonable_encoder(
            actor_translations[actor.id], include={'name', 'short_bio'}
        ) if actor_translations else None

    return actors_dict


@router.get('/{actor_nickname}', response_model=ReadActor)  # response_model=ActorRead
async def fetch_actor(actor_nickname: str,
                      entase_data: dict = Depends(get_entase_raw_data),
                      session: Session = Depends(get_session)):

    actor = session.exec(select(Actor).where(Actor.nickname == actor_nickname)).first()
    actor_dict = actor.dict()
    actor_plays: list[dict] = [play.dict() for play in actor.plays]
    actor_translation = None

    for i, play in enumerate(actor.plays):
        if play.current:
            play_dict = play.dict()
            await get_entase_data(play_dict, entase_data)
            actor_plays[i] = play_dict

    if babel.locale != 'en':
        actor_translation = session.exec(select(ActorTranslations).where(and_(
            ActorTranslations.lang_code == babel.locale,
            ActorTranslations.actor_id == actor.id
        ))).first()

        for i, play in enumerate(actor.plays):
            actor_plays[i]['translation'] = session.exec(select(PlayTranslations).where(and_(
                PlayTranslations.lang_code == babel.locale,
                PlayTranslations.play_id == play.id
            ))).first()

    actor_dict['plays'] = actor_plays
    actor_dict['translation'] = actor_translation

    return jsonable_encoder(actor_dict)
