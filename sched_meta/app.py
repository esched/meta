import logging

from flask import Flask

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
