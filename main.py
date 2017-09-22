from flask import Flask
from wsgiref import simple_server
import logging

from esched_meta.endpoints.groups_endpoints import groups_bp

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

app.register_blueprint(groups_bp, url_prefix="/api/v1/groups")

if __name__ == '__main__':
    logging.info("Starting debug server on 127.0.0.1:0080")
    debug_server = simple_server.make_server('127.0.0.1', 8080, app)
    debug_server.serve_forever()
