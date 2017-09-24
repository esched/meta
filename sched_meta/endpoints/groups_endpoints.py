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
        abort(404, "Unknown group")
    return jsonify(group.as_json())


@bp.route("/<int:group_id>/members", methods=["GET"])
def get_members(group_id):
    group = db_session.query(Group).get(group_id)  # type: Group
    if not group:
        abort(404, "Unknown group")

    result = list(map(lambda u: u.as_json(), group.users))
    return jsonify(result)


@bp.route("/byInviteCode/<code>", methods=["GET"])
def get_by_invite_code(code):
    group = db_session.query(Group).filter(Group.invite_code == code).first()  # type: Group
    if not group:
        abort(422, "Unknown group")
    return jsonify(group.as_json())


@bp.route("/<int:group_id>", methods=["DELETE"])
def delete(group_id):
    group = db_session.query(Group).get(group_id)  # type: Group
    if not group:
        abort(422, "Unknown group")

    db_session.delete(group)
    db_session.commit()
    return "OK"


@bp.route("/<int:group_id>/join", methods=["POST"])
def join(group_id):
    group = db_session.query(Group).get(group_id)  # type: Group
    if not group:
        abort(422, "Unknown group")

    user = db_session.query(User).get(request.form["user_id"])  # type: User
    if not user:
        abort(422, "Unknown user")

    user.groups.append(group)
    db_session.add(user)
    db_session.commit()

    return "OK"


@bp.route("/<int:group_id>/leave", methods=["POST"])
def leave(group_id):
    group = db_session.query(Group).get(group_id)  # type: Group
    if not group:
        abort(422, "Unknown group")

    user = db_session.query(User).get(request.form["user_id"])  # type: User
    if not user:
        abort(422, "Unknown user")

    if group in user.groups:
        user.groups.remove(group)
        db_session.add(user)
        db_session.commit()

    return "OK"


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
