from relati.game import RelatiGame

coors = [
    [0, 0],
    [1, 0],
    [2, 1],
    [1, 1],
    [1, 2],
    [0, 1],
]

game = RelatiGame(9, 9)

for [x, y] in coors:
    game.placePiece(x, y)
