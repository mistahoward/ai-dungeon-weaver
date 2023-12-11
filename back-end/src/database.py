import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL") or ""
print(DATABASE_URL)
engine = create_engine(DATABASE_URL, echo=False, future=True)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
