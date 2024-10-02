import json
import logging
import subprocess
from src.models.dtos import CommandInputDTOV1, CommandOutputDTOV1


class ZmqServerAdapter:
    async def recieve_and_send_message(self,socket):
        message = socket.recv()
        command = CommandInputDTOV1(**json.loads(message.decode()))
        result =  await self.handle_command(command)
        socket.send(
            result.model_dump_json(exclude_defaults=True, exclude_none=True, exclude_unset=True).encode('utf-8'))


    async def handle_command(self,command):
        if command.command_type == 'os':
            command_name = command.command_name
            parameters = command.parameters
            try:
                result = subprocess.check_output([command_name] + parameters, text=True,timeout=10)
                return CommandOutputDTOV1(result=result)

            except subprocess.TimeoutExpired:
                return CommandOutputDTOV1(result='timeout: input commad took more than 10 sec to process')
            except Exception as e:
                logging.error(e)
                return CommandOutputDTOV1(result=str(e))


        if command.command_type == 'compute':
            expression = command.expression
            try:
                result = eval(expression)
                return CommandOutputDTOV1(result=str(result))
            except Exception as e:
                logging.error(e)
                return CommandOutputDTOV1(result=str(e))
