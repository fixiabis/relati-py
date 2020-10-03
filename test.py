from relati.gridboard import GridBoard
from relati.actions import placePiece
from relati.rules import enablePieces, disablePieces, getGameStatus
from relati.utils import printBoard

from relati.color import (
    COLOR_RESET,
    COLOR_FG_RED,
    COLOR_FG_BLUE,
)

turn = 0
board = GridBoard(9, 9)
rootGrids = [None] * 2

for y in range(9):
    for x in [0, 8, 1, 7, 2, 6, 3, 5]:
        symbol = turn % 2
        grid = board.getGridAt(x, y)
        isPlaced = placePiece(turn, grid, symbol)

        if not isPlaced:
            continue

        if turn >= 2:
            disablePieces(board)

            for rootGrid in rootGrids:
                enablePieces(rootGrid)
        else:
            rootGrids[turn] = grid

        turn += 1
        printBoard(board)
        isOver, winner = getGameStatus(turn, board)

        if isOver:
            if winner != -1:
                print("game over, winner: %s" % (
                    [COLOR_FG_RED, COLOR_FG_BLUE][winner] +
                    ["O", "X"][winner] +
                    COLOR_RESET
                ))
            else:
                print("game over, draw")
        else:
            print()

for y in range(9):
    symbol = turn % 2
    grid = board.getGridAt(4, y)
    isPlaced = placePiece(turn, grid, symbol)

    if not isPlaced:
        continue

    if turn >= 2:
        disablePieces(board)

        for rootGrid in rootGrids:
            enablePieces(rootGrid)
    else:
        rootGrids[turn] = grid

    turn += 1
    printBoard(board)
    isOver, winner = getGameStatus(turn, board)

    if isOver:
        if winner != -1:
            print("game over, winner: %s" % (
                [COLOR_FG_RED, COLOR_FG_BLUE][winner] +
                ["O", "X"][winner] +
                COLOR_RESET
            ))
        else:
            print("game over, draw")
    else:
        print()
