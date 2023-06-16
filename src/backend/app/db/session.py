from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://ananth:password@localhost/test_1",
    echo = True
)

print('creating Base')
Base = declarative_base()


SessionLocal = sessionmaker(bind=engine)