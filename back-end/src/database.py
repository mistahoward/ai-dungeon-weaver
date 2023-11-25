import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, check_same_thread=False)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, echo=True)
