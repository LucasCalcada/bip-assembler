import argparse
import os
from typing import List

from bip import Bip
from tagmanager import TagManager
from utils import intToHex

parser = argparse.ArgumentParser()
parser.add_argument("code", type=str, help="Code file path")

args = parser.parse_args()
processor = Bip()


if not os.path.exists(args.code):
    raise FileNotFoundError("Code file not found")

code: List[str] = []
with open(args.code, "r") as f:
    codeText = f.read()
    code = codeText.split("\n")

# Initial parse
code.remove("")

lineIndex = 0
tags = TagManager.instance()

instructions = []
for line in code:
    # Remove empty lines
    if line == "":
        code.pop(lineIndex)
        continue

    # Remove comments
    if line.startswith("#"):
        code.pop(lineIndex)
        continue

    # Register tags addresses
    if line.endswith(":"):
        tagName = line[:-1]
        tags.addTag(tagName, lineIndex)
        continue

    instructions.append(line)
    lineIndex += 1

# Assemble code
with open("output.cdm", "w+", encoding="UTF-8") as f:
    output = []
    for i, line in enumerate(instructions):
        (command, param) = line.split(" ")
        instr = processor.parse_instruction(command, param)
        output.append(f"{intToHex(i)} : {instr}\n")
    f.writelines(output)
