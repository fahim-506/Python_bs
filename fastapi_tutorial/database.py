from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

db_url="postgresql://postgres:12345@localhost:5432/basic_db"
engine=create_engine(db_url)
Sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

