from relati.gridboard import GridBoard
from relati.actions import placePiece
from relati.rules import enablePieces, disablePieces, getGameStatus


class RelatiGame:
    def __init__(self, boardWidth, boardHeight):
        self.turn = 0
        self.isOver = False
        self.winner = -1
        self.board = GridBoard(boardWidth, boardHeight)
        self.rootGrids = []
        self.isAllRootPlaced = False

    def placePiece(self, x, y):
        symbol = self.turn % 2
        grid = self.board.getGridAt(x, y)
        isPlaced = placePiece(grid, symbol, self.isAllRootPlaced)

        if not isPlaced:
            return

        if self.isAllRootPlaced:
            disablePieces(self.board)
            
            for grid in self.rootGrids:
                enablePieces(grid)
        else:
            self.rootGrids.append(grid)
            self.isAllRootPlaced = self.turn == 2 - 1

        self.turn += 1
        self.isOver, self.winner = getGameStatus(self.turn, self.board)
