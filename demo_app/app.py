from sanic import Sanic

from demo_app.blueprints import bp

app = Sanic('demo_application')
app.blueprint(bp)
