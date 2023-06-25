from fastapi import FastAPI
from db.session import Base, engine
from routers import Role, Permission

app = FastAPI()

app.include_router(Role.router)
app.include_router(Permission.router)

@app.get('/')
def index():
    return {"message": "Authz V2"}

def init_db():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    init_db()