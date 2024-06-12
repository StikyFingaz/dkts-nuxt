from datetime import datetime
from typing import ForwardRef, List, Optional
import pendulum
from pydantic import BaseModel, field_validator  # ValidationError, ValidationInfo
from sqlmodel import Column, Field, Relationship, SQLModel, String, Text, UniqueConstraint
from models.employee import EmpPlayLink, Employee

Play = ForwardRef('Play')


class ActorBase(Employee):
    quote: Optional[str] = Field(default=None, sa_column=Column(String(1000)))
    short_bio: str = Field(sa_column=Column(Text))


# Subclasses for actors
class Actor(ActorBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    plays: List[Play] = Relationship(back_populates='actors', link_model=EmpPlayLink)

    # TODO: Set proper relationship Actor-ActorTranslation


class ActorCreate(ActorBase):

    # The warning comes from PyCharm but
    # decorators are used in this order in Pydantic docs.
    @field_validator('age', mode='before')  # noqa - decorator callable warning
    @classmethod
    def set_age(cls, v: str):
        if v:
            dt = pendulum.from_format(v, 'DD-MM-YYYY').to_iso8601_string()
            v = datetime.fromisoformat(dt)
        else:
            v = None
        return v

    @field_validator('height', mode='before')  # noqa - decorator callable warning
    @classmethod
    def set_height(cls, v):
        try:
            v = int(v)
        except ValueError:
            v = None
        return v

    @field_validator('nickname')  # noqa - decorator callable warning
    @classmethod
    def make_slug(cls, v):
        return v.lower().replace(' ', '-')


class ActorUpdate(ActorBase):
    pass


class ActorRead(BaseModel):
    id: int
    name: str
    nickname: str
    short_bio: str
    translation: Optional[dict] = None

    """Example of excluding fields. To only include certain fields
    inherit from BaseModel and add matching fields."""
    # class Config:
    #     fields = {'name': {'exclude': True}}


class ActorTranslations(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint('actor_id', 'lang_code', name='actor_id_lang_code'),
    )

    id: Optional[int] = Field(default=None, primary_key=True)
    actor_id: Optional[int] = Field(foreign_key='actor.id', index=True)
    lang_code: str = Field(default='bg', index=True)
    name: str
    nickname: str = Field(unique=True)
    gender: Optional[str] = None
    locations: str
    quote: Optional[str] = Field(default=None, sa_column=Column(String(1000)))
    short_bio: str = Field(sa_column=Column(Text))
