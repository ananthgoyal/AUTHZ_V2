from db.session import Base
from sqlalchemy import String, Boolean, Integer, Column, ARRAY, DateTime, Date, UUID
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from uuid import uuid4

class Persistent(object):
    createdOn = Column(DateTime, default=datetime.now())
    createdBy = Column(UUID(as_uuid = True), nullable=True)
    lastModifiedOn = Column(DateTime, nullable=True, default=None)
    lastModifiedBy = Column(UUID(as_uuid = True), nullable=True, default=None)
    version = Column(Integer, nullable=False)
    effectiveFrom = Column(Date, nullable=True, default=None)
    isEnabled = Column(Boolean, default = True)
    id = Column(UUID(as_uuid = True), primary_key=True, unique=True, default=uuid4)
    __mapper_args__ = {"version_id_col": version}
    

