from models.Persistent import Persistent
from db.session import Base
from sqlalchemy import String, Boolean, Integer, Column, ARRAY, DateTime, Date, UUID
from sqlalchemy.dialects.postgresql import UUID


class Permission(Persistent, Base):
    __tablename__ = "permissions"
    role = Column(UUID(as_uuid = True), nullable=True, default=None)
    can_create = Column(Boolean, default=False)
    can_update = Column(Boolean, default=False)
    can_delete = Column(Boolean, default=False)
    can_read = Column(Boolean, default=False)
    can_read_all = Column(Boolean, default=False)
    can_assign = Column(Boolean, default=False)
    can_share = Column(Boolean, default=False)