from pydantic_core import Url
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from private import *

SQLALCHEMY_DATABASE_URL =  db_url

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True )

SessionLocal = sessionmaker( bind=engine)

Base = declarative_base()
