import pytest
from sanic import Sanic

from demo_app.blueprints import bp


@pytest.fixture
def sanic_application():
    app = Sanic('test_demo_application')

    app.blueprint(bp)

    return app
