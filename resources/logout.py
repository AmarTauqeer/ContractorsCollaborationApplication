from flask import Response
from flask_apispec.views import MethodResource
from flask_restful import Resource
from flask_apispec import doc
from flask_login import login_user, login_required, logout_user


class Logout(MethodResource, Resource):
    @doc(description="Logout page.", tags=["Logout page"])
    @login_required
    def get(self):
        logout_user()
        return Response("logout successfully")
