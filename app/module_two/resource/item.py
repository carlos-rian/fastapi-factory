from fastapi import APIRouter


def init_app(_router: APIRouter) -> None:
    router = APIRouter()

    @router.get("/item")
    def get_item():
        return {"message": "Hello World - Module Two - Item"}

    # inlude the router on the app with the prefix - factory pattern
    _router.include_router(router=router)
