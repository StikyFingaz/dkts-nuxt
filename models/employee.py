from datetime import datetime
from typing import Optional
from pydantic import EmailStr
from sqlmodel import AutoString, Field, SQLModel


class EmpPlayLink(SQLModel, table=True):
    play_id: Optional[int] = Field(
        default=None, foreign_key='play.id', primary_key=True
    )
    actor_id: Optional[int] = Field(
        default=None, foreign_key='actor.id', primary_key=True
    )


class Employee(SQLModel):
    name: str = Field(index=True)
    nickname: str = Field(unique=True, index=True)
    gender: str | None
    locations: str
    email: EmailStr = Field(index=True, unique=True, sa_type=AutoString)
    age: datetime | None
    height: int | None
    current: bool = Field(default=True, index=True)
