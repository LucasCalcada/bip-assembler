from dataclasses import dataclass

from tagmanager import TagManager
from utils import intToHex


tags = TagManager.instance()


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

    @staticmethod
    def parse_param(param: str) -> str:
        if param.startswith("0b"):
            param = param[2:]
            return intToHex(int(param, 2))
        elif param.startswith("0x"):
            param = param[2:]
            return intToHex(int(param, 16))
        elif param.isdigit():
            return intToHex(int(param))
        else:
            return intToHex(tags.getTag(param))

    def parseInstruction(self, param):
        return f"{self.address}{param.zfill(3)}"
