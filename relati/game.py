from relati.gridboard import GridBoard
from relati.actions import placePiece
from relati.rules import enablePieces, disablePieces, revokePieces, getGameStatus
from relati.utils import printBoard
from relati.color import COLOR_RESET, COLOR_FG_RED, COLOR_FG_BLUE


class RelatiGame:
    def __init__(self, boardWidth, boardHeight):
        self.turn = 0
        self.isOver = False
        self.winner = -1
        self.board = GridBoard(boardWidth, boardHeight)
        self.rootGrids = [None] * 2

    def placePiece(self, x, y):
        symbol = self.turn % 2
        grid = self.board.getGridAt(x, y)
        isAllRootPlaced = self.turn >= 2
        isPlaced = placePiece(self.turn, grid, symbol)

        if not isPlaced:
            return

        if isAllRootPlaced:
            disablePieces(self.board)
            revokePieces(self.board)

            for rootGrid in self.rootGrids:
                enablePieces(rootGrid)
        else:
            self.rootGrids[self.turn] = grid

        self.turn += 1
        self.isOver, self.winner = getGameStatus(self.turn, self.board)
