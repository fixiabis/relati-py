from relati.rules import isPlaceable, isRelatiPlaceable
from relati.types import toRelatiRepeater


def placePiece(turn, grid, symbol):
    isAllRootPlaced = turn >= 2

    isGridPlaceable = (
        grid is not None and
        isPlaceable(grid) and
        (not isAllRootPlaced or isRelatiPlaceable(grid, symbol))
    )

    if not isGridPlaceable:
        return False

    grid.body = symbol

    if isAllRootPlaced:
        grid.body = toRelatiRepeater(grid.body)

    return True
