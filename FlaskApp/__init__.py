from flask import Flask
# from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
# Always use relative import for custom module
from .package.module import MODULE_VALUE


app = Flask(__name__)

# @app.route("/")
# def index():
#     return (
#         "Try /hello/Chris for parameterized Flask route.\n"
#         "Try /module for module import guidance"
#     )
# CORS(app)

# app_register_blueprint(request_api.get_blueprint())

@app.route("/hello/<name>", methods=['GET'])
def hello(name: str):
    return f"hello {name}"

@app.route("/module")
def module():
    return f"loaded from FlaskApp.package.module = {MODULE_VALUE}"

SWAGGER_URL = '/swagger'  # URL for exposing Swagger UI (without trailing '/')
API_URL = 'FlaskApp/static/swagger.json'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint)

app.register_blueprint(request_api.get_blueprint())

if __name__ == "__main__":
    app.run()