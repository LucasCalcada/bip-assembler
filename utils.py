def intToHex(val: int) -> str:
    hexVal = hex(val)
    hexVal = hexVal.upper()
    hexVal = hexVal[2:]
    return hexVal
