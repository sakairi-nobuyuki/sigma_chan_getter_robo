# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


USER_NAME = "sigma_chan"
PASSWD = "yz22714n"
HOST = "localhost"
#HOST = "127.0.0.1"
DB_NAME = "getter_db"

DATABASE = f'mysql://{USER_NAME}:{PASSWD}@{HOST}/{DB_NAME}?charset=utf8'

Engine = create_engine(DATABASE, encoding="utf-8", echo=True)

session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=Engine))

Base = declarative_base()
Base.query = session.query_property()