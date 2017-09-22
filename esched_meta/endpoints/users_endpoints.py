from flask import request, Blueprint, jsonify
from flask import abort

from esched_meta.db import db_session
from esched_meta.models import User

bp = Blueprint(__name__, __name__)


@bp.route("/byTgInfo")
def get_user_by_tg_id():
    user = None

    if "id" in request.args:
        tg_id = request.args["id"]
        user = db_session.query(User).filter_by(tg_id=tg_id).first()
        if user is None:
            user = User()
            user.tg_id = tg_id
    elif "username" in request.args:
        tg_username = request.args["username"]
        user = db_session.query(User).filter_by(tg_username=tg_username).first()

    if user is None:
        abort(404, "Cannot find specified user")

    if "allow_update" in request.args and request.args["allow_update"].lower() == "true":
        if "username" in request.args:
            user.tg_username = request.args["username"]

    db_session.add(user)
    db_session.commit()

    return jsonify(user.as_json())
