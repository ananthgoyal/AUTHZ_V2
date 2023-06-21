from session import Base, engine
from src.backend.app.models.Role import Role
from src.backend.app.models.Permission import Permission

Base.metadata.create_all(engine)