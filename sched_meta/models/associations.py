from sqlalchemy import ForeignKey, Column, Integer, Table

from sched_meta.models import Base

user_group_association_table = Table('user_group_associations', Base.metadata,
                                     Column('user_id', Integer, ForeignKey('users.id')),
                                     Column('group_id', Integer, ForeignKey('groups.id'))
                                     )
