from flask_restful import Resource
from flask_restful import Api 
from flask import Blueprint 


class OrganizationResource(Resource):
    def get(self):
        return {"hello": "world"}
    