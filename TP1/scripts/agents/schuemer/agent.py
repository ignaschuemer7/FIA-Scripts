import numpy as np

BEST_POSITIONS = [[0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0],
                [0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0],
                [0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0],
                [0, 0, 0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0, 0, 0],
                [0, 0, 0, 0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2, 0, 0, 0],
                [0, 0, 0, 0.2, 0.4, 0.6, 0.6, 0.6, 0.6, 0.6, 0.4, 0.2, 0, 0, 0],
                [0, 0, 0, 0.2, 0.4, 0.6, 0.8, 0.8, 0.8, 0.6, 0.4, 0.2, 0, 0, 0],
                [0, 0, 0, 0.2, 0.4, 0.6, 0.8, 1.0, 0.8, 0.6, 0.4, 0.2, 0, 0, 0],
                [0, 0, 0, 0.2, 0.4, 0.6, 0.8, 0.8, 0.8, 0.6, 0.4, 0.2, 0, 0, 0],
                [0, 0, 0, 0.2, 0.4, 0.6, 0.6, 0.6, 0.6, 0.6, 0.4, 0.2, 0, 0, 0],
                [0, 0, 0, 0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2, 0, 0, 0],
                [0, 0, 0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0, 0, 0],
                [0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0],
                [0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0],
                [0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0]]

class SchuemerAgent ():
    def __init__(self):
        self.currBoard = Board(np.zeros((15, 15)))
        self.rating = 0

    def action(self, board):
        if not np.any(board): 
            board[7][7] = 1
            self.currBoard.doMovements(board)
            # print("Selection. Posible moves:", len(self.currBoard.getPerimeterMovements()))
            return 7*15 + 7
        self.currBoard.doMovements(board)
        move = self.selectMovement()
        # print("Selection. Posible moves:", len(self.currBoard.getPerimeterMovements()))
        return move[0]*15 + move[1]
    
    def selectMovement(self):
        alpha = float('-inf')
        beta = float('inf')
        node_value = float('-inf')
        for mov in self.currBoard.getPerimeterMovements():
            newBoard = self.currBoard.copy()
            board = self.currBoard.board.copy()
            board[mov] = 1
            newBoard.doMovements(board)
            value = alpha_beta(newBoard, 1, alpha, beta, False, mov)
            if value > node_value:
                node_value = value
                move = mov
        return move
    
    def name(self):
        return {'nombre': 'Ignacio', 'apellido': 'Schuemer', 'legajo': 34575}
    
    def __str__(self):
        return 'Chirimbolo'


def alpha_beta(board, depth, alpha, beta, maximizingPlayer, move):
    if depth == 0 or board.isTerminal():
        return heuristicValue(board, maximizingPlayer, move)
    if maximizingPlayer:
        value = float('-inf')
        for mov in board.getPerimeterMovements():
            newBoard = board.copy()
            board.board[mov] = 1
            newBoard.doMovements(board.board.copy())
            value = max(value, alpha_beta(newBoard, depth-1, alpha, beta, False, mov))
            if alpha >= beta:
                break
            alpha = max(alpha, value)
        return value
    else:
        value = float('inf')
        for mov in board.getPerimeterMovements():
            newBoard = board.copy()
            board.board[mov] = -1
            newBoard.doMovements(board.board.copy())
            value = min(value, alpha_beta(newBoard, depth-1, alpha, beta, True, mov))
            if alpha >= beta:
                break
            beta = min(beta, value)
        return value
    
class Board():
    "class to know the state of the board, last movements, and the perimeter movements"
    def __init__(self, board):
        self.board = board
        self.lastMovements = []
        self.allowedMovements = set()
        self.lastPerimeterAdded = set()

    def copy(self):
        newBoard = Board(self.board.copy())
        newBoard.lastMovements = self.lastMovements.copy()
        newBoard.allowedMovements = self.allowedMovements.copy()
        newBoard.lastPerimeterAdded = self.lastPerimeterAdded.copy()
        return newBoard

    def getHeuristicValue(self):
        return heuristicValue(self.board)

    def getBoard(self):
        return self.board
    
    def isPosInsideBoard(self, i, j):
        return i >= 0 and i < self.board.shape[0] and j >= 0 and j < self.board.shape[1]
    
    def doMovements(self, board):
        if np.array_equal(board, self.board):
            return
        newMovements = np.argwhere(board != self.board)
        addMov = set()
        relativePositions = [(-1, -1), (-1, 0), (-1, 1),(0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in newMovements:
            self.lastMovements.append((i[0], i[1]))
            if (i[0], i[1]) in self.allowedMovements:
                self.allowedMovements.remove((i[0], i[1]))
        for i in newMovements:
            for rp in relativePositions:
                pos = (i[0]+rp[0], i[1]+rp[1])
                if self.isPosInsideBoard(pos[0], pos[1]) and pos not in self.allowedMovements and pos not in self.lastMovements:
                    addMov.add(pos)
        self.allowedMovements = self.allowedMovements.union(addMov)
        self.board = board
        self.lastPerimeterAdded = addMov
        # print("new movements:", newMovements)
        # print("Movements:", len(self.lastMovements))


    
    def getPerimeterMovements(self):
        return self.allowedMovements
    
    def isPosEmpty(self, i, j):
        return self.board[i][j] == 0
    
    def isTerminal(self):
        if len(self.allowedMovements) == 0:
            return True
        return False
    
def heuristicValue(board, player, pos):
    "Returns the heuristic value of the board"
    " define if the position is near to another of a same player is good"
    
    #the best position is the center of the board and it has best value
    #We snip the board in vectors of 5 elements and we check if there is a 1 or -1 in the vector
    #The line wich has more 1 or -1 is the best line
    if player:
        player = 1
    else:
        player = -1
    value = 0
    # print(board.board)
    value+=np.where(board.board[pos[0],pos[1]-4:pos[1]+4]==player,player,0).sum()
    value+=np.where(board.board[pos[0]-4:pos[0]+4:,pos[1]]==player,player,0).sum()
    value+=np.where(board.board.diagonal(pos[1]-pos[0])==player,player,0).sum()
    value+=np.where(np.fliplr(board.board).diagonal(board.board.shape[1]-pos[1]-1-pos[0])==player,player,0).sum()
    #si esta contiguo a una ficha mia sumo 1
    relativePositions = [(-1, -1), (-1, 0), (-1, 1),(0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for rp in relativePositions:
        posr = (pos[0]+rp[0], pos[1]+rp[1])
        if board.isPosInsideBoard(posr[0], posr[1]) and board.board[posr[0], posr[1]] == player:
            if player == 1:
                value += 3
            else:
                value -= 3

    return value


        