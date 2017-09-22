import logging

from flask import Flask

from esched_meta import db
from esched_meta.db import db_session
from esched_meta.endpoints import groups_endpoints, users_endpoints

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger("main")

app = Flask(__name__)

app.register_blueprint(groups_endpoints.bp, url_prefix="/api/v1/groups")
app.register_blueprint(users_endpoints.bp, url_prefix="/api/v1/users")


@app.teardown_appcontext
def shutdown_session(exception=None):
    """
    Closes SQLAlchemy session after request is processed
    """
    db_session.remove()


if __name__ == '__main__':
    db.init_db()
    app.run("127.0.0.1", 8080, debug=True)
