from relati_perf.rules import isPlaceable, isRelatiable
from relati_perf.types import RELATI_LAUNCHER, RELATI_REPEATER


def placePiece(grid, symbol, isAllRootPlaced):
    if not isPlaceable(grid):
        return False

    if isAllRootPlaced:
        if isRelatiable(grid, symbol):
            grid.symbol = symbol
            grid.status = RELATI_REPEATER
            return True
    else:
        grid.symbol = symbol
        grid.status = RELATI_LAUNCHER
        return True

    return False
