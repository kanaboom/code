from sqlalchemy.ext.declarative import declarative_base
from common.server_env import ServerEnve
from sqlmodel import create_engine, Session
import sqlalchemy as sql

DATABASE_URL = "postgresql://{0}/{1}@{2}:{3}/{4}".format(
    ServerEnve().postgres_user,
    ServerEnve().postgres_pass,
    ServerEnve().postgres_host,
    ServerEnve().postgres_port,
    ServerEnve().postgres_db
)
engine = create_engine(DATABASE_URL)
Base = declarative_base()
metadata = sql.Metadata()

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()