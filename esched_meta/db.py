from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.session import Session as SessionType

from esched_meta.models import Base

import logging

logging.getLogger("sqlalchemy.engine.base.Engine").propagate = False
engine = create_engine("postgres://postgres@localhost/esched_meta", echo=True)

Session = sessionmaker(bind=engine)
db_session = scoped_session(Session)  # type: SessionType


def init_db():
    Base.metadata.create_all(engine)
