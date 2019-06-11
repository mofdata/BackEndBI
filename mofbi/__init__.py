import os 
import json 
from flask import Flask 
from flask import Blueprint
from flask_restful import Api, Resource 
import config


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    api = Api(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE={
            "user": config.DB_USER,
            "password": config.DB_PASSWORD,
            "dsn": config.ORACLE_DB_CONNECT,
        },
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Flask api 
    api = Api(app)

    # Add the resources. 
    from .resources.organization import OrganizationResource
    from .resources.budget import ExpenditureResource
    from .resources.budget import BudgetResource

    # Urls
    api.add_resource(OrganizationResource, '/api/v1/orgs')
    api.add_resource(ExpenditureResource, '/api/v1/expenditure')
    api.add_resource(BudgetResource, '/api/v1/budget')

    return app