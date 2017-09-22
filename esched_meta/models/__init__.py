from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

from esched_meta.models.user import User

engine = create_engine("postgres://postgres@localhost/esched_meta", echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)