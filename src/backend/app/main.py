from db.session import SessionLocal
from fastapi import FastAPI, Request, Depends, Form, status, HTTPException
from fastapi.encoders import jsonable_encoder
from db.session import Base, engine
from models.Role import Role
from typing import List
from crud.crud_role import CRUD_Role

app = FastAPI()
session = SessionLocal()

@app.get('/')
def index():
    return {"message": "Authz V2"}


@app.post('/roles', status_code = status.HTTP_201_CREATED)
def passed():
    pass

"""Read All Roles"""
@app.get('/roles', response_model = List[Role], status_code = 200)
def get_all_roles():
    pass



def init_db():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    init_db()