from fastapi import FastAPI


def create_app() -> FastAPI:
    application = FastAPI()
    register_routers(application)
    return application


def register_routers(app: FastAPI) -> None:
    from .apps.users import router as users_router
    from .apps.auths import router as auths_router

    app.include_router(users_router)
    app.include_router(auths_router)
