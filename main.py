import falcon
from wsgiref import simple_server
import logging
from esched_meta.endpoints.groups import groups_api

app = falcon.API()

# app.(groups_api, "/groups")

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    logging.info("Starting debug server on 127.0.0.1:0080")
    debug_server = simple_server.make_server('127.0.0.1', 8080, app)
    debug_server.serve_forever()
