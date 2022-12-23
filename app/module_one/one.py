from fastapi import FastAPI, APIRouter
from .resource import item


def init_app(app: FastAPI) -> None:
    router = APIRouter(tags=["Module One"])

    # include the new resource to item
    item.init_app(_router=router)

    # inlude the router on the app with the prefix - factory pattern
    app.include_router(router=router, prefix="/api/v1/module_one")
