# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


USER_NAME = "docker"
PASSWD = "docker"
HOST="192.168.0.16:3306"
DB_NAME = "getter_db"

DATABASE = f'mysql://{USER_NAME}:{PASSWD}@{HOST}/{DB_NAME}?charset=utf8'

Engine = create_engine(DATABASE, encoding="utf-8", echo=True)

session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=Engine))

Base = declarative_base()
Base.query = session.query_property()