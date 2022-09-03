# coding: utf-8

#from settings import Engine, Base
#from getter_robo_db.settings import Engine, Base
from database.settings import Engine, Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class JobId(Base):
    __tablename__ = "job_id"
    job_id = Column("job_id", String(512), primary_key=True)
    tweet_id = Column("tweet_id", String(512), nullable=False)
    modified_at = Column("modified", DateTime, default=datetime.now(), nullable=False)
    created_at = Column("created", DateTime, default=datetime.now(), nullable=False)
