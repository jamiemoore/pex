#!/usr/bin/env python3
"""
PEX Application
"""
import os

from flask import Flask, make_response
from flask.logging import create_logger

app = Flask(__name__)
log = create_logger(app)
app.config.from_object("src.pex.config.Config")
app.config.from_envvar("COMMIT_SHA", True)


def check_app_health():
    """
    Check the health of the app
    """
    status = True
    # Check the config
    cfg_list = ["VERSION", "COMMIT_SHA", "DESC"]
    for cfg in cfg_list:
        if cfg not in app.config:
            log.error("can't find config item %s", cfg)
            status = False
        elif not app.config[cfg]:
            log.error("config item %s is empty", cfg)
            status = False
    return status


@app.route("/health", methods=["GET"])
def health_check():
    """
    Healthcheck Endpoint
    """
    health = {"health": "sad"}
    response_code = 503
    if check_app_health():
        health["health"] = "happy"
        response_code = 200
    return make_response(health, response_code)


@app.route("/meta", methods=["GET"])
def metadata():
    """
    Metadata Endpoint
    """
    meta = {}
    meta["version"] = app.config["VERSION"]
    meta["description"] = app.config["DESC"]
    meta["lastcommitsha"] = app.config["COMMIT_SHA"]

    return meta


@app.route("/", methods=["GET"])
def root():
    """
    Root Endpoint
    """
    return "hello world"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 4040)))
