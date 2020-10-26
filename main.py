import re
from relati.evaluations import evaluatePlayersPoints
from relati.game import RelatiGame
from relati.utils import printBoard, clearScreen
from relati.color import COLOR_FG_RED, COLOR_FG_BLUE, COLOR_RESET

game = RelatiGame(9, 9)

while True:
    clearScreen()
    printBoard(game.board, game.turn % 2)

    if game.isOver:
        isDraw = game.winner == -1

        if not isDraw:
            print("winner is %s, game over" % (
                [COLOR_FG_RED, COLOR_FG_BLUE][game.winner] +
                ["O", "X"][game.winner] +
                COLOR_RESET
            ))
        else:
            print("draw, game over")

        break

    print("turn to %s: " % (
        [COLOR_FG_RED, COLOR_FG_BLUE][game.turn % 2] +
        ["O", "X"][game.turn % 2] +
        COLOR_RESET
    ), end="    \b\b\b\b")

    coor = input().upper()

    if coor in ["EXIT", "QUIT", "Q"]:
        break
    
    isValidCoor = re.search("^[A-Z][0-9]+$", coor) != None

    if not isValidCoor:
        continue

    x = ord(coor[0]) - 65
    y = int(coor[1:]) - 1
    game.placePiece(x, y)
