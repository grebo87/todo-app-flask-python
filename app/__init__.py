import os
import sqlalchemy
from yaml import load, Loader
from flask import Flask
import pathlib

app = Flask(__name__)

def init_connection_engine():
    path = pathlib.Path(__file__).parent.absolute()
    variables = load(open(path/'env.yaml'), Loader=Loader)

    pool = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL(
            drivername="mysql+pymysql",
            username=variables['MYSQL_USER'],
            password=variables['MYSQL_PASSWORD'],
            database=variables['MYSQL_DB'],
            host= variables['MYSQL_HOST'],
        )
    )

    return pool

db = init_connection_engine()

from app import routes
