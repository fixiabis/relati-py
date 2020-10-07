from relati.game import RelatiGame
from relati.utils import printBoard, clearScreen
from relati.color import COLOR_FG_RED, COLOR_FG_BLUE, COLOR_RESET

game = RelatiGame(9, 9)

while True:
    clearScreen()
    printBoard(game.board)

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
    ), end="   \b\b\b")

    coor = input().upper()
    x = ord(coor[0]) - 65
    y = int(coor[1:]) - 1
    game.placePiece(x, y)
