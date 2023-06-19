from typing import Optional
from datetime import datetime, date
from pydantic import BaseModel, Field
from uuid import UUID

class Persistent(BaseModel):
    createdOn: Optional[datetime] = Field(None, description = "The datetime stamp object the object was created on; cannot be changed once object is created")
    createdBy: Optional[UUID] = Field(None, description = "The ID of the User object that created this object")
    lastModifiedOn: Optional[datetime]  = Field(None, description = "Datetime object indicating the time stamp this object was last modified")
    lastModifiedBy: Optional[UUID] = Field(None, description = "The of ID of the User object that last edited this object")
    version: Optional[int] = Field(0, description = "The version number of the object")
    effectiveFrom: Optional[date] = Field(None, description = "Date object indicating the time this object is effective from")
    isEnabled: Optional[bool] = Field(True, description = "Whether the object is enabled; default value is True unless changed by User")
    id: Optional[UUID] = Field(None, description = "The unique ID of the object")


