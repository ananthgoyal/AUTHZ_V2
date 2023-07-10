import models
from schemas.Role import Role
from schemas.Persistent import Persistent
from schemas.Permission import Permission
from fastapi import FastAPI, Request, Depends, Form, status, HTTPException, APIRouter
from fastapi.encoders import jsonable_encoder
from db.session import Base, engine
from db.session import SessionLocal
from repositories.PermissionRepository import PermissionRepository
from typing import List


session = SessionLocal()
router = APIRouter()
permCrud = PermissionRepository()


"""Create a Permission"""
@router.post('/permissions', status_code = status.HTTP_201_CREATED)
def create_permission(permission: Permission):
    return permCrud.create(session, obj_in=permission)

"""Read all Permissions"""
@router.get('/permissions', response_model = List[Permission], status_code = 200)
def read_all_permissions():
    return permCrud.read_all(session)

"""Read Single Permission"""
@router.get('/permissions/{perm_guid}', response_model = Permission, status_code = 200)
def read_permission(perm_guid: str):
    return permCrud.read(session, perm_guid)

"""Update a Permission"""
@router.put('/permissions/{perm_guid}', response_model = Permission, status_code=status.HTTP_200_OK)
def update_permission(perm_guid:str, perm: Permission):
    return permCrud.update(session, obj_id = perm_guid, obj_in=perm)

"""Delete a Permission"""
@router.delete('/permissions/{perm_guid}')
def delete_permission(perm_guid: str):
    return permCrud.delete(session, id = perm_guid)