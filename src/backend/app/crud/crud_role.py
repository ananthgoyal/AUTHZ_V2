from db.base_class import Base  
from models.Role import Role
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from crud.base import CRUDBase
import models
from fastapi import FastAPI, HTTPException


from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUD_Role(CRUDBase):
    
    def __init__(self):
        super().__init__(models.Role.Role)
    
    def update(self, session: Session, *, obj_id: str, obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> ModelType:
        pers_obj = super().update(session, obj_id=obj_id, obj_in = obj_in)
        return pers_obj
        #call update on super and then handle specifics towards the role class (permissions, tags, description, etc.)

    def delete(self, session: Session, *, id: str) -> ModelType:
        obj = session.query(self.model).get(id)
        if obj is None:
            raise HTTPException(status_code = 404, detail = "ID does not match any existing object")
        for perm in session.query(models.Permission.Permission).filter(models.Permission.Permission.role == id):
            session.delete(perm)
        session.delete(obj)
        session.commit()
        return obj
    