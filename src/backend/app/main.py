from math import perm
from urllib import response
from crud.crud_permission import CRUD_Permission
from db.session import SessionLocal
from fastapi import FastAPI, Request, Depends, Form, status, HTTPException
from fastapi.encoders import jsonable_encoder
from db.session import Base, engine
from schemas.Role import Role
from schemas.Persistent import Persistent
from schemas.Permission import Permission
import models
from typing import List
from crud.crud_role import CRUD_Role
from crud.base import CRUDBase

app = FastAPI()
session = SessionLocal()

roleCrud = CRUD_Role()
permCrud = CRUD_Permission()

@app.get('/')
def index():
    return {"message": "Authz V2"}

"""Create a Role"""
@app.post('/roles', status_code = status.HTTP_201_CREATED)
def create_role(role: Role):
    return roleCrud.create(session, obj_in=role)

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
    return roleCrud.update(session, obj_id = role_guid, obj_in=role)

"""Delete a Role"""
@app.delete('/roles/{role_guid}')
def delete_role(role_guid: str):
    return roleCrud.delete(session, id = role_guid)

"""Create a Permission"""
@app.post('/permissions', status_code = status.HTTP_201_CREATED)
def create_permission(permission: Permission):
    return permCrud.create(session, obj_in=permission)

"""Read all Permissions"""
@app.get('/permissions', response_model = List[Permission], status_code = 200)
def read_all_permissions():
    return permCrud.read_all(session)

"""Read Single Permission"""
@app.get('/permissions/{perm_guid}', response_model = Permission, status_code = 200)
def read_permission(perm_guid: str):
    return permCrud.read(session, perm_guid)

"""Update a Permission"""
@app.put('/permissions/{perm_guid}', response_model = Permission, status_code=status.HTTP_200_OK)
def update_permission(perm_guid:str, perm: Permission):
    return permCrud.update(session, obj_id = perm_guid, obj_in=perm)

"""Delete a Permission"""
@app.delete('/permissions/{perm_guid}')
def delete_permission(perm_guid: str):
    return permCrud.delete(session, id = perm_guid)

def init_db():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    init_db()