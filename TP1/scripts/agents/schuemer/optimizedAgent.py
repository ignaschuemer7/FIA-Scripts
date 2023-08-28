import numpy as np
import time
import regex as re

KNOWN_MOVES = {'1 1 1 1 1': 50000000,
               '0 1 1 1 1 0': 400000,
               '0 1 1 1 1 -1': 50000,
               '-1 1 1 1 1 0': 50000,
               '0 1 1 1 0': 30000,
               '-1 1 1 1 0 0': 15000,
               '0 0 1 1 1 -1': 15000,
               '0 1 0 1 1 0': 7000,
               '0 1 1 0 1 0': 7000,
               '-1 1 0 1 1 0': 3000,
               '-1 1 1 0 1 0': 3000,
               '0 1 0 1 1 -1': 3000,
               '0 1 1 0 1 -1': 3000,
               '0 0 1 1 0': 500, 
               '0 1 1 0 0 -1': 500,
               '-1 1 1 0 0 0': 400, 
               '0 0 0 1 1 -1': 400,
                '0 1 0 1 0': 300,
                '-1 1 0 1 0 0': 40,
                '0 0 1 0 1 -1': 40,
            }
class SchuemerAgent ():
    def __init__(self):
        self.currBoard = None
        self.allowedMovements = set()
        self.evaluationSquare = [2, 2, 2, 2]
    def name(self):
        return {'nombre': 'Ignacio', 'apellido': 'Schuemer', 'legajo': 34575}
    
    def __str__(self):
        return 'Chirimbolo'
    
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
        if board[board.shape[0]//2][board.shape[1]//2] == 0:
            return (board.shape[0]//2)*board.shape[1] + board.shape[1]//2
        newMoves = self.__getNewMoves(board)
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
        for mov in newMoves:
            relativePositions = [(-1, -1), (-1, 0), (-1, 1),(0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for rp in relativePositions:
                pos = (mov[0]+rp[0], mov[1]+rp[1])
                if self.__isPosInsideBoard(pos[0], pos[1]) and self.__isPosEmpty(pos[0], pos[1]) and pos not in self.allowedMovements:
                    self.allowedMovements.add(pos)
                    added.add(pos)
            if (mov[0], mov[1]) in self.allowedMovements:
                self.allowedMovements.remove((mov[0], mov[1]))

            #cambiar el radio de evaluacion si los nuevos movimientos estan más lejos del centro
            # diff = max(abs(mov[0]-self.currBoard.shape[0]//2), abs(mov[1]-self.currBoard.shape[1]//2))
            

        return added

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
        for mov in self.allowedMovements:
            self.currBoard[mov[0]][mov[1]] = 1
            value = self.__alpha_beta(0, alpha, beta, False, mov)
            if value > node_value:
                node_value = value
                move = mov
            self.currBoard[mov[0]][mov[1]] = 0
        return move

    def __alpha_beta(self, depth, alpha, beta, maximizingPlayer, move):
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

        if depth == 0 or self.__isTerminal():
            return self.__heuristicValue(maximizingPlayer, move)
        if maximizingPlayer:
            value = float('-inf')
            newMovements = self.__updateAllowedMovements([move])
            for mov in self.allowedMovements:
                self.currBoard[mov[0]][mov[1]] = 1
                value = max(value, self.__alpha_beta(depth-1, alpha, beta, False, mov))
                self.currBoard[mov[0]][mov[1]] = 0
                if alpha >= beta:
                    break
                alpha = max(alpha, value)
            self.allowedMovements-=newMovements
            self.allowedMovements.add(move)
            return value
        else:
            value = float('inf')
            newMovements = self.__updateAllowedMovements([move])
            for mov in self.allowedMovements:
                self.currBoard[mov[0]][mov[1]] = -1
                value = min(value, self.__alpha_beta(depth-1, alpha, beta, True, mov))
                self.currBoard[mov[0]][mov[1]] = 0
                if alpha >= beta:
                    break
                beta = min(beta, value)
            self.allowedMovements-=newMovements
            self.allowedMovements.add(move)
            return value
        
    def __isTerminal(self):
        """
        Returns True if the game is over, False otherwise.
        """
        if len(self.allowedMovements) == 0:
            return True
        return False
    
    def __heuristicValue(self, maximizingPlayer, pos):
        """
        Returns the heuristic value of the board.

        Parameters
        ----------
        maximizingPlayer : bool
            True if the agent is the maximizing player, False otherwise.
        pos : tuple
            The movement to be evaluated.   
        """
        if maximizingPlayer:
            board = self.currBoard    
        else:
            board = -1*self.currBoard

        attackValue = 0
        
        for key in KNOWN_MOVES:
            occurences = 0
            occurences+=len(re.findall(key, ''.join(' '.join(map(str, board[pos[0], :])))))
            occurences+=len(re.findall(key, ''.join(' '.join(map(str, board[:, pos[1]])))))
            occurences+=len(re.findall(key, ''.join(' '.join(map(str, np.flipud(board).diagonal(pos[1]-pos[0]))))))
            occurences+=len(re.findall(key, ''.join(' '.join(map(str, board.diagonal(pos[0]-pos[1]))))))
            attackValue += occurences*KNOWN_MOVES[key]

        #defense
        defenseValue = 0
        for key in KNOWN_MOVES:
            occurences = 0
            occurences+=len(re.findall(key, ''.join(' '.join(map(str, -1*board[pos[0], :])))))
            occurences+=len(re.findall(key, ''.join(' '.join(map(str, -1*board[:, pos[1]])))))
            occurences+=len(re.findall(key, ''.join(' '.join(map(str, np.flipud(-1*board).diagonal(pos[1]-pos[0]))))))
            occurences+=len(re.findall(key, ''.join(' '.join(map(str, -1*board.diagonal(pos[0]-pos[1]))))))
            defenseValue += occurences*KNOWN_MOVES[key]

        return attackValue + defenseValue