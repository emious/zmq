import asyncio
import threading

import zmq
import zmq.asyncio

from time import sleep

from src.logics.server_logic import ServerLogic

class ServerProcess():
    def __init__(self) -> None:
        self.logic = ServerLogic()

    def server_process(self):
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind("tcp://127.0.0.1:5559")
        for i in range(3):
            thread = threading.Thread(target=self._start, args=(socket,))
            thread.start()

    def _start(self, socket):
        while True:
            sleep(1)
            asyncio.run(self.logic.process_commands(socket))
