from uuid import UUID
from src.database import Base
from sqlalchemy import String, Boolean, Integer, Column, ARRAY, DateTime, Date
from uuid import uuid4

class Persistent(object):
    createdOn = Column(DateTime)
    createdBy = Column(UUID(as_uuid=True), nullable=True)
    lastModifiedOn = Column(DateTime, nullable=True, default=None)
    lastModifiedBy = Column(UUID(as_uuid=True), nullable=True, default=None)
    version = Column(Integer)
    effectiveFrom = Column(Date, nullable=True, default=None)
    isEnabled = Column(Boolean)
    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid4)

