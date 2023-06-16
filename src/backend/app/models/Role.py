from models.Persistent import Persistent
from db.session import Base
from sqlalchemy import String, Boolean, Integer, Column, ARRAY, DateTime, Date


class Role(Persistent, Base):
    __tablename__ = "roles"
    name = Column(String(255), nullable=False, default="")
    description = Column(String(1024), nullable=True, default="")
    tags = Column(ARRAY(String), nullable=True, default=[])