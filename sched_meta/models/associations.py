from sqlalchemy import ForeignKey, Column, Integer

from sched_meta.models import Base


class UserGroupAssociationTable(Base):
    __tablename__ = 'user_group_associations'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    group_id = Column(Integer, ForeignKey("groups.id"))
