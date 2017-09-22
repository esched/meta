from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.session import Session as SessionType

from sched_meta.models import Base

engine = create_engine("postgres://postgres@localhost/sched_meta", echo=True)

Session = sessionmaker(bind=engine)
db_session = scoped_session(Session)  # type: SessionType


def init_db():
    Base.metadata.create_all(engine)
