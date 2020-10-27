from relati_perf.relatiboard import RelatiBoard
from relati_perf.actions import placePiece
from relati_perf.rules import getGameStatus, reEnablePieces


class RelatiGame:
    def __init__(self, boardWidth, boardHeight):
        self.turn = 0
        self.isOver = False
        self.winner = -1
        self.board = RelatiBoard(boardWidth, boardHeight)
        self.isAllRootPlaced = False

    def placePiece(self, x, y):
        symbol = self.turn % 2
        grid = self.board.getGridAt(x, y)

        if grid is None:
            return

        isPlaced = placePiece(grid, symbol, self.isAllRootPlaced)

        if not isPlaced:
            return

        if self.isAllRootPlaced:
            reEnablePieces(self.board)
        else:
            self.isAllRootPlaced = self.turn == 2 - 1

        self.turn += 1
        self.isOver, self.winner = getGameStatus(self.turn, self.board)
