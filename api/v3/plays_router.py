import csv
from operator import itemgetter
from pathlib import Path
from typing import Optional
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
import pendulum
from sqlmodel import and_, or_, select, Session
from app_config import settings
from babel_config import babel
from dependencies import get_entase_raw_data, get_session, get_user_timezone
from models.actor import ActorRead, ActorTranslations
from models.play import Play, PlayBase, PlayRead, PlayTranslations

router = APIRouter(
    prefix='/plays',
    tags=['plays'],
    dependencies=[],  # Add dependencies here
    responses={}  # Add responses here
)


class ReadPlay(PlayBase):
    actors: Optional[list[ActorRead]] = None
    has_trailer: bool = False
    entase_data: Optional[list] = None
    translation: Optional[dict] = None


async def get_entase_data(play: dict, entase_data: dict, user_timezone: str | None = None) -> dict:
    entase_events = [
        event for event in entase_data['resource']['data'] if event['productionID'] == play['entase_id']
    ]
    entase_events.sort(key=itemgetter('dateStart'))

    for event in entase_events:
        event['dateStart'] = pendulum.from_timestamp(
            event['dateStart'], tz=user_timezone).format('dddd, DD.MM.YYYY - HH:mm')

    play['entase_data'] = entase_events

    return play


working_dirs = settings.working_dirs
working_env = settings.work_env


# Route order matters! Moving highlights to the bottom will cause
# error 500 because FastAPI tries to match 'highlights' as path parameter
# in @router.get('/{play_slug}'
@router.get('/highlights', response_model=list[PlayRead])  # response_model=list[PlayRead]
async def fetch_highlights(session: Session = Depends(get_session),
                           entase_data: dict = Depends(get_entase_raw_data)):

    highlights = session.exec(select(Play).where(or_(
        Play.highlight,
        Play.premiere
    ))).all()
    highlights_dict = jsonable_encoder(highlights)

    # TODO: Should make a function to get play translation similar to get_entase_data()
    play_translations = None
    if babel.locale != 'en':
        play_translations = session.exec(select(PlayTranslations).where(and_(
            PlayTranslations.lang_code == babel.locale,
            PlayTranslations.play_id.in_([play.id for play in highlights])  # noqa - play_id is a Column not int
        ))).all()
        play_translations = {play_translation.play_id: play_translation for play_translation in play_translations}

    for i, play in enumerate(highlights):
        highlights_dict[i]['translation'] = jsonable_encoder(
            play_translations[play.id], include={'name', 'short_description'}
        ) if play_translations else None

        if play.current:
            highlights_dict[i] = await get_entase_data(highlights_dict[i], entase_data)

    return highlights_dict


@router.get('/festival')
async def fetch_plays(user_timezone: str = Depends(get_user_timezone),
                      entase_data: dict = Depends(get_entase_raw_data)):

    csv_file = "./csv/festival-2024.csv"
    with open(csv_file, 'r') as csvfile:
        plays_list = list(csv.DictReader(csvfile))

        for i, play in enumerate(plays_list):
            plays_list[i] = dict(play)
            plays_list[i] = await get_entase_data(plays_list[i], entase_data, user_timezone=user_timezone)

        return plays_list


# The comments are instructions how to include actors
@router.get('/', response_model=list[PlayRead])  # ReadPlay response_model=list[ReadPlay]
async def fetch_plays(session: Session = Depends(get_session),
                      entase_data: dict = Depends(get_entase_raw_data)):
    plays = session.exec(select(Play)).all()
    plays_dict = jsonable_encoder(plays)

    play_translations = None
    if babel.locale != 'en':
        play_translations = session.exec(select(PlayTranslations).where(
            PlayTranslations.lang_code == babel.locale
        )).all()
        play_translations = {play_translation.play_id: play_translation for play_translation in play_translations}

    for i, play in enumerate(plays):
        plays_dict[i]['translation'] = jsonable_encoder(
            play_translations[play.id], include={'name'}
        ) if play_translations else None
        plays_dict[i]['filter'] += f',{play.current},{play.audience}'.lower()

        if play.current:
            plays_dict[i] = await get_entase_data(plays_dict[i], entase_data)

    return plays_dict


@router.get('/{play_slug}', response_model=ReadPlay)  # response_model=PlayRead
async def fetch_play(play_slug: str, session: Session = Depends(get_session),
                     user_timezone: str = Depends(get_user_timezone),
                     entase_raw_data: dict = Depends(get_entase_raw_data)):

    play = session.exec(select(Play).where(Play.slug == play_slug)).first()
    play_dict = play.dict()
    play_actors = play.actors
    play_translation = None
    # play_trailer = Path() / f'{working_dirs[working_env]}/media/plays/{play_slug}/videos/trailer.webm'

    if babel.locale != 'en':
        play_translation = session.exec(select(PlayTranslations).where(and_(
            PlayTranslations.play_id == play.id,
            PlayTranslations.lang_code == babel.locale
        ))).first()

        actor_translations = []
        for i, actor in enumerate(play_actors):
            actor_dict = actor.dict()
            actor_dict['translation'] = jsonable_encoder(
                session.exec(select(ActorTranslations).where(and_(
                    ActorTranslations.lang_code == babel.locale,
                    ActorTranslations.actor_id == actor.id
                ))).first(),
                include={'name'}
            )
            actor_translations.append(actor_dict)

        play_actors = actor_translations

    if play.current:
        play_dict = await get_entase_data(play_dict, entase_raw_data, user_timezone)

    play_dict['actors'] = play_actors
    play_dict['translation'] = play_translation
    # play_dict['has_trailer'] = play_trailer.exists()

    return jsonable_encoder(play_dict)
