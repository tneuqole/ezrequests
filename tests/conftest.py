import threading

import pytest

from local import mockserver


@pytest.fixture(scope="session", autouse=True)
def server():
    s: threading.Thread = threading.Thread(target=mockserver.run, daemon=True)
    yield s.start()
