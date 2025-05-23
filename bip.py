import os
import yaml

from instruction import Instruction, InstructionParams

CONFIG_FILE_PATH = "./config.yaml"


class Bip:
    def __init__(self) -> None:
        self.__config = {}
        self.instructions: dict[str, Instruction] = {}

        self.load_config()
        self.load_instructions(self.__config["instructions"])

    def load_config(self):
        if not os.path.exists(CONFIG_FILE_PATH):
            raise FileNotFoundError("Config file not found")

        with open(CONFIG_FILE_PATH, "r") as config:
            self.__config = yaml.safe_load(config.read())

    def load_instructions(self, instructions):
        for i in instructions:
            name = i["name"]
            addr = i["address"]
            paramConfig = InstructionParams(
                i["constParam"], i["addressParam"], i["tagParam"]
            )
            instruction = Instruction(name, addr, paramConfig)
            self.instructions[name] = instruction
