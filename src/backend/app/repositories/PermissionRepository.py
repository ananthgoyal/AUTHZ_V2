from db.base_class import Base  
from models.Permission import Permission
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from repositories.base import CRUDBase
from fastapi import FastAPI, HTTPException
import models
from datetime import datetime

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import *

from db.base_class import Base
from repositories.RoleRepository import RoleRepository

roleCrud = RoleRepository()

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class PermissionRepository(CRUDBase):
    
    def __init__(self):
        super().__init__(models.Permission.Permission)

    def create(self, session: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        role_id = db_obj.role
        roleCrud.read(session, role_id) #check if role is valid
        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj

    def update(self, session: Session, *, obj_id: str, obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> ModelType:
        """Implemented Using Optimistic Version Locking with built in SQLAlchemy tools"""
        try:
            restricted = ["createdBy", "createdOn", "id", "version", "lastModifiedBy", "lastModifiedOn"] #immutable attributes once created
            allowed = []
            db_obj = session.get(self.model, obj_id)
            if db_obj is None:
                raise HTTPException(status_code = 404, detail = "ID does not match any existing object")
            obj_data = jsonable_encoder(db_obj)
            if isinstance(obj_in, dict):
                update_data = obj_in
            else:
                update_data = obj_in.dict(exclude_unset=True)
            if "role" in update_data:
                role_id = update_data["role"]
                roleCrud.read(session, role_id) #check if role is valid and stop if invalid
            for field in obj_data:
                if field in update_data and field not in restricted: #bypass any attempt to change immutable attributes
                    setattr(db_obj, field, update_data[field])
            setattr(db_obj, "lastModifiedOn", datetime.now())
            session.add(db_obj)
            session.commit()
            session.refresh(db_obj) 
            return db_obj
        except StaleDataError:
            raise HTTPException(status_code = 409, detail = "Version Number Conflict Error") #return mismatch error