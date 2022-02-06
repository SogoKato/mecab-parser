# -*- coding: utf-8 -*-
from dataclasses import asdict
from logging import DEBUG
import os

from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

from mecab_parser import MecabParserFactory


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


@app.route("/parse", methods=["POST"])
def parse():
    if not request.is_json:
        return jsonify({
            "ok": False,
            "code": 400,
            "name": "Invalid Content-Type",
            "description": "Content-Type must be application/json.",
        })
    content = request.get_json()
    if (
        content is None or
        not isinstance(content, dict) or
        "texts" not in content.keys() or
        not isinstance(content["texts"], list) or
        [x for x in content["texts"] if not isinstance(x, str)]
    ):
        return jsonify({
            "ok": False,
            "code": 400,
            "name": "Invalid JSON Format",
            "description": 'Valid JSON format is {"texts": ["Ipsum dolore eirmod autem et"]}',
        })
    parser = MecabParserFactory.create("mecab-ipadic-neologd")
    results = [[asdict(dc)for dc in parser(t)] for t in content["texts"]]
    return jsonify({"ok": True, "results": results})


@app.errorhandler(HTTPException)
def handle_exception(e):
    return jsonify({
        "ok": False,
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.logger.level = DEBUG
    app.run(host="0.0.0.0", port=port)
