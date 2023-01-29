"""Application module."""

from fastapi import FastAPI

from .containers import Container
from .endpoints import router


def create_app() -> FastAPI:
    container = Container()
    # container.config.giphy.api_key.from_env("GIPHY_API_KEY")

    _app = FastAPI()
    _app.container = container
    _app.include_router(router)
    return _app


app = create_app()
