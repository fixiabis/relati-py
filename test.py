from relati.game import RelatiGame
from relati.utils import printBoard, clearScreen
from relati.color import COLOR_FG_RED, COLOR_FG_BLUE, COLOR_RESET

clearScreen()
game = RelatiGame(9, 9)

coors = [
    *[[x, y] for y in range(9) for x in [0, 8, 1, 7, 2, 6, 3, 5]],
    *[[4, y] for y in range(9)],
    [-1, -1]
]

for coor in coors:
    print("\033[0;0H", end="")
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

    [x, y] = coor

    print("turn to %s: " % (
        [COLOR_FG_RED, COLOR_FG_BLUE][game.turn % 2] +
        ["O", "X"][game.turn % 2] +
        COLOR_RESET
    ), end="   \b\b\b%s" % (chr(x + 65) + str(y + 1)))

    game.placePiece(x, y)
