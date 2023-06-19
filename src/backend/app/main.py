from urllib import response
from db.session import SessionLocal
from fastapi import FastAPI, Request, Depends, Form, status, HTTPException
from fastapi.encoders import jsonable_encoder
from db.session import Base, engine
from schemas.Role import Role
from schemas.Persistent import Persistent
import models
from typing import List
from crud.crud_role import CRUD_Role
from crud.base import CRUDBase

app = FastAPI()
session = SessionLocal()

roleCrud = CRUD_Role()

@app.get('/')
def index():
    return {"message": "Authz V2"}

"""Create a Role"""
@app.post('/roles', status_code = status.HTTP_201_CREATED)
def create_role(role: Role):
    return roleCrud.create(db = session, obj_in=role)

"""Read All Roles"""
@app.get('/roles', response_model = List[Role], status_code = 200)
def read_all_roles():
    return roleCrud.read_all(session)

"""Read Single Role"""
@app.get('/roles/{role_guid}', response_model = Role, status_code = 200)
def read_role(role_guid: str):
    return roleCrud.read(session, role_guid)

"""Update a Role"""
@app.put('/roles/{role_guid}', response_model = Role, status_code=status.HTTP_200_OK)
def update_role(role_guid:str, role: Role):
    return roleCrud.update(db = session, obj_id = role_guid, obj_in=role)



def init_db():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    init_db()