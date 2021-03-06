import connexion
from flask_cors import CORS

# Create the application instance
from .exceptions import HttpErrorBaseException

app = connexion.FlaskApp(__name__, specification_dir='./')
app.add_api('swagger.yml', options={
    "swagger_ui": True,
    "swagger_url": "/swagger-ui",
})
CORS(app.app)
app.app.config.from_pyfile('config.py')
app.add_error_handler(HttpErrorBaseException, lambda it: it.to_json_response())
