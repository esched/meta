from esched_meta.models import Base

from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer)
    tg_username = Column(String)

    def __repr__(self):
        return f"<User(id={self.id}, th_id={self.tg_id}, tg_username={self.tg_username})>"

    def as_json(self):
        return {
            "id": self.id,
            "tg_id": self.tg_id,
            "tg_username": self.tg_username
        }
