import pytest
import ujson

from demo_app.exceptions import InvalidArgument

"""
pytest tests using fixtures
"""


@pytest.fixture(scope='module', autouse=True)
def setup_fixture():
    print(f"Doing setup logic of module {__name__}")
    yield
    print(f"Doing teardown logic of module {__name__}")


def test_division_view_success_int(sanic_application):
    sanic_client = sanic_application.test_client

    request_data = {
        'dividend': 15,
        'divisor': 3
    }

    response = sanic_client.post(
        '/api/v1/divide/',
        gather_request=False,
        # server_kwargs={},
        # used to inject additional arguments on app.run()
        # injecting empty dict will incur infinite loop on somewhere.

        debug=True,
        # params={},  # used on GET method to describe query parameter
        data=ujson.dumps(request_data)
    )

    assert response.status == 200
    assert response.json == {'answer': 5}


def test_division_view_success_double(sanic_application):
    sanic_client = sanic_application.test_client

    request_data = {
        'dividend': 15,
        'divisor': 7
    }

    response = sanic_client.post(
        '/api/v1/divide/',
        gather_request=False,
        # server_kwargs={},
        # used to inject additional arguments on app.run()
        # injecting empty dict will incur infinite loop on somewhere.

        debug=True,
        # params={},  # used on GET method to describe query parameter
        data=ujson.dumps(request_data)
    )

    assert response.status == 200
    assert 'answer' in response.json
    assert round(response.json['answer'], 2) == 2.14

def test_division_view_failure_invalid_data_type(sanic_application):
    sanic_client = sanic_application.test_client

    request_data = {
        'dividend': '15',
        'divisor': 7
    }

    response = sanic_client.post(
        '/api/v1/divide/',
        gather_request=False,
        # server_kwargs={},
        # used to inject additional arguments on app.run()
        # injecting empty dict will incur infinite loop on somewhere.

        debug=True,
        # params={},  # used on GET method to describe query parameter
        data=ujson.dumps(request_data)
    )

    assert response.status == InvalidArgument.status_code
    assert response.text == "Error: Both divisor or dividend should be provided as int."
    # string 'Error: ' prefixed from Sanic


def test_division_view_failure_dividend_not_provided(sanic_application):
    sanic_client = sanic_application.test_client

    request_data = {
        'divisor': 7
    }

    response = sanic_client.post(
        '/api/v1/divide/',
        gather_request=False,
        # server_kwargs={},
        # used to inject additional arguments on app.run()
        # injecting empty dict will incur infinite loop on somewhere.

        debug=True,
        # params={},  # used on GET method to describe query parameter
        data=ujson.dumps(request_data)
    )

    assert response.status == InvalidArgument.status_code
    assert response.text == "Error: Should provide dividend and divisor, 'dividend' is missing."


def test_division_view_failure_empty_argument_provided(sanic_application):
    sanic_client = sanic_application.test_client

    request_data = {}

    response = sanic_client.post(
        '/api/v1/divide/',
        gather_request=False,
        # server_kwargs={},
        # used to inject additional arguments on app.run()
        # injecting empty dict will incur infinite loop on somewhere.

        debug=True,
        # params={},  # used on GET method to describe query parameter
        data=ujson.dumps(request_data)
    )

    assert response.status == InvalidArgument.status_code
    assert response.text == "Error: Should provide dividend and divisor, 'dividend' is missing."


def test_division_view_failure_divisor_not_provided(sanic_application):
    sanic_client = sanic_application.test_client

    request_data = {
        'dividend': 15
    }

    response = sanic_client.post(
        '/api/v1/divide/',
        gather_request=False,
        # server_kwargs={},
        # used to inject additional arguments on app.run()
        # injecting empty dict will incur infinite loop on somewhere.

        debug=True,
        # params={},  # used on GET method to describe query parameter
        data=ujson.dumps(request_data)
    )

    assert response.status == InvalidArgument.status_code
    assert response.text == "Error: Should provide dividend and divisor, 'divisor' is missing."


def test_division_view_failure_zero_division(sanic_application):
    sanic_client = sanic_application.test_client

    request_data = {
        'dividend': 15,
        'divisor': 0
    }

    response = sanic_client.post(
        '/api/v1/divide/',
        gather_request=False,
        # server_kwargs={},
        # used to inject additional arguments on app.run()
        # injecting empty dict will incur infinite loop on somewhere.

        debug=True,
        # params={},  # used on GET method to describe query parameter
        data=ujson.dumps(request_data)
    )

    assert response.status == InvalidArgument.status_code
    assert response.text == "Error: Cannot divide by zero."
