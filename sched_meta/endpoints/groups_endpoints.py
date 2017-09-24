import uuid

import flask
from flask import request, abort, jsonify

from sched_meta.db import db_session
from sched_meta.models import User, Group

bp = flask.Blueprint("groups_endpoints", __name__)


@bp.route("/<int:group_id>", methods=["GET"])
def get(group_id):
    group = db_session.query(Group).get(group_id)  # type: Group
    if not group:
        abort(422, "Unknown group")
    return jsonify(group.as_json())


@bp.route("/create", methods=["PUT"])
def create():
    admin_id = request.form["admin_id"]
    admin = db_session.query(User).get(admin_id)

    if not admin:
        abort(422, "Unknown admin_id")

    title = request.form["title"]

    group = Group(admin, title)
    db_session.add(group)
    db_session.commit()

    return jsonify(group.as_json())


@bp.route("/<int:group_id>/rotateInviteCode", methods=["PATCH"])
def rotate_invite_code(group_id):
    group = db_session.query(Group).get(group_id)  # type: Group
    if not group:
        abort(422, "Unknown group")

    group.invite_code = str(uuid.uuid4())
    db_session.add(group)
    db_session.commit()

    return jsonify(group.as_json())
