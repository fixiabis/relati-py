import re, json
from relati_perf.rules import isRelatiPlaceable, reEnablePieces
from relati_perf.actions import placePiece
from relati_perf.game import RelatiGame
from relati_perf.utils import printBoard, clearScreen
from relati_perf.color import COLOR_FG_RED, COLOR_FG_BLUE, COLOR_RESET
from relati_perf.evaluations import cachedPlayersPoints, evaluatePlayerNextStep

game = RelatiGame(9, 9)

cachedPlayersPointsDictFile = open("./cachedPoints.json", "r")
prevCachedPlayersPoints = eval(cachedPlayersPointsDictFile.read())
cachedPlayersPoints.update(prevCachedPlayersPoints)
cachedPlayersPointsDictFile.close()

while True:
    symbol = game.turn % 2
    clearScreen()
    printBoard(game.board, symbol)

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
        [COLOR_FG_RED, COLOR_FG_BLUE][symbol] +
        ["O", "X"][symbol] +
        COLOR_RESET
    ), end="    \b\b\b\b")

    gridOfHighestPoints = evaluatePlayerNextStep(game.board, symbol, 2)

    if gridOfHighestPoints is not None:
        game.placePiece(gridOfHighestPoints.x, gridOfHighestPoints.y)
        print(chr(gridOfHighestPoints.x) + str(gridOfHighestPoints.y + 1))
        continue

    coor = input().upper()

    if coor in ["EXIT", "QUIT", "Q"]:
        break

    isValidCoor = re.search("^[A-Z][0-9]+$", coor) != None

    if not isValidCoor:
        continue

    x = ord(coor[0]) - 65
    y = int(coor[1:]) - 1
    game.placePiece(x, y)

cachedPlayersPointsDictFile = open("./cachedPoints.json", "w")
cachedPlayersPointsDictText = json.dumps(cachedPlayersPoints)
cachedPlayersPointsDictFile.write(cachedPlayersPointsDictText)
cachedPlayersPointsDictFile.close()
