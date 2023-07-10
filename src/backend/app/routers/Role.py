from os import stat
import models
from schemas.Role import Role
from schemas.Persistent import Persistent
from schemas.Permission import Permission
from fastapi import FastAPI, Request, Depends, Form, status, HTTPException, APIRouter
from fastapi.encoders import jsonable_encoder
from db.session import Base, engine
from db.session import SessionLocal
from typing import List
from repositories.RoleRepository import RoleRepository
session = SessionLocal()


router = APIRouter()
roleCrud = RoleRepository()


"""Create a Role"""
@router.post('/roles', status_code = status.HTTP_201_CREATED)
def create_role(role: Role):
    return roleCrud.create(session, obj_in=role)

"""Read All Roles"""
@router.get('/roles', response_model = List[Role], status_code = 200)
def read_all_roles():
    return roleCrud.read_all(session)

"""Read Single Role"""
@router.get('/roles/{role_guid}', response_model = Role, status_code = 200)
def read_role(role_guid: str):
    return roleCrud.read(session, role_guid)

"""Update a Role"""
@router.put('/roles/{role_guid}', response_model = Role, status_code=status.HTTP_200_OK)
def update_role(role_guid:str, role: Role):
    return roleCrud.update(session, obj_id = role_guid, obj_in=role)

"""Delete a Role"""
@router.delete('/roles/{role_guid}', status_code = 200)
def delete_role(role_guid: str):
    return roleCrud.delete(session, id = role_guid)