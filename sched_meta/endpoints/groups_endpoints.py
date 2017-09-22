import flask

bp = flask.Blueprint("groups_endpoints", __name__)


@bp.route("/create")
def create():
    return "Hello world"
