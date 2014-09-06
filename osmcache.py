from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from credentials import POSTGRES_USERNAME, POSTGRES_PASSWORD, POSTGRES_DBNAME

d = {'NAME': POSTGRES_USERNAME,
     'PASSWORD': POSTGRES_PASSWORD,
     'DBNAME': POSTGRES_DBNAME}

engine = create_engine('postgresql://{NAME}:{PASSWORD}@localhost:5432/{DBNAME}'.format(**d))
session = sessionmaker(bind=engine)()


def create():
    from models import Base
    Base.metadata.create_all(engine)
