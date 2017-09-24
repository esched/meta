from sqlalchemy.orm import relationship

from sched_meta.models import Base

from sqlalchemy import Column, Integer, String, Table, ForeignKey

from sched_meta.models.associations import user_group_association_table


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer)
    tg_username = Column(String)

    groups = relationship('Group', secondary=user_group_association_table, back_populates="users")

    def __repr__(self):
        return f"<User(id={self.id}, th_id={self.tg_id}, tg_username={self.tg_username})>"

    def as_json(self):
        return {
            "id": self.id,
            "tg_id": self.tg_id,
            "tg_username": self.tg_username
        }
