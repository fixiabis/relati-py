RELATI_SYMBOL = 0b00000001
RELATI_STATUS = 0b00000110
RELATI_SYMBOL_O = 0b00000000
RELATI_SYMBOL_X = 0b00000001
RELATI_LAUNCHER = 0b00000000
RELATI_REPEATER = 0b00000010
RELATI_RECEIVER = 0b00000100
RELATI_DECEASED = 0b00000110
RELATI_REPEATABLE = 0b00000100


def getRelatiStatus(status):
    return status & RELATI_STATUS


def getRelatiSymbol(symbol):
    return symbol & RELATI_SYMBOL


def isRelatiStatus(status, relatiStatus):
    return getRelatiStatus(status) == relatiStatus


def isRelatiLauncher(status):
    return isRelatiStatus(status, RELATI_LAUNCHER)


def isRelatiRepeater(status):
    return isRelatiStatus(status, RELATI_REPEATER)


def isRelatiReceiver(status):
    return isRelatiStatus(status, RELATI_RECEIVER)


def isRelatiDeceased(status):
    return isRelatiStatus(status, RELATI_DECEASED)


def isRelatiSymbol(symbol, relatiSymbol):
    return getRelatiSymbol(symbol) == relatiSymbol


def isRelatiSymbolEqual(symbolA, symbolB):
    return getRelatiSymbol(symbolA) == getRelatiSymbol(symbolB)


def isRelatiRepeatable(status):
    return status & RELATI_REPEATABLE == RELATI_LAUNCHER


def toRelatiStatus(status, relatiStatus):
    return status & ~RELATI_STATUS | relatiStatus


def toRelatiLauncher(status):
    return toRelatiStatus(status, RELATI_LAUNCHER)


def toRelatiRepeater(status):
    return toRelatiStatus(status, RELATI_REPEATER)


def toRelatiReceiver(status):
    return toRelatiStatus(status, RELATI_RECEIVER)


def toRelatiDeceased(status):
    return toRelatiStatus(status, RELATI_DECEASED)
