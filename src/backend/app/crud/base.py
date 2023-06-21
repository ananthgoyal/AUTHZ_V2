from datetime import datetime
from db.base_class import Base  
from models.Role import Role
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def read(self, session: Session, id: Any) -> Optional[ModelType]:
        return session.get(self.model, id)

    def read_all(
        self, session: Session, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        return session.query(self.model).offset(skip).limit(limit).all()

    def create(self, session: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data) 
        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj

    def update(self, session: Session, *, obj_id: str, obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> ModelType:
        restricted = ["createdBy", "createdOn", "id", "version", "lastModifiedBy", "lastModifiedOn"] #immutable attributes once created
        allowed = []
        db_obj = session.get(self.model, obj_id)
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data and field not in restricted: #bypass any attempt to change immutable attributes
                setattr(db_obj, field, update_data[field])
        setattr(db_obj, "lastModifiedOn", datetime.now())
        curr_version = getattr(db_obj, "version")
        if getattr(session.get(self.model, obj_id), "version") != curr_version:
            return {"message": "Version Mismatch Error"} #return mismatch error
        setattr(db_obj, "version", curr_version + 1)
        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj

    def delete(self, session: Session, *, id: str) -> ModelType:
        obj = session.query(self.model).get(id)
        session.delete(obj)
        session.commit()
        return obj