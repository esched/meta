import logging
from wsgiref import simple_server

from flask import Flask

from esched_meta import db
from esched_meta.db import db_session
from esched_meta.endpoints.groups_endpoints import groups_bp

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger("main")

app = Flask(__name__)

app.register_blueprint(groups_bp, url_prefix="/api/v1/groups")


@app.teardown_appcontext
def shutdown_session(exception=None):
    """
    Closes SQLAlchemy session after request is processed
    """
    db_session.remove()


if __name__ == '__main__':
    db.init_db()
    logger.info("Starting debug server on http://127.0.0.1:8080")
    debug_server = simple_server.make_server('127.0.0.1', 8080, app)
    debug_server.serve_forever()
