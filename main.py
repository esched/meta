from sched_meta import db
from sched_meta.app import app

import logging

logging.getLogger("sqlalchemy.engine.base.Engine").propagate = False

logger = logging.getLogger("main")

if __name__ == '__main__':
    logger.info("Initializing database schema")
    db.init_db()
    logger.info("Starting debug server")
    app.run("127.0.0.1", 8080, debug=True)
