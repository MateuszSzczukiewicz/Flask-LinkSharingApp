from flask import (
    Blueprint,
    jsonify,
    request,
)
from .db import get_db

bp = Blueprint("links", __name__, url_prefix="/links")


@bp.route("/<int:user_id>", methods=["GET"])
def get_all_links(user_id):
    user = get_user(user_id)


@bp.route("/create", methods=["POST"])
def create():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON data."}), 415

    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"error": "Invalid JSON data."}), 400

    user_id = data.get("user_id")
    platform = data.get("platform")
    url = data.get("url")
    db = get_db()

    if not user_id:
        return jsonify({"error": "User_id is required."}), 400
    elif not platform:
        return jsonify({"error": "Platform is required."}), 400
    elif not url:
        return jsonify({"error": "Url is required."}), 400

    try:
        db.execute(
            "INSERT INTO links (user_id, platforma, url) VALUES (?, ?, ?)",
            (user_id, platform, url),
        )
        db.commit()
        return jsonify({"message": "Link created successfully."}), 201
    except db.IntegrityError:
        return jsonify({"error": "Failed to create link."}), 409
