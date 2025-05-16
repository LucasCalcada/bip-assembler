commands = {"HLT": 0, "STO": 1, "LD": 2}

codeInstructions = []
compiled = []

with open("./code.txt", "r") as f:
    lineIndex = 0
    tags = {}
    codeInstructions = f.read().split("\n")

for line in codeInstructions:
    print(f"Parsing line: {line}")
    if line == "":
        print("Skipping empty line")
        continue

    if line.startswith("//"):
        print(f"Skipping comment: {line[2:]}")
        continue

    if line.endswith(":"):
        tags[line[:-1]] = lineIndex
        continue

    command = line.split(" ")[0]

    if command == "HLT":
        compiled.append(f"{str(hex(lineIndex)).upper()[2:]} : 0000")
        lineIndex += 1
        continue

    param = line.split(" ")[1]
    if command not in commands.keys():
        raise SyntaxError(f"Command '{command}' not found")

    if param in tags.keys():
        param = tags[param]

    compiled.append(
        f"{str(hex(lineIndex)).upper()[2:]} : {commands[command]}{param:03}"
    )
    lineIndex += 1

print("\n".join(compiled))
