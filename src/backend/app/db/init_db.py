from session import Base, engine
from src.backend.app.models.Role import Role

Base.metadata.create_all(engine)