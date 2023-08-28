import numpy as np

class Board():
    "class to know the state of the board, last movements, and the perimeter movements"
    def __init__(self, SIZE):
        self.SIZE = SIZE
        self.board = np.zeros((SIZE, SIZE), dtype=int)
        self.lastMovements = [] #list of tuples, it can be changed to a set
        self.allowedMovements = set()
        self.lastPerimeterAdded = set()
        self.heuristicValue = 0
        self.player = 1

    def getBoard(self):
        return self.board
    
    def isPosInsideBoard(self, i, j):
        return i >= 0 and i < self.SIZE and j >= 0 and j < self.SIZE
    
    def updateBoard(self, board):
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
    print(board.board)
    value+=np.where(board.board[pos[0],:]==player,player,0).sum()
    value+=np.where(board.board[:,pos[1]]==player,player,0).sum()
    value+=np.where(board.board.diagonal(pos[1]-pos[0])==player,player,0).sum()
    value+=np.where(np.fliplr(board.board).diagonal(board.board.shape[1]-pos[1]-1-pos[0])==player,player,0).sum()
    #si esta contiguo a una ficha mia sumo 1
    relativePositions = [(-1, -1), (-1, 0), (-1, 1),(0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for rp in relativePositions:
        posr = (pos[0]+rp[0], pos[1]+rp[1])
        print(board.board[posr[0], posr[1]])
        if board.isPosInsideBoard(posr[0], posr[1]) and board.board[posr[0], posr[1]] == player:
            if player == 1:
                value += 10
            else:
                value -= 10

    if player == 1:
        return value
    else:
        return -value
    
# #testing
board = Board(15)
newBoard = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 1, -1, 0, 0 ,0 ,0 ,0 ,0], 
                        [0, 0, 0, 0, 0, 0, 1, 1, 1, -1, 0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0, 0, 1, 1, 1, -1, 0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0 ,0 ,0 ,0 ,0]])

                      
board.updateBoard(newBoard)
pos = (6, 9)
print("pos:", pos, "value:", heuristicValue(board, False, pos))
# print(board.getPerimeterMovements())
# print(len(board.getPerimeterMovements()))


board.updateBoard(np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0 ,0 ,0 ,0 ,0], 
                            [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0 ,0 ,0 ,0 ,0],
                            [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0 ,0 ,0 ,0 ,0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0]]))

# print(board.getPerimeterMovements())
# print(len(board.getPerimeterMovements()))

# newBoard = np.array([[0, 0, 0, 0, 0],
#                     [0, 0, 0, 0, 0],
#                     [0, 0, 1, 1, 1],
#                     [0, 0, 1, 1, 1],
#                     [0, 0, 0, 0, 1]])
# board.updateBoard(newBoard)
# print(board.allowedMovements)

    
# print(heuristicValue(board, True, (1,1)))



    
    