from ssl import RAND_status
from flask import Response, json
from flask_restful import Resource
from flask_apispec.views import MethodResource
from flask_apispec import doc


class Rooms(MethodResource, Resource):
    @doc(description="Get all Rooms.", tags=["All Rooms"])
    def get(self):
        result = "Get all rooms"
        return result
