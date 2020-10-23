from relati.rules import isExists, isPlaceable, isRelatiPlaceable
from relati.types import toRelatiRepeater


def placePiece(grid, symbol, isAllRootPlaced):
    isGridPlaceable = (
        isExists(grid) and
        isPlaceable(grid) and
        (not isAllRootPlaced or isRelatiPlaceable(grid, symbol))
    )

    if not isGridPlaceable:
        return False

    if isAllRootPlaced:
        grid.body = toRelatiRepeater(symbol)
    else:
        grid.body = symbol

    return True
