import logging

from fastapi import FastAPI
from fastapi.security import HTTPBearer

from starlette.middleware.cors import CORSMiddleware

from src.process.server_process import ServerProcess

bearer_scheme = HTTPBearer()

base_responses = {
    400: {"description": "Invalid Input Arguments"},
    504: {"description": "Request Process Timed Out"},
    404: {"description": "Requested Resource Not Found"},
    409: {"description": "Requested Entity Already Exists or Faced a conflict"},
    429: {"description": "Too Many Requests Sent"},
    503: {"description": "Service Temporary Unavailable"},
    501: {"description": "Requested Method Not Implemented"},
    500: {"description": "Internal Server Error"},
}


def _create_app():
    app = FastAPI()
    _add_routers(app)
    _add_middleware(app)
    return app


def _add_middleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )


def _add_routers(app):
    _add_public_router(app)


def _add_public_router(app):
    from src.services.v1.public_services_v1 import public_router_v1
    responses = base_responses
    app.include_router(public_router_v1, prefix="/api/v1", responses=responses)





app = _create_app()

@app.on_event("startup")
async def startup_event():
    # Start the ZeroMQ server
    logging.info('server started')
    ServerProcess().server_process()

