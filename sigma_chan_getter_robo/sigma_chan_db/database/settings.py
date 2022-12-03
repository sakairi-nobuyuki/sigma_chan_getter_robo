# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import os

DB_TYPE = os.getenv("GETTER_DB_TYPE")
DB_USER_NAME = os.getenv("GETTER_DB_USER_NAME")
DB_PASSWD = os.getenv("GETTER_DB_PASSWD")
DB_HOST = os.getenv("GETTER_DB_HOST")
DB_NAME = os.getenv("GETTER_DB_NAME")

DATABASE = f'{DB_TYPE}://{DB_USER_NAME}:{DB_PASSWD}@{DB_HOST}/{DB_NAME}?charset=utf8'

Engine = create_engine(DATABASE, encoding="utf-8", echo=True)

session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=Engine))

Base = declarative_base()
Base.query = session.query_property()