from uuid import UUID
from src.database import Base
from sqlalchemy import String, Boolean, Integer, Column, ARRAY, DateTime, Date
from uuid import uuid4

class Persistent(object):
    createdOn = Column(DateTime)
    createdBy = Column(String, nullable=True)
    lastModifiedOn = Column(DateTime, nullable=True)
    lastModifiedBy = Column(String, nullable=True)
    version = Column(Integer)
    effectiveFrom = Column(Date, nullable=True)
    isEnabled = Column(Boolean)
    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid4)

