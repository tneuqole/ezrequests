from typing import Any

import requests


def send_request(
    method: str,
    url: str,
    auth: Any,
    headers: dict,
    body: dict,
    params: dict,
    **kwargs: dict,
) -> requests.Response:
    return getattr(requests, method.lower())(
        url, auth=auth, headers=headers, data=body, params=params, **kwargs
    )
