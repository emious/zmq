import json

import zmq
import zmq.asyncio
from src.models.dtos import CommandInputDTOV1, CommandOutputDTOV1

class ZmqClientAdapter:

    async def send_and_recieve_massage(self, input_dto: CommandInputDTOV1 | CommandOutputDTOV1):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://127.0.0.1:5559")
        socket.send(
            input_dto.model_dump_json(exclude_defaults=True, exclude_none=True, exclude_unset=True).encode('utf-8'))
        message = socket.recv()
        socket.close()
        context.term()
        return json.loads(message)


