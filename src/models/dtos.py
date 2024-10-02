from pydantic import (
    StrictStr, BaseModel,
)


class CommandInputDTOV1(BaseModel):
    command_type: StrictStr
    command_name: StrictStr | None = None
    parameters: list[str] | None = None
    expression: StrictStr | None = None


class CommandOutputDTOV1(BaseModel):
    result: str
