from datetime import datetime
from typing import ForwardRef, List, Annotated, Optional
import pendulum
from pydantic import BaseModel, ConfigDict, field_validator, model_validator
from sqlmodel import Column, Field, Relationship, select, Session, SQLModel, String, Text, UniqueConstraint
from database import engine
from models.employee import EmpPlayLink
from models.event import Event

Actor = ForwardRef('Actor')


class PlayBase(Event):
    entase_id: str | None = Field(index=True)
    director: str | None
    scenographer: str | None
    composer: str | None
    author: str | None
    dramatization: str | None
    artistic_director: str | None
    translator: str | None
    length: int | None
    stage: str | None = Field('Other Location', index=True)
    theater: str | None = Field('DKT Shumen')
    genre: str | None = Field('Other', index=True)
    filter: str | None = Field('other', index=True)
    audience: str = Field(index=True)
    premiere: bool = Field(False, index=True)
    oad: datetime | None
    trivia: str | None = Field(sa_column=Column(String(1000)))


# Full text index example
# Index('idx_play_name', Play.name, mysql_prefix='FULLTEXT')


class Play(PlayBase, table=True):
    # TODO: set a proper relationship Play-PlayTranslations with Relationship and backpopulates
    id: Optional[int] = Field(default=None, primary_key=True)
    actors: List[Actor] = Relationship(back_populates='plays', link_model=EmpPlayLink)


class PlayCreate(PlayBase):

    # The warning comes from PyCharm but
    # decorators are used in this order in Pydantic docs.
    @model_validator(mode='before')  # noqa - decorator callable warning
    @classmethod
    def set_slug(cls, values):
        if 'slug' not in values:
            values['slug'] = values['name'].lower().replace(' ', '-')
        return values

    @field_validator('entase_id', mode='before')  # noqa - decorator callable warning
    @classmethod
    def set_entase_id(cls, v):
        if v == '':
            v = None
        return v

    @field_validator('length', mode='before')  # noqa - decorator callable warning
    @classmethod
    def set_length(cls, v):
        try:
            v = int(v)
        except ValueError:
            v = None
        return v

    @field_validator('theater', mode='before')  # noqa - decorator callable warning
    @classmethod
    def set_theater(cls, v):
        if v == '':
            v = None
        return v

    @field_validator('genre', mode='before')  # noqa - decorator callable warning
    @classmethod
    def set_genre(cls, v):
        if v == '':
            v = None
        return v

    @field_validator('filter', mode='before')  # noqa - decorator callable warning
    @classmethod
    def set_filter(cls, v):
        if v == '':
            v = None
        return v

    @field_validator('oad', mode='before')  # noqa - decorator callable warning
    @classmethod
    def set_oad(cls, v):
        if v:
            dt = pendulum.from_format(v, 'DD-MM-YYYY').to_iso8601_string()
            v = datetime.fromisoformat(dt)
        else:
            v = None
        return v


class PlayRead(BaseModel):
    id: int
    name: str
    slug: str
    filter: str
    short_description: str
    current: bool
    highlight: bool
    premiere: bool
    entase_data: Optional[list] = None
    translation: Optional[dict] = None

    """Model configuration is now an attribute
    and not a separate class."""
    # model_config = ConfigDict()
    # class Config:
    #     fields = {'name': {'exclude': True}}


class PlayUpdate(PlayBase):
    pass


class PlayTranslations(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint('play_id', 'lang_code', name='play_id_lang_code'),
    )

    id: Optional[int] = Field(default=None, primary_key=True)
    play_id: Optional[int] = Field(default=None, foreign_key='play.id', index=True)
    slug: str = Field(default=None, foreign_key='play.slug')
    name: str
    director: str | None = Field(default=None)
    scenographer: str | None = None
    composer: str | None = None
    author: str | None = None
    dramatization: str | None = None
    artistic_director: str | None = None
    translator: str | None = None
    stage: str | None = Field(default=None)
    theater: str = Field(default='DKT Shumen')
    genre: str = Field(default=None)
    lang_code: str = Field(default='bg', index=True)
    short_description: str = Field(sa_column=Column(Text))
    trivia: str | None = Field(default=None, sa_column=Column(String(1000)))

    @model_validator(mode='before')  # noqa - decorator callable warning
    @classmethod
    def get_play(cls, values):
        with Session(engine) as session:
            play_id = values.get('play_id')
            play = session.exec(select(Play).where(Play.id == play_id)).first()
            if play:
                values['slug'] = play.slug
        return values
