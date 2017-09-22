import flask

groups_bp = flask.Blueprint("groups_endpoints", __name__)


@groups_bp.route("/create")
def create():
    return "Hello world"
