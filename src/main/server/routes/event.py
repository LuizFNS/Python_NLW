from flask import Blueprint, jsonify, request

event_route_bp = Blueprint("event_route", __name__)

from src.http_types.http_response import HttpResponse
from src.http_types.http_request import HttpRequest

@event_route_bp.route("/event", methods=["POST"])
def create_new_event():
    Http_Request =  HttpRequest(body=request.json)
    Http_Response = HttpResponse(body={"estou":"aqui"}, status_code = 201)

    return jsonify(Http_Response.body),Http_Response.status_code

