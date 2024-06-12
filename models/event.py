from sqlmodel import Column, Field, SQLModel, Text


class Event(SQLModel):
    name: str = Field(index=True)
    slug: str = Field(unique=True)
    current: bool = Field(False, index=True)
    highlight: bool = Field(False, index=True)
    short_description: str = Field(sa_column=Column(Text))
