from app.db.base_class import Base  
from app.models.Role import Role
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from backend.app.crud.base import CRUDBase

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUD_Permission(CRUDBase):
    pass