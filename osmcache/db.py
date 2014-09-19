import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

URI_ENV_KEY = "OSM_DB_URI"

if URI_ENV_KEY not in os.environ:
    raise Exception("Missing ENV: %s" % URI_ENV_KEY)

engine = create_engine(os.environ[URI_ENV_KEY])
