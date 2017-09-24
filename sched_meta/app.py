import logging

from flask import Flask, jsonify
from werkzeug.exceptions import default_exceptions, HTTPException

from sched_meta.db import db_session
from sched_meta.endpoints import groups_endpoints, users_endpoints

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

app.register_blueprint(groups_endpoints.bp, url_prefix="/api/v1/groups")
app.register_blueprint(users_endpoints.bp, url_prefix="/api/v1/users")


@app.teardown_appcontext
def shutdown_session(exception=None):
    """
    Closes SQLAlchemy session after request is processed
    """
    db_session.remove()


@app.errorhandler(Exception)
def make_json_error(ex):

    if isinstance(ex, HTTPException):
        status_code = ex.code
        resp_data = {
            "code": status_code,
            "message": f"{ex.description}"
        }

        if status_code == 400 and ex.args:
            resp_data["message"] = f"Required param was not provided: {ex.args[0]}"
    else:
        status_code = 500
        resp_data = {
            "code": status_code,
            "message": str(ex),
            "exception": str(type(ex))
        }

    response = jsonify(resp_data)
    response.status_code = status_code
    return response


for code in default_exceptions.keys():
    app.register_error_handler(code, make_json_error)
