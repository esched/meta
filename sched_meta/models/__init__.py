from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sched_meta.models.user import User
from sched_meta.models.group import Group
