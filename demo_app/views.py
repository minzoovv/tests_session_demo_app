from sanic.response import json
from sanic.views import HTTPMethodView

from demo_app.exceptions import InvalidArgument


class DivideTwoNumbersView(HTTPMethodView):
    async def post(self, request, *args, **kwargs):
        """
        return quotient of two numbers

        :param request: payload should contain:
        {
            'dividend': int,
            'divisor': int
        }

        :return: json object
        {
            'answer': int
        } with status_code = 200

        :raises:
        ** 400 Bad Request **
            KeyError: client does not provide dividend or divisor
            TypeError: client provided all numbers but the type is not int. - This API does not cast type automatically.
            ZeroDivisionError: client requested to divide by zero
        """
        try:
            dividend = request.json['dividend']
            divisor = request.json['divisor']

            if not isinstance(dividend, int) or not isinstance(divisor, int):
                raise TypeError
        except KeyError as e:
            raise InvalidArgument(f"Should provide dividend and divisor, {str(e)} is missing.")
        except TypeError:
            raise InvalidArgument("Both divisor or dividend should be provided as int.")

        try:
            return json({'answer': dividend / divisor}, status=200)
        except ZeroDivisionError:
            raise InvalidArgument("Cannot divide by zero.")
