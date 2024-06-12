from typing import Any, Dict, List
from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi_babel import _  # noqa - imports gettext
from fastapi_mail import FastMail, MessageSchema, MessageType
import pendulum
from pydantic import BaseModel, EmailStr
from sqlmodel import select
from app_config import email_config
from dependencies import get_basic_credentials, get_session
from models.actor import Actor
from .translations_router import festival_strings

router = APIRouter(
    prefix='/email',
    tags=['email'],
    dependencies=[],  # Add router dependencies here
    responses={}  # Add router dependencies here
)


class EmailSchema(BaseModel):
    # Birthday reminder schema
    email: List[EmailStr] = [
        'bozukov.p@gmail.com', 'elenkim17@gmail.com',
        'info@dktshumen.com', 'drumevipraznici@dktshumen.com'
    ]
    body: Dict[str, Any] = {}


# TODO: Remove basic authentication when it's moved to API level
@router.post('/reminders/birthday')
async def send_birthday_reminder(is_authorized: Annotated[bool, Depends(get_basic_credentials)],
                                 session=Depends(get_session)):

    actors = session.exec(select(Actor).where(Actor.current)).all()
    birthdays = {}
    for actor in actors:
        if actor.age:
            birthday = pendulum.instance(actor.age).naive()
            # Adjust when to send email reminders
            birthday_is_upcoming = {
                birthday.is_birthday(): 'today',
                birthday.is_birthday(pendulum.now().add(days=7)): 'in 7 days',
                # birthday.is_birthday(pendulum.now().add(days=8)): 'in 8 days'
            }.get(True)

            if birthday_is_upcoming:
                birthdays[actor.name] = {
                    'birthday': birthday.format('DD.MM.YYYY'),
                    'age': birthday.age, 'birthday_is_upcoming': birthday_is_upcoming
                }

    if is_authorized and birthdays:
        email_data = EmailSchema()
        email_data.body['birthdays'] = birthdays
        email_data.body['recipients'] = ['Eli']

        message = MessageSchema(
            subject='Automatic Birthday Reminder',
            recipients=email_data.model_dump().get('email'),
            template_body=email_data.model_dump().get('body'),
            subtype=MessageType.html
        )

        config = email_config
        config.MAIL_FROM = 'birthday-reminder@dktshumen.com'
        fm = FastMail(config)
        await fm.send_message(message, template_name='birthday_reminder.html')
        return JSONResponse(status_code=200, content={'message': 'email has been sent'})

    elif is_authorized and not birthdays:
        return JSONResponse(status_code=200, content={'message': 'no upcoming birthdays'})

    return {'HTTPException': 'Unauthorized'}


@router.post('/festival/submit-form')
async def submit_form(form_data: dict):
    form_dict = {}
    for k, v in form_data.items():
        form_dict[festival_strings[k]] = v

    email_data = EmailSchema()
    email_data.body['form_dict'] = form_dict

    message = MessageSchema(
        subject='Automatic Application Form',
        recipients=email_data.model_dump().get('email')[2:],

        template_body=email_data.model_dump().get('body'),
        subtype=MessageType.html
    )

    config = email_config
    config.MAIL_FROM = 'info@dktshumen.com'
    fm = FastMail(config)
    await fm.send_message(message, template_name='application_form.html')
    return JSONResponse(status_code=200, content={'message': 'email has been sent'})
