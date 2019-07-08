from sanic import Blueprint

from demo_app import views

bp = Blueprint('demo_app_blueprint', url_prefix='/api/v1')

bp.add_route(views.DivideTwoNumbersView.as_view(), '/divide/', strict_slashes=True)
