from dotenv import load_dotenv
from flask import Flask, request
import json
import os
import requests

load_dotenv()

app = Flask(__name__)

BUNGIE_URL = "https://www.bungie.net/Platform/Destiny2"


@app.route("/")
def index():
    return "Hello!"


@app.route("/manifest")
def manifest():
    response = requests.get(f"{BUNGIE_URL}/Manifest")
    response_json = response.json()

    print(response_json)

    return {"status_code": 200, "message": "Success", "data": response_json["Response"]}


@app.route("/destinyplayer/search")
def destiny_player_search():
    search_params = request.args.to_dict()

    headers = {"x-api-key": os.environ["X_API_KEY"]}
    data = json.dumps(
        {
            "displayName": search_params["display_name"],
            "displayNameCode": search_params["display_name_code"],
        }
    )

    response = requests.post(
        "https://www.bungie.net/Platform/Destiny2/SearchDestinyPlayerByBungieName/all/",
        data=data,
        headers=headers,
    )
    response_json = response.json()

    return {"status_code": 200, "message": "Success", "data": response_json["Response"]}
