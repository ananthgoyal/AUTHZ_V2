from fastapi import FastAPI
from src import *
app = FastAPI()

@app.get('/')
def index():
    return {"message": "Authz V2"}
