import logging

import uvicorn


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    uvicorn.run(
        "manage_rest:app",
        host="127.0.0.1",
        port=8100,
    )
    logging.info('client started')