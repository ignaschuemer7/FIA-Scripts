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

KNOWN_MOVES = {'[1. 1. 1. 1. 1.]': 100000,
                '[0. 1. 1. 1. 1. 0.]': 15000,
                '[0. 1. 1. 1. 1. -1.]': 10000,
                ' [1. 0. 1. 1. 1.]': 10000,
                '[1. 1. 0. 1. 1.]': 10000,
                '[0. 1. 1. 1. 0.]': 5000,
                '[0. 1. 0. 1. 1. 0.]': 4000,
                '[0. 1. 1. 1. -1.]': 1000,
                '[0. 1. 0. 1. 1. -1.]': 1000,
                '[0. 1. 1. 0. 1. -1.]': 1000,
                '[0. 1. 0. 0. 1. 1.]': 700,
                '[1. 0. 1. 0. 1.]': 700,
                '[-1. 0. 1. 1. 1. 0. -1.]': 5000,
                '[1. 0. 0. 0. 1.]': 100,
                ' [0. 1. 0. 1. 0.]': 500,
                '[1. 0. 0. 1. 0.]': 300,
                '[0. 1. 1. -1.]': 200,
                '[0. 1. 0. 1. -1.]': 200,
                ' [1. 0. 0. 1. -1.]': 150,
                ' [0. 1. 1. 0.]': 500,
                '[0. 1. 1. 1. 1.]': 100}
# KNOWN_MOVES = { '[1 1 1 1 1]': 100000,
#                 '[0. 1. 1. 1. 1. 0.]': 15000,
#                 '[0. 1. 1. 1. 1. -1.]': 10000,
#                 '[1. 0. 1. 1. 1.]': 10000,
#                 '[1. 1. 0. 1. 1.]': 10000,
#                 '[0. 1. 1. 1. 0.]': 5000,
#                 '[0. 1. 0. 1. 1. 0.]': 4000,
#                 '[0. 1. 1. 1. -1.]': 1000,
#                 '[0. 1. 0. 1. 1. -1.]': 1000,
#                 '[0. 1. 1. 0. 1. -1.]': 1000,
#                 '[0. 1. 0. 0. 1. 1.]': 700,
#                 '[1. 0. 1. 0. 1.]': 700,
#                 '[-1. 0. 1. 1. 1. 0. -1.]': 5000,
#                 '[1. 0. 0. 0. 1.]': 100,
#                 '[0. 1. 0. 1. 0.]': 500,
#                 '[1. 0. 0. 1. 0.]': 300,
#                 '[0. 1. 1. -1.]': 200,
#                 '[0. 1. 0. 1. -1.]': 200,
#                 '[1. 0. 0. 1. -1.]': 150,
#                 '[0. 1. 1. 0.]': 500,
#                 '[0. 1. 1. 1. 1.]': 100}
# KNOWN_MOVES = {'1 1 1 1 1': 100000,
#  '0 1 1 1 1 0': 15000,
#  '0 1 1 1 1 -1': 10000,
#  '1 0 1 1 1': 10000,
#  '1 1 0 1 1': 10000,
#  '0 1 1 1 0': 5000,
#  '0 1 0 1 1 0': 4000,
#  '0 1 1 1 -1': 1000,
#  '0 1 0 1 1 -1': 1000,
#  '0 1 1 0 1 -1': 1000,
#  '0 1 0 0 1 1': 700,
#  '1 0 1 0 1': 700,
#  '-1 0 1 1 1 0 -1': 5000,
#  '1 0 0 0 1': 100,
#  '0 1 0 1 0': 500,
#  '1 0 0 1 0': 300,
#  '0 1 1 -1': 200,
#  '0 1 0 1 -1': 200,
#  '1 0 0 1 -1': 150,
#  '0 1 1 0': 500,
#  '0 1 1 1 1': 10000}

KNOWN_MOVES = {'1 1 1 1 1': 20000000,
               '0 1 1 1 1 0': 400000,
               '0 1 1 1 1 -1': 50000,
               '-1 1 1 1 1 0': 50000,
               '0 1 1 1 0': 30000,
            #    '1 1 0 1 1': 30000,
               '-1 1 1 1 0': 15000,
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
            #    '0 1 1 1 -1': 1000,
            #    '0 1 0 1 1 -1': 1000,
            #    '0 1 1 0 1 -1': 1000,
            #    '0 1 0 0 1 1': 700,
            #    '1 0 1 0 1': 700,
            #    '-1 0 1 1 1 0 -1': 5000,
            #    '1 0 0 0 1': 100,
            #    '0 1 0 1 0': 500,
            #    '1 0 0 1 0': 300,
            #    '0 1 -1': 200,
            #    '0 1 0 1 -1': 200,
            #    '1 0 0 1 -1': 150,
            #    '0 1 1 0': 500,
            #    '0 1 1 1 1': 10000,
            #    '-1 1 1 1 1 0': 15000,
            #    '0 1 1 1 1 -1': 15000,
            #    '-1 1 1 1 1 -1': 0,
            #    '0 1 1 1 1 0 -1': 3000
            }



savedSecuences = {}

class Board():
    "class to know the state of the board, last movements, and the perimeter movements"
    def __init__(self, usedBoard, valueBoard=np.array(BEST_POSITIONS)):
        self.board = usedBoard
        self.player = 1
        self.valueBoard = valueBoard

    def isPosInsideBoard(self, i, j):
        return i >= 0 and i < self.board.shape[0] and j >= 0 and j < self.board.shape[1]

    def updatevalueBoard(self, move, player):
        """"
        Look arround the 32 positions that are arround the last movement on the board in the diferent directions
        and update the value of the board.
        The idea is to slice the board in 32 parts and update with the value of the KNOWED_MOVES in each empty position 
        """      
        self.board[move[0]][move[1]] = player
        x = move[0]
        y = move[1]
        # # #Actualizamos las filas
        start = max(0, y-5) 
        end = min(15, y+6)
        strArray = str(self.board[x, start:end])
        print("el arreglo de la fila es", strArray)
        value = 0 
        # print("el arreglo de la fila es", self.valueBoard[x, start:end])
        if strArray in savedSecuences:
            self.valueBoard[x, start:end] += savedSecuences[strArray]
        else:
            #si no esta guardado lo guardamos
            #creamos un vector de valores del tamaño de la secuencia que contenga los valores que se le sumarian a los lugares vacíos
            array = np.zeros(len(self.board[x,start:end]))
            for i in range(start, y+1):
                    #vemos si la secuencia de 5 esta en el diccionario
                    sec = str(self.board[x, i:i+5])
                    flipsec = str(np.flip(self.board[x, i:i+5]))
                    if sec in KNOWN_MOVES:
                        for j in range(5):
                            if self.board[x][i+j] == 0:
                                array[i+j-start] += KNOWN_MOVES[sec]
                                self.valueBoard[x, i+j] += KNOWN_MOVES[sec]

                    elif flipsec in KNOWN_MOVES:
                        for j in range(5):
                            if self.board[x, i+j] == 0:
                                array[i+j-start] += KNOWN_MOVES[flipsec]
                                self.valueBoard[x, i+j] += KNOWN_MOVES[str(np.flip(self.board[x, i:i+5]))]
            savedSecuences[strArray] = array

        #Actualizamos las columnas
        start2 = max(0, x-5)
        end2 = min(15, x+6)
        strArray = str(self.board[start2:end2, y])
        print("el arreglo de la columna es", strArray)
        value = 0
        if strArray in savedSecuences:
            self.valueBoard[start2:end2, y] += savedSecuences[strArray]
        else:
            #si no esta guardado lo guardamos
            #creamos un vector de valores del tamaño de la secuencia que contenga los valores que se le sumarian a los lugares vacíos
            array = np.zeros(len(self.board[start2:end2, y]))
            for i in range(start2, x+2):
                    # print("la secuencia es", self.board[i:i+5, y])
                    #vemos si la secuencia de 5 esta en el diccionario
                    sec = str(self.board[i:i+5, y])
                    flipsec = str(np.flip(self.board[i:i+5, y]))
                    print("la secuencia es", sec)
                    if sec in KNOWN_MOVES:
                        for j in range(5):
                            if self.board[i+j][y] == 0:
                                array[i+j-start2] += KNOWN_MOVES[sec]
                                self.valueBoard[i+j, y] += KNOWN_MOVES[sec]

                    elif flipsec in KNOWN_MOVES:
                        for j in range(5):
                            if self.board[i+j][y] == 0:
                                array[i+j-start2] += KNOWN_MOVES[flipsec]
                                self.valueBoard[i+j, y] += KNOWN_MOVES[str(np.flip(self.board[i:i+5, y]))]
            savedSecuences[strArray] = array

        start = max(0, y-5)
        end = min(15, y+6)
        strArray = str(self.board.diagonal(y-x)[start:end])
        print("el arreglo de la diagonal es", strArray)
        value = 0
        if strArray in savedSecuences:
            np.einsum('i,i->i', self.valueBoard.diagonal(y-x)[start:end], savedSecuences[strArray])
        else:
            #si no esta guardado lo guardamos
            #creamos un vector de valores del tamaño de la secuencia que contenga los valores que se le sumarian a los lugares vacíos
            array = np.zeros(len(self.board.diagonal(y-x)[start:end]))
            for i in range(start, x-1):
                    #vemos si la secuencia de 5 esta en el diccionario
                    sec = str(self.board.diagonal(y-x)[i:i+5])
                    print("la secuencia es", sec)
                    flipsec = str(np.flip(self.board.diagonal(y-x)[i:i+5]))
                    if sec in KNOWN_MOVES:
                        for j in range(5):
                            if self.board[i+j][i+j] == 0:
                                array[i+j-start] += KNOWN_MOVES[sec]
                                self.valueBoard[i+j][i+j] += KNOWN_MOVES[sec]
                    elif flipsec in KNOWN_MOVES:
                        for j in range(5):
                            if self.board[i+j][i+j] == 0:
                                array[i+j-start] += KNOWN_MOVES[flipsec]
                                self.valueBoard[i+j][i+j] += KNOWN_MOVES[str(np.flip(self.board.diagonal(y-x)[i:i+5]))]
            savedSecuences[strArray] = array
        # #anti-diagonal
        # start = max(0, x-5)
        # end = min(15, x+6)
        # strArray = str(np.fliplr(self.board).diagonal(self.board.shape[1]-y-1-x)[start:end])
        # print("el arreglo de la antidiagonal es", strArray)
        # print("d-----------------")
        # value = 0
        # if strArray in savedSecuences:
        #     self.valueBoard.diagonal(self.board.shape[1]-y-1-x)[start:end]+= savedSecuences[strArray]
        # else:
        #     #si no esta guardado lo guardamos
        #     #creamos un vector de valores del tamaño de la secuencia que contenga los valores que se le sumarian a los lugares vacíos
        #     array = np.zeros(len(np.fliplr(self.board).diagonal(self.board.shape[1]-y-1-x)[start:end]))
        #     for i in range(start, x+1):
        #             #vemos si la secuencia de 5 esta en el diccionario
        #             sec = str(np.fliplr(self.board).diagonal(self.board.shape[1]-y-1-x)[i:i+5])
        #             flipsec = str(np.flip(np.fliplr(self.board).diagonal(self.board.shape[1]-y-1-x)[i:i+5]))
        #             if sec in KNOWN_MOVES:
        #                 for j in range(5):
        #                     if self.board[i+j][14-i-j] == 0:
        #                         array[i+j-start] += KNOWN_MOVES[sec]
        #                         self.valueBoard[i+j][14-i-j] += KNOWN_MOVES[sec]

        #             elif flipsec in KNOWN_MOVES:
        #                 for j in range(5):
        #                     if self.board[i+j][14-i-j] == 0:
        #                         array[i+j-start] += KNOWN_MOVES[flipsec]
        #                         self.valueBoard[i+j][14-i-j] += KNOWN_MOVES[str(np.flip(np.fliplr(self.board).diagonal(self.board.shape[1]-y-1-x)[i:i+5]))]
        #     savedSecuences[strArray] = array
#test   

board = Board(np.zeros((15, 15)), np.array(BEST_POSITIONS))
# board.board[7][8] = 1
# board.board[7][9] = 1
# board.board[7][10] = 1
# board.board[7][7] = 1
# board.board[6][7] = 1
# board.board[5][7] = 1
# board.board[4][7] = 1
# board.board[2][7] = 1

board.board[7][7] = 1
board.board[8][8] = 1
board.board[9][9] = 1




for i in range(15):
    print(board.board[i])
print('----------------------')
board.updatevalueBoard([5, 5], 1)
for i in range(15):
    print(board.valueBoard[i])
print('----------------------')


    
class SchuemerAgent ():
    def __init__(self):
        self.currBoard = Board(np.zeros((15, 15)))
        self.rating = 0

    def identifymove(self, board):
        return np.argwhere(board == -1)

    def action(self, board):
        update = self.identifymove(board)
        self.currBoard.updatevalueBoard(update, -1)
        # print('dkfjsfksjd',self.currBoard.valueBoard == np.amax(self.currBoard.valueBoard))
        maxPos = np.argwhere(self.currBoard.board == 0)
        #elegimos el de mayor valor
        newPos = maxPos[np.random.choice(len(maxPos))]
        self.currBoard.updatevalueBoard(newPos, 1)
        board[newPos[0]][newPos[1]] = 1
        print(self.currBoard.valueBoard)
        return newPos[0]*15 + newPos[1]
    
    def name(self):
        return {'nombre': 'Ignacio', 'apellido': 'Schuemer', 'legajo': 34575}
    
    def __str__(self):
        return 'Chirimbolo'


# def alpha_beta(board, depth, alpha, beta, maximizingPlayer, move):
#     if depth == 0 or board.isTerminal():
#         return heuristicValue(board, maximizingPlayer, move)
#     if maximizingPlayer:
#         value = float('-inf')
#         for mov in board.getPerimeterMovements():
#             newBoard = board.copy()
#             board.board[mov] = 1
#             newBoard.doMovements(board.board.copy())
#             value = max(value, alpha_beta(newBoard, depth-1, alpha, beta, False, mov))
#             if alpha >= beta:
#                 break
#             alpha = max(alpha, value)
#         return value
#     else:
#         value = float('inf')
#         for mov in board.getPerimeterMovements():
#             newBoard = board.copy()
#             board.board[mov] = -1
#             newBoard.doMovements(board.board.copy())
#             value = min(value, alpha_beta(newBoard, depth-1, alpha, beta, True, mov))
#             if alpha >= beta:
#                 break
#             beta = min(beta, value)
#         return value


    





        