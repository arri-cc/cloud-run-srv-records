import flask
import pytest

import main


@pytest.fixture(scope="module")
def app():
    return flask.Flask(__name__)


def test_hello_get(app):
    with app.test_request_context(args={'name': 'yellow'}):
        res = main.test_lookup(flask.request)
        assert 'yellow' in res
