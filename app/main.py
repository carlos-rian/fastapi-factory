import os
import sys


sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from fastapi import FastAPI

from .module_one import one
from .module_two import two


def create_app():
    app = FastAPI()

    one.init_app(app=app)
    two.init_app(app=app)

    return app


# This is only for local development
if __name__ != "__main__":
    app = create_app()
