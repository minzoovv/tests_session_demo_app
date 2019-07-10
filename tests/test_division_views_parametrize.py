import pytest
import ujson

from demo_app.exceptions import InvalidArgument


@pytest.fixture(scope='module', autouse=True)
def setup_fixture():
    print(f"Doing setup logic of module {__name__}")
    yield
    print(f"Doing teardown logic of module {__name__}")


@pytest.mark.parametrize("dividend, divisor, expected_response", [
    (15, 3, {'answer': 5}), (15, 7, {'answer': round(15 / 7, 2)})
])
def test_division_view_success(dividend, divisor, expected_response, sanic_application):
    sanic_client = sanic_application.test_client

    request_data = {
        'dividend': dividend,
        'divisor': divisor
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
    assert response.json == expected_response


@pytest.mark.parametrize("dividend, divisor, expected_error_decription", [
    ('15', 7, 'Error: Both divisor or dividend should be provided as int.'),
    (None, 7, "Error: Should provide dividend and divisor, 'dividend' is missing."),
    (None, None, "Error: Should provide dividend and divisor, 'dividend' is missing."),
    (15, None, "Error: Should provide dividend and divisor, 'divisor' is missing."),
    (15, 0, "Error: Cannot divide by zero.")
])
def test_division_view_failure(dividend, divisor, expected_error_decription, sanic_application):
    sanic_client = sanic_application.test_client

    request_data = {}
    if dividend is not None:
        request_data['dividend'] = dividend
    if divisor is not None:
        request_data['divisor'] = divisor

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
    assert response.text == expected_error_decription
