from relati.types import RELATI_RECEIVER
from relati_perf.actions import placePiece
from relati_perf.rules import isPlaceable, isRelatiPlaceable, reEnablePieces


def isPlaceableOrReceiver(grid):
    return isPlaceable(grid) or grid.status == RELATI_RECEIVER


def getUnmergedPlaceableAreas(board):
    unmergedPlaceableAreas = []

    for grid in board.grids:
        if not isPlaceableOrReceiver(grid):
            continue

        isGridInArea = False

        for nearbyGrid in grid.nearbyGrids:
            if not isPlaceableOrReceiver(nearbyGrid):
                continue

            for placeableArea in unmergedPlaceableAreas:
                if nearbyGrid in placeableArea:
                    placeableArea.append(grid)
                    isGridInArea = True
                    break

            if isGridInArea:
                break

        if not isGridInArea:
            placeableArea = [grid]
            unmergedPlaceableAreas.append(placeableArea)

    return unmergedPlaceableAreas


def getPlaceableAreas(board):
    unmergedPlaceableAreas = getUnmergedPlaceableAreas(board)

    for placeableArea in unmergedPlaceableAreas:
        for otherPlaceableArea in unmergedPlaceableAreas:
            if otherPlaceableArea is placeableArea:
                continue

            isOtherPlaceableAreaMerged = False

            for grid in otherPlaceableArea:
                for nearbyGrid in grid.nearbyGrids:
                    if isPlaceableOrReceiver(nearbyGrid) and nearbyGrid in placeableArea:
                        placeableArea.extend(otherPlaceableArea)
                        otherPlaceableArea.clear()
                        isOtherPlaceableAreaMerged = True
                        break

                if isOtherPlaceableAreaMerged:
                    break

    placeableAreas = [
        placeableArea for placeableArea in unmergedPlaceableAreas if len(placeableArea) != 0
    ]

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


def evaluatePlayerPoints(board, symbol, depth, isPlayerTurn=True, alpha=-100000, beta=100000):
    if depth == 0:
        [oPoints, xPoints] = evaluatePlayersPoints(board)

        if symbol == 0:
            return oPoints - xPoints
        else:
            return xPoints - oPoints

    if isPlayerTurn:
        maxPlayerPoints = -100000

        for grid in board.grids:
            if not isRelatiPlaceable(grid, symbol):
                continue

            placePiece(grid, symbol, True)
            reEnablePieces(board)

            playerPoints = evaluatePlayerPoints(
                board, symbol, depth - 1, False, alpha, beta
            )

            maxPlayerPoints = max(maxPlayerPoints, playerPoints)
            alpha = max(alpha, maxPlayerPoints)

            grid.symbol = None
            reEnablePieces(board)

            if beta <= alpha:
                break

        return maxPlayerPoints
    else:
        minPlayerPoints = 100000

        for grid in board.grids:
            if not isRelatiPlaceable(grid, (symbol + 1) % 2):
                continue

            placePiece(grid, (symbol + 1) % 2, True)
            reEnablePieces(board)

            playerPoints = evaluatePlayerPoints(
                board, symbol, depth - 1, True, alpha, beta
            )

            minPlayerPoints = min(minPlayerPoints, playerPoints)
            beta = min(beta, minPlayerPoints)

            grid.symbol = None
            reEnablePieces(board)

            if beta <= alpha:
                break

        return minPlayerPoints
