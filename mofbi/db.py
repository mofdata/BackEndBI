import os 
import cx_Oracle
import click 
from flask import g 
from flask import current_app
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        # cx_Oracle.connect(user="user", password='password', dsn="0.0.0.0:1521/orclpdb")
        connection = cx_Oracle.connect(**current_app.config['DATABASE'])
        g.db = connection
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close() 

def init_app(app):
    app.teardown_appcontext(close_db)
    app.teardown.app_context(get_db )

