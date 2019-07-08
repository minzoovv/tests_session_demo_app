import os

from demo_app.app import app


try:
    port = int(os.environ['DEMO_APPLICATION_PORT'])
except KeyError:
    port = 8000


if __name__ == "__main__":
    app.run(port=port)
