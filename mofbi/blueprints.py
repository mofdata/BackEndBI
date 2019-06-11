from flask import Blueprint 
from flask_restful import Resource
from flask_restful import Api

from .resources import Organization 


organization_bp = Blueprint("organization", __name__)
api = Api(organization_bp)
api.add_resource(Organization, '/organizations')
