

from fastapi import APIRouter

from src.logics.client_logic import ClientLogic
from src.models.dtos import CommandOutputDTOV1, CommandInputDTOV1

public_router_v1 = APIRouter()
logic = ClientLogic()

@public_router_v1.post(
    "/command",
    response_model=CommandOutputDTOV1,
)
async def command(input_dto: CommandInputDTOV1) -> CommandOutputDTOV1:
    return await logic.command(input_dto)


