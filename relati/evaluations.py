from relati.types import toRelatiRepeater
from relati.actions import placePiece
from relati.rules import isExists, isPlaceable, isRelatiPlaceable
from relati.routes import normalRoutes


def getPlaceableAreas(board):
    placeableAreas = []

    for grid in board.grids:
        if not isPlaceable(grid):
            continue

        isGridInArea = False

        for [[x, y]] in normalRoutes:
            nearbyGrid = grid.getGridTo(x, y)

            if not isExists(nearbyGrid) or not isPlaceable(nearbyGrid):
                continue

            for placeableArea in placeableAreas:
                if nearbyGrid in placeableArea:
                    placeableArea.append(grid)
                    isGridInArea = True
                    break

            if isGridInArea:
                break

        if not isGridInArea:
            placeableArea = [grid]
            placeableAreas.append(placeableArea)

    for placeableArea in placeableAreas:
        for otherPlaceableArea in placeableAreas:
            if otherPlaceableArea is placeableArea:
                continue

            isOtherPlaceableAreaShouldMerge = False

            for otherGrid in otherPlaceableArea:
                for [[x, y]] in normalRoutes:
                    nearbyOtherGrid = otherGrid.getGridTo(x, y)

                    if not isExists(nearbyOtherGrid) or not isPlaceable(nearbyOtherGrid):
                        continue

                    if nearbyOtherGrid in placeableArea:
                        isOtherPlaceableAreaShouldMerge = True
                        break

                if isOtherPlaceableAreaShouldMerge:
                    break

            if isOtherPlaceableAreaShouldMerge:
                placeableArea.extend(otherPlaceableArea)
                otherPlaceableArea.clear()

    placeableAreas = [
        placeableArea for placeableArea in placeableAreas if len(placeableArea) != 0]

    return placeableAreas


def evaluatePlayersPoints(board):
    placeableAreas = getPlaceableAreas(board)
    isPlaceableAreasForPlayers = [[False, False] for _ in placeableAreas]
    placeableGridsCountForPlayers = [0, 0]
    pointsForPlayers = [0, 0]

    for placeableAreaIndex in range(len(placeableAreas)):
        placeableArea = placeableAreas[placeableAreaIndex]

        for grid in placeableArea:
            for symbol in range(2):
                if isRelatiPlaceable(grid, symbol):
                    isPlaceableAreasForPlayers[placeableAreaIndex][symbol] = True
                    placeableGridsCountForPlayers[symbol] += 1

    for placeableAreaIndex in range(len(placeableAreas)):
        placeableArea = placeableAreas[placeableAreaIndex]
        isPlaceableAreaForPlayers = isPlaceableAreasForPlayers[placeableAreaIndex]

        if isPlaceableAreaForPlayers[0] and not isPlaceableAreaForPlayers[1]:
            pointsForPlayers[0] += len(placeableArea) * 9
        elif isPlaceableAreaForPlayers[1] and not isPlaceableAreaForPlayers[0]:
            pointsForPlayers[1] += len(placeableArea) * 9

    pointsForPlayers[0] += placeableGridsCountForPlayers[0]
    pointsForPlayers[1] += placeableGridsCountForPlayers[1]

    return pointsForPlayers


def evaluatePlayerPoints(symbol, board, depth, isPlayerTurn=True, alpha=-100000, beta=100000):
    if depth == 0:
        [oPoints, xPoints] = evaluatePlayersPoints(board)

        if symbol == 0:
            return oPoints - xPoints
        else:
            return xPoints - oPoints

    if isPlayerTurn:
        maxPlayerPoints = -100000

        for grid in board.grids:
            if not isPlaceable(grid) or not isRelatiPlaceable(grid, symbol):
                continue

            placePiece(grid, symbol, True)

            playerPoints = evaluatePlayerPoints(
                symbol, board, depth - 1, False, alpha, beta
            )

            maxPlayerPoints = max(maxPlayerPoints, playerPoints)
            alpha = max(alpha, maxPlayerPoints)

            grid.body = None

            if beta <= alpha:
                break

        return maxPlayerPoints
    else:
        minPlayerPoints = 100000

        for grid in board.grids:
            if not isPlaceable(grid) or not isRelatiPlaceable(grid, (symbol + 1) % 2):
                continue

            placePiece(grid, (symbol + 1) % 2, True)

            playerPoints = evaluatePlayerPoints(
                symbol, board, depth - 1, True, alpha, beta
            )

            minPlayerPoints = min(minPlayerPoints, playerPoints)
            beta = min(beta, minPlayerPoints)

            grid.body = None

            if beta <= alpha:
                break

        return minPlayerPoints
