import requests

from app import requestor

URL: str = "http://localhost:8080"


def test_send_request():
    resp: requests.Response = requestor.send_request(
        "get",
        URL,
        auth=None,
        headers={"Accept": "application/json"},
        body=None,
        params=None,
        kwargs={"verify": False, "timeout": 5},
    )

    assert resp.status_code == 200
