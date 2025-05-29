import argparse
import os
from typing import List

from bip import Bip

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
tags: dict[str, int] = {}

instructions = []
for line in code:
    # Remove comments
    if line.startswith("#"):
        code.pop(lineIndex)
        continue

    # Register tags addresses
    if line.endswith(":"):
        tagName = line[:-1]
        tags[tagName] = lineIndex
        continue

    instructions.append(line)
    lineIndex += 1

# Assemble code
for line in instructions:
    (command, param) = line.split(" ")
