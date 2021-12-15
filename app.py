from functools import wraps
import ssl
from flask import Flask
from db import get_user
from flask_restful import Api
from apispec import APISpec
from flask_apispec.extension import FlaskApiSpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_cors import CORS
from dotenv import load_dotenv
from flask_login import LoginManager
from resources.login import Login
from resources.logout import Logout

# contract resources
from resources.rooms import Rooms
from user import User


# flask app
app = Flask(__name__)
# load_dotenv()
app.secret_key = "amar"
login_manager = LoginManager()
login_manager.init_app(app)
# cors enable for swagger-editor
CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)
# swagger configuration
app.config.update(
    {
        "APISPEC_SPEC": APISpec(
            title="Contractors Collaboration Application",
            version="v01",
            plugins=[MarshmallowPlugin()],
            openapi_version="2.0.0",
        ),
        "APISPEC_SWAGGER_UI_URL": "/",
    }
)


@login_manager.user_loader
def load_user(username):
    return get_user(username)


docs = FlaskApiSpec(app)

api.add_resource(Login, "/api/login/")
docs.register(Login)

api.add_resource(Logout, "/api/logout/")
docs.register(Logout)

api.add_resource(Rooms, "/api/agents/rooms/")
docs.register(Rooms)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
