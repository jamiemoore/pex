#!/usr/bin/env python3
import os

from flask import Flask, make_response

app = Flask(__name__)
app.config.from_object("src.pex.config.Config")
app.config.from_envvar("COMMIT_SHA", True)


def checkhealth():
    """
    Check the health of the service
    """
    status = True
    # Check the config
    cfg_list = ["VERSION", "COMMIT_SHA", "DESC"]
    for cfg in cfg_list:
        if cfg not in app.config:
            app.logger.error("can't find config item %s", cfg)
            status = False
        elif not app.config[cfg]:
            app.logger.error("config item %s is empty", cfg)
            status = False
    return status


@app.route("/health", methods=["GET"])
def healthcheck():
    health = {"health": "sad"}
    response_code = 503
    if checkhealth():
        health["health"] = "happy"
        response_code = 200
    res = make_response(health, response_code)
    return res


@app.route("/meta", methods=["GET"])
def metadata():
    meta = {}
    meta["version"] = app.config["VERSION"]
    meta["description"] = app.config["DESC"]
    meta["lastcommitsha"] = app.config["COMMIT_SHA"]

    return meta


@app.route("/", methods=["GET"])
def root():
    return "hello world"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 4040)))
