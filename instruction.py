from dataclasses import dataclass

from utils import intToHex


@dataclass
class InstructionParams:
    constantParam: bool
    addressParam: bool
    tagParam: bool


class Instruction:
    def __init__(
        self, commandName: str, address: int, paramOptions: InstructionParams
    ) -> None:
        self.name = commandName
        self.address = intToHex(address)

    def parseInstruction(self, param):
        return f"{self.address}{param.zfill(3)}"
