from collections import defaultdict
from fastapi import APIRouter, Depends
import pendulum
from sqlalchemy.orm import load_only
from sqlmodel import and_, select, Session
from babel_config import babel
from dependencies import get_entase_raw_data, get_user_timezone, get_session
from models.play import Play, PlayTranslations

router = APIRouter(
    prefix='/calendar',
    tags=['calendar'],
    dependencies=[],  # Add dependencies here
    responses={}  # Add responses here
)


@router.get('/')
async def fetch_data(session: Session = Depends(get_session),
                     user_timezone: str = Depends(get_user_timezone),
                     entase_data: dict = Depends(get_entase_raw_data)):
    plays = session.exec(select(Play).where(and_(
        Play.current, Play.entase_id
    )).options(load_only(
        Play.name, Play.slug, Play.entase_id, Play.length, Play.director, Play.stage, Play.genre
    ))).all()

    db_entase_ids = [play.entase_id for play in plays]

    play_translations = None
    if babel.locale != 'en':
        play_translations = session.exec(select(PlayTranslations).where(and_(
            PlayTranslations.lang_code == babel.locale,
            PlayTranslations.play_id.in_([play.id for play in plays])  # noqa - play_id is a Column not int
        )).options(load_only(
            PlayTranslations.name, PlayTranslations.genre, PlayTranslations.director, PlayTranslations.stage
        ))).all()
        play_translations = {play_translation.play_id: play_translation for play_translation in play_translations}

    plays = {
        play.entase_id:
            {
                'databaseID': play.id, 'slug': play.slug, 'length': play.length,
                'name': play.name, 'genre': play.genre, 'director': play.director,
                'stage': play.stage, 'translation': play_translations[play.id] if play_translations else None
            }
        for play in plays
    }

    event_dates = defaultdict(list)
    current_events = sorted(entase_data['resource']['data'], key=lambda evt: evt['dateStart'])
    for event in current_events:
        entase_id = event['productionID']

        if entase_id in db_entase_ids:
            date = pendulum.from_timestamp(event['dateStart']).format('DD-MMMM-dddd')
            start_time = pendulum.from_timestamp(event['dateStart'], tz=user_timezone).format('HH:mm')
            event_data = {
                'entaseID': entase_id,
                'eventID': event['id'],
                'eventDate': date,
                'eventStart': start_time,
                'eventStats': event['stats'],
                'eventDetails': plays[entase_id]
            }
            event_dates[date].append(event_data)

    return event_dates
