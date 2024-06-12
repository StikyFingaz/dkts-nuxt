from sqlmodel import create_engine, SQLModel
from app_config import settings

"""
To generate revision and update the DB:
alembic revision --autogenerate -m "Message"
alembic upgrade head
"""

db_user = settings.db_user
db_pass = settings.db_pass
db_name = settings.db_name

db = f"mysql+pymysql://{db_user}:{db_pass}@localhost/{db_name}"
engine = create_engine(db)  # echo=True - add as a kwarg for testing


def create_db():
    SQLModel.metadata.create_all(engine)
