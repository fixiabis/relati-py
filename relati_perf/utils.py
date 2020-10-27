import os
import sys
from relati_perf.evaluations import evaluatePlayersPoints, evaluatePlayerPoints
from relati_perf.actions import placePiece
from relati_perf.rules import isRelatiPlaceable, reEnablePieces

from relati_perf.color import (
    COLOR_RESET,
    COLOR_FG_BRIGHT_BLACK,
    COLOR_BG_RED,
    COLOR_FG_RED,
    COLOR_BG_BLUE,
    COLOR_FG_BLUE,
)

from relati_perf.types import (
    RELATI_SYMBOL_O,
    RELATI_SYMBOL_X,
    RELATI_LAUNCHER,
    RELATI_REPEATER,
)


def printBoard(board, symbol):
    if board.height < 10:
        print("|   |", end="")
    else:
        print("|    |", end="")

    for x in range(board.width):
        print(" %c |" % chr(x + 65), end="")

    print()

    for y in range(board.height):
        if board.height < 10:
            print("| %d |" % (y + 1), end="")
        else:
            print("| %2d |" % (y + 1), end="")

        for x in range(board.width):
            grid = board.getGridAt(x, y)
            color = COLOR_FG_BRIGHT_BLACK
            gridSymbol = " "

            if grid.symbol == RELATI_SYMBOL_O:
                gridSymbol = "O"

                if grid.status == RELATI_LAUNCHER:
                    color = COLOR_BG_RED
                elif grid.status == RELATI_REPEATER:
                    color = COLOR_FG_RED

            elif grid.symbol == RELATI_SYMBOL_X:
                gridSymbol = "X"

                if grid.status == RELATI_LAUNCHER:
                    color = COLOR_BG_BLUE
                elif grid.status == RELATI_REPEATER:
                    color = COLOR_FG_BLUE

            elif isRelatiPlaceable(grid, symbol):
                gridSymbol = "."
                color = COLOR_FG_RED if symbol == 0 else COLOR_FG_BLUE

            print(" %s |" % (color + gridSymbol + COLOR_RESET), end="")

        print()

    # print(evaluatePlayersPoints(board))


def clearScreen():
    if sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
        os.system("clear")
    elif sys.platform.startswith("win32") or sys.platform.startswith("cygwin"):
        os.system("cls")
