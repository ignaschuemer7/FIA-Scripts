import numpy as np
from time import perf_counter	

KNOWN_MOVES = {' 1 1 1 1 1 ': 40000010,
               ' 0 1 1 1 1 0 ': 399980,
               ' 0 1 1 1 1 -1 ': 50000,
               ' -1 1 1 1 1 0 ': 50000,
               ' 1 1 0 1 1 ': 50000,
               ' 0 1 1 1 0 ': 29998,
               ' -1 1 1 1 0 0 ': 14987,
               ' -1 1 1 1 0 0 ': 14987,
               ' 0 0 1 1 1 -1 ': 14987,
               ' 0 1 0 1 1 0 ': 6995,
               ' 0 1 1 0 1 0 ': 6995,
               ' -1 1 0 1 1 0 ': 2990,
               ' -1 1 1 0 1 0 ': 2990,
               ' 0 1 0 1 1 -1 ': 2987,
               ' 0 1 1 0 1 -1 ': 2987,
               ' 0 0 1 1 0 ': 490, 
               ' 0 1 1 0 0 ': 490, 
               ' 0 1 1 0 0 -1 ': 490,
               ' -1 1 1 0 0 0 ': 395, 
               ' 0 0 0 1 1 -1 ': 395,
               ' 0 1 0 1 0 ': 295,
                ' -1 1 0 1 0 0 ': 38,
                ' 0 0 1 0 1 -1 ': 38,
            }   
deep = 2
boardValues = {}

class SchuemerAgent ():
    def __init__(self):
        self.currBoard = None
        self.allowedMovements = set()
        self.perimeterEval = None
        self.Table = None
        self.currHash = None
        self.timeCut = 5

    def name(self):
        return {'nombre': 'Ignacio', 'apellido': 'Schuemer', 'legajo': 34575}
    
    def __str__(self):
        return 'Chirimbolo'
    
    def reset(self):
        self.currBoard = None
        self.allowedMovements = set()
        self.perimeterEval = None
        self.Table = None
        self.currHash = None
        self.timeCut = 1
    
    def initTable(self):
        ZobristTable = [[[np.random.randint(0, 2**31) for k in range(2)] for j in range(self.currBoard.shape[1])] for i in range(self.currBoard.shape[0])]
        return ZobristTable

    def hash(self):
        h = 0
        for i in np.argwhere(self.currBoard != 0):
            player = self.currBoard[i[0], i[1]]
            if player == -1:
                p = 0
            else:
                p = 1
            h = h ^ self.Table[i[0]][i[1]][p]
        return h

    def update_hash(self, row, col, player, hash):
        if player == -1:
            hash ^= self.Table[row][col][0]
        else:
            hash ^= self.Table[row][col][1]
        return hash
    
    def action(self, board):
        """
        Returns the next action to be taken by the agent.
        
        Parameters
        ----------
        board : numpy array
            The current board state.
        """
        if self.currBoard is None:
            self.currBoard = np.zeros((board.shape[0], board.shape[1]))   
            self.perimeterEval = [board.shape[0]//2, board.shape[0]//2, 
                                 board.shape[1]//2, board.shape[1]//2] 
            self.Table = self.initTable()
            self.currHash = self.hash()    
            
        if board[board.shape[0]//2][board.shape[1]//2] == 0:
            self.currHash = self.update_hash(board.shape[0]//2, board.shape[1]//2, 1, self.currHash)
            return (board.shape[0]//2)*board.shape[1] + board.shape[1]//2

        newMoves = self.__getNewMoves(board)
        for mov in newMoves:
            self.currHash = self.update_hash(mov[0], mov[1], -1, self.currHash)
        self.currBoard = board
        self.__updateAllowedMovements(newMoves)
        myMove = self.__selectMovement()
        return myMove[0]*board.shape[1] + myMove[1]

    def __getNewMoves(self, board):
        """
        Returns the new moves made by the opponent.

        Parameters
        ----------
        board : numpy array
            The current board state.
        """
        return np.argwhere(board != self.currBoard)
    
    def __updateAllowedMovements(self, newMoves):
        """
        Updates the allowed movements of the agent based on the adjacent positions of the new moves.

        Parameters
        ----------
        newMoves : numpy array
            The new moves made by the opponent.
        """

        added = set()
        oldPerimeter = self.perimeterEval
        for mov in newMoves:
            relativePositions = [(-1, -1), (-1, 0), (-1, 1),(0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for rp in relativePositions:
                pos = (mov[0]+rp[0], mov[1]+rp[1])
                if self.__isPosInsideBoard(pos[0], pos[1]) and self.__isPosEmpty(pos[0], pos[1]) and pos not in self.allowedMovements:
                    self.allowedMovements.add(pos)
                    added.add(pos)
            if (mov[0], mov[1]) in self.allowedMovements:
                self.allowedMovements.remove((mov[0], mov[1]))

            radio = 2
            if mov[0]-radio < self.perimeterEval[0]:
                self.perimeterEval[0] = max(mov[0]-radio, 0)
            if mov[0]+radio > self.perimeterEval[1]:
                self.perimeterEval[1] = min(mov[0]+radio, self.currBoard.shape[0])
            if mov[1]-radio < self.perimeterEval[2]:
                self.perimeterEval[2] = max(mov[1]-radio, 0)
            if mov[1]+radio > self.perimeterEval[3]:
                self.perimeterEval[3] = min(mov[1]+radio, self.currBoard.shape[1]-1)
        return added, oldPerimeter

    def __isPosEmpty(self, i, j):
        """
        Returns True if the position is empty, False otherwise.
        """
        return self.currBoard[i][j] == 0

    def __isPosInsideBoard(self, i, j):
        """
        Returns True if the position is inside the board, False otherwise.
        """
        return i >= 0 and i < self.currBoard.shape[0] and j >= 0 and j < self.currBoard.shape[1]
    
    def __selectMovement(self):
        """
        Select the next movement to be made by the agent.
        """
        alpha = float('-inf')
        beta = float('inf')
        node_value = float('-inf')
        hash = self.currHash
        start = perf_counter()
        for mov in self.allowedMovements:
            self.currBoard[mov[0]][mov[1]] = 1
            hash = self.update_hash(mov[0], mov[1], 1, hash)
            value = self.__alpha_beta(deep-1, alpha, beta, False, mov, hash)
            if value > node_value:
                node_value = value
                move = mov
            self.currBoard[mov[0]][mov[1]] = 0
            if perf_counter() - start > self.timeCut:
                break
        return move

    def __alpha_beta(self, depth, alpha, beta, maximizingPlayer, move, hash):
        """
        Finds the best movement for the agent using the alpha-beta pruning algorithm.

        Parameters
        ----------
        depth : int
            The current depth of the tree.
        alpha : int
            The alpha value. 
        beta : int
            The beta value.
        maximizingPlayer : bool
            True if the agent is the maximizing player, False otherwise.
        move : tuple
            The movement to be evaluated.
        """
        if hash in boardValues and boardValues[hash][2] >= depth:
            score = boardValues[hash][0] - 1.0494*boardValues[hash][1]
            return score

        if depth == 0 or self.__isTerminal():
            return self.__heuristicValue(maximizingPlayer, move, hash, depth)
        if maximizingPlayer:
            value = float('-inf')
            newMovements, perEval = self.__updateAllowedMovements([move])
            for mov in self.allowedMovements:
                self.currBoard[mov[0]][mov[1]] = 1
                hash = self.update_hash(mov[0], mov[1], 1, hash)
                value = max(value, self.__alpha_beta(depth-1, alpha, beta, False, mov, hash))
                self.currBoard[mov[0]][mov[1]] = 0
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
                
            self.allowedMovements-=newMovements
            self.allowedMovements.add(move)
            self.perimeterEval = perEval
            return value
        else:
            value = float('inf')
            newMovements, perEval = self.__updateAllowedMovements([move])
            for mov in self.allowedMovements:
                self.currBoard[mov[0]][mov[1]] = -1
                hash = self.update_hash(mov[0], mov[1], -1, hash)
                value = min(value, self.__alpha_beta(depth-1, alpha, beta, True, mov, hash))
                self.currBoard[mov[0]][mov[1]] = 0
                beta = min(beta, value)
                if alpha >= beta:
                    break
                
            self.allowedMovements-=newMovements
            self.allowedMovements.add(move)
            self.perimeterEval = perEval
            return value

    def __isTerminal(self):
        """
        Returns True if the game is over, False otherwise.
        """
        if len(self.allowedMovements) == 0:
            return True
        return False
    
    def __heuristicValue(self, maximizingPlayer, pos, hash, depth):
        """
        Returns the heuristic value of the board.

        Parameters
        ----------
        maximizingPlayer : bool
            True if the agent is the maximizing player, False otherwise.
        pos : tuple
            The movement to be evaluated.   
        """
        if not maximizingPlayer:
            board = -1*self.currBoard[self.perimeterEval[0]:self.perimeterEval[1]+1, self.perimeterEval[2]:self.perimeterEval[3]+1]
        else :
            board = self.currBoard[self.perimeterEval[0]:self.perimeterEval[1]+1, self.perimeterEval[2]:self.perimeterEval[3]+1]

        board = np.concatenate((np.full((board.shape[0],1),3),board,np.full((board.shape[0],1),3)),axis=1)
        board = np.concatenate((np.full((1,board.shape[1]),3),board,np.full((1,board.shape[1]),3)),axis=0)

        attackValue = 0
        strRow = ''.join(' '.join(map(str, row)) for row in board if not np.all(row[1:-1]==0))
        strCol = ''.join(' '.join(map(str, col)) for col in board.T if not np.all(col[1:-1]==0))
        strDiag1 = ''.join(' '.join(map(str,board.diagonal(i))) for i in range(-board.shape[0]+1, board.shape[1]) if len(board.diagonal(i))>=5 and not np.all(board.diagonal(i)[1:-1]==0))
        strDiag2 = ''.join(' '.join(map(str,np.fliplr(board).diagonal(i))) for i in range(-board.shape[0]+1, board.shape[1]) if len(np.fliplr(board).diagonal(i))>=4 and not np.all(np.fliplr(board).diagonal(i)[1:-1]==0))
        
        for key in KNOWN_MOVES:
            occurences = 0
            occurences+=strRow.count(key)
            occurences+=strCol.count(key)
            occurences+=strDiag1.count(key)
            occurences+=strDiag2.count(key)
            attackValue += occurences*KNOWN_MOVES[key]

        board = -1*board
        
        strRow = ''.join(' '.join(map(str, row)) for row in board if not np.all(row[1:-1]==0))
        strCol = ''.join(' '.join(map(str, col)) for col in board.T if not np.all(col[1:-1]==0))
        strDiag1 = ''.join(' '.join(map(str,board.diagonal(i))) for i in range(-board.shape[0]+1, board.shape[1]) if len(board.diagonal(i))>=5 and not np.all(board.diagonal(i)[1:-1]==0))
        strDiag2 = ''.join(' '.join(map(str,np.fliplr(board).diagonal(i))) for i in range(-board.shape[0]+1, board.shape[1]) if len(np.fliplr(board).diagonal(i))>=5 and not np.all(np.fliplr(board).diagonal(i)[1:-1]==0))
        defenseValue = 0
        for key in KNOWN_MOVES:
            occurences = 0
            occurences+=strRow.count(key)
            occurences+=strCol.count(key)
            occurences+=strDiag1.count(key)
            occurences+=strDiag2.count(key)
            defenseValue += occurences*KNOWN_MOVES[key]
        
        boardValues[hash] = [attackValue, defenseValue, depth]
        return attackValue - 1.0494*defenseValue

    






