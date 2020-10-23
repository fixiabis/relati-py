import os
import sys

from relati.color import (
    COLOR_RESET,
    COLOR_FG_BRIGHT_BLACK,
    COLOR_BG_RED,
    COLOR_FG_RED,
    COLOR_BG_BLUE,
    COLOR_FG_BLUE,
)

from relati.types import (
    RELATI_SYMBOL_O,
    RELATI_SYMBOL_X,
    isRelatiSymbol,
    isRelatiLauncher,
    isRelatiRepeater,
)


def printBoard(board):
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

            if grid.body != None:
                if isRelatiSymbol(grid.body, RELATI_SYMBOL_O):
                    gridSymbol = "O"

                    if isRelatiLauncher(grid.body):
                        color = COLOR_BG_RED
                    elif isRelatiRepeater(grid.body):
                        color = COLOR_FG_RED

                elif isRelatiSymbol(grid.body, RELATI_SYMBOL_X):
                    gridSymbol = "X"

                    if isRelatiLauncher(grid.body):
                        color = COLOR_BG_BLUE
                    elif isRelatiRepeater(grid.body):
                        color = COLOR_FG_BLUE

            print(" %s |" % (color + gridSymbol + COLOR_RESET), end="")

        print()


def clearScreen():
    if sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
        os.system("clear")
    elif sys.platform.startswith("win32") or sys.platform.startswith("cygwin"):
        os.system("cls")
