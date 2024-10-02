from src.adapters.zmq_client_adapter import ZmqClientAdapter
from src.models.dtos import CommandInputDTOV1, CommandOutputDTOV1


class ClientLogic():
    def __init__(self) -> None:
        self.zmq_adapter = ZmqClientAdapter()

    async def command(self, input_dto: CommandInputDTOV1) -> CommandOutputDTOV1:
        result = await self.zmq_adapter.send_and_recieve_massage(input_dto)
        return CommandOutputDTOV1(**result)
