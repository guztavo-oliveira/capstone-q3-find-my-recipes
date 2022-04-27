from flask import Blueprint
from app.controllers import feed_controller

bp = Blueprint("feed", __name__, url_prefix="/feed")

bp.get("")(feed_controller.get_publications)
bp.post("")(feed_controller.post_a_publication)
bp.patch("/<post_id>")(feed_controller.update_a_publication)
bp.delete("/<post_id>")(feed_controller.delete_a_publication)