from flask import Response
from flask_restful import Resource, request
from flask_apispec.views import MethodResource
from flask_apispec import doc
from db import get_user
from flask_login import login_user, current_user


class Login(MethodResource, Resource):
    @doc(description="Login page.", tags=["Login page"])
    def post(self):
        if request.method == "POST":
            if current_user.is_authenticated:
                return Response("already logged in")

            data = request.get_json()
            username = data["_id"]
            password_input = data["password"]
            user = get_user(username)

            if user and user.check_password(password_input):
                login_user(user)
                return Response("successfull")
            else:
                return Response("unsuccessfull")
