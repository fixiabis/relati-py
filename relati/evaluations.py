from relati.rules import isPlaceable, isRelatiPlaceable


def evaluatePlayerPoints(symbol, board):
    points = 0
    opponentSymbol = (symbol + 1) % 2

    isGridPlaceable = map(isPlaceable, board.grids)

    isGridRelatiPlaceableForSymbol = map(
        lambda grid: isRelatiPlaceable(grid, symbol),
        board.grids
    )

    isGridRelatiPlaceableForOpponentSymbol = map(
        lambda grid: isRelatiPlaceable(grid, opponentSymbol),
        board.grids
    )

    def getPoint(isGridPlaceable, isGridRelatiPlaceableForSymbol, isGridRelatiPlaceableForOpponentSymbol):
        if not isGridPlaceable:
            return 0

        if isGridRelatiPlaceableForSymbol and isGridRelatiPlaceableForOpponentSymbol:
            return 1

        if isGridRelatiPlaceableForSymbol and not isGridRelatiPlaceableForOpponentSymbol:
            return 5

        if not isGridRelatiPlaceableForSymbol and isGridRelatiPlaceableForOpponentSymbol:
            return -5

        return 0

    points = sum(map(
        getPoint,
        isGridPlaceable,
        isGridRelatiPlaceableForSymbol,
        isGridRelatiPlaceableForOpponentSymbol
    ))

    return points
