from schemas.Persistent import Persistent
from typing import Optional
from pydantic import Field
from uuid import UUID


class Permission(Persistent):
    """
    Permissions specify what tasks users can perform and what features users can access.
    """
    role: Optional[UUID] = Field(None, description = "The ID of the role this permission is assigned to")
    can_create: Optional[bool] = Field(False , description = "Whether user can create")
    can_update: Optional[bool] = Field(False, description = "Whether user can update")
    can_delete: Optional[bool] = Field(False, description = "Whether user can delete")
    can_read: Optional[bool] = Field(False, description = "Whether user can read")
    can_read_all: Optional[bool] = Field(False, description = "Whether user can read all")
    can_assign: Optional[bool] = Field(False, description = "Whether user can assign")
    can_share: Optional[bool] = Field(False, description = "Whether user can share")

    class Config:
        orm_mode = True