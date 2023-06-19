from db.base_class import Base  
from models.Role import Role
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from crud.base import CRUDBase
import models

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUD_Role(CRUDBase):
    
    def __init__(self):
        super().__init__(models.Role.Role)
    