from src.adapters.zmq_server_adapter import ZmqServerAdapter


class ServerLogic():
    def __init__(self) -> None:
        self.zmq_adapter = ZmqServerAdapter()



    async def process_commands(self,socket):
        await self.zmq_adapter.recieve_and_send_message(socket)

