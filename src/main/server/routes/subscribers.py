from flask import Blueprint, jsonify, request

subs_route_bp = Blueprint("subs_route", __name__)

from src.validators.subscribers_creator_validator import subscribers_creator_validator

from src.http_types.http_request import HttpRequest

from src.controllers.subscribers.subscribers_creator import SubscribersCreator
from src.model.repositories.subscribers_repository import SubscribersRepository

@subs_route_bp.route("/subscriber", methods=["POST"])
def create_new_subs():
    subscribers_creator_validator(request)
    http_request =  HttpRequest(body=request.json)

    sub_repo = SubscribersRepository()
    sub_creator = SubscribersCreator(sub_repo)

    http_response = sub_creator.create(http_request)


    return jsonify(http_response.body),http_response.status_code

