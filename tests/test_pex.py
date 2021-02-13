import json


def test_root_endpoint(app, client):
    """
    GIVEN a simple, small, operable web-style API or service provider
    WHEN the root endpoint is requested
    THEN it responds "hello world"
    """
    expected = "hello world"
    res = client.get("/")
    assert expected == res.get_data(as_text=True)


def test_health_endpoint_good(app, client):
    """
    GIVEN a simple, small, operable web-style API or service provider in good health
    WHEN the health endpoint is requested
    THEN it responds with response code 200
    """
    app.config["COMMIT_SHA"] = "aaaaaaa"
    res = client.get("/health")
    assert res.status_code == 200


def test_health_endpoint_bad(app, client):
    """
    GIVEN a simple, small, operable web-style API or service provider in bad health
    WHEN the the health endpoint is requested
    THEN it responds with response code 503
    """
    app.logger.disabled = True
    app.config["COMMIT_SHA"] = ""
    res = client.get("/health")
    assert res.status_code == 503
    app.logger.disabled = False


def test_metadata_endpoint(app, client):
    """
    GIVEN a simple, small, operable web-style API or service provider in bad health
    WHEN the the health endpoint is requested
    THEN it responds with meta data such as
    {
        "version": "1.0",
        "description": "description goes here",
        "lastcommitsha": "aaaaaaa",
    }
    """
    expected = {
        "version": "1.0.0",
        "description": "description goes here",
        "lastcommitsha": "aaaaaaa",
    }

    app.config["VERSION"] = expected["version"]
    app.config["DESC"] = expected["description"]
    app.config["COMMIT_SHA"] = expected["lastcommitsha"]

    res = client.get("/meta")
    json_response = {}

    # Check the json will decode
    try:
        json_response = json.loads(res.get_data(as_text=True))
    except Exception:
        raise Exception("failed to decode json from metadata")

    # Check we have all the keys we expect
    assert expected.keys() == json_response.keys()

    # Check the values match what we expect
    assert expected.items() == json_response.items()
