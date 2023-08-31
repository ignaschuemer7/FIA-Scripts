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

KNOWN_MOVES = { 
                #con doble espacio
            #     ' 1  1  1  1  1 ': 40000000,
            #    '0  1  1  1  1  0': 400000,
            #    '0  1  1  1  1 -1': 50000,
            #    '-1  1  1  1  1  0': 50000,
            #    '0  1  1  1  0': 30000,
            #    '-1  1  1  1  0  0': 15000,
            #    '0  0  1  1  1 -1': 15000,
            #    '0  1  0  1  1  0': 7000,
            #    '0  1  1  0  1  0': 7000,
            #    '1  1  0  1  1': 50000,
            #    '-1  1  0  1  1  0': 3000,
            #    '-1  1  1  0  1  0': 3000,
            #    '0  1  0  1  1 -1': 3000,
            #    '0  1  1  0  1 -1': 3000,
            #    '0  0  1  1  0': 500, 
            #    '0  1  1  0  0': 500, 
            #    '0  1  1  0  0 -1': 500,
            #    '-1  1  1  0  0  0': 400, 
            #    '0  0  0  1  1 -1': 400,
            #    '0  1  0  1  0': 300,
            #     '-1  1  0  1  0  0': 40,
            #     '0  0  1  0  1 -1': 40,
            #     '-1  1  1  1  1  1 -1': 0,
            }

# def heuristicValue(board, position, player):
#     "Returns the heuristic value of the board"
    # if player:
    #     player = 1
    # else:
    #     player = -1
    # value = 0
    # # print(board.board)
    # value+=np.where(self.currBoard[pos[0],pos[1]-4:pos[1]+4]==player,player,0).sum()
    # value+=np.where(self.currBoard[pos[0]-4:pos[0]+4:,pos[1]]==player,player,0).sum()
    # value+=np.where(self.currBoard.diagonal(pos[1]-pos[0])==player,player,0).sum()
    # value+=np.where(np.fliplr(self.currBoard).diagonal(self.currBoard.shape[1]-pos[1]-1-pos[0])==player,player,0).sum()
    # #si esta contiguo a una ficha mia sumo 1
    # relativePositions = [(-1, -1), (-1, 0), (-1, 1),(0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    # for rp in relativePositions:
    #     posr = (pos[0]+rp[0], pos[1]+rp[1])
    #     if self.isPosInsideBoard(posr[0], posr[1]) and self.currBoard[posr[0], posr[1]] == player:
    #         if player == 1:
    #             value += 3
    #         else:
    #             value -= 3

    # return value

    # value = 0
    #     for key in KNOWN_MOVES:
    #         if key in ''.join(map(str, self.currBoard[pos[0], :])):
    #             value += KNOWN_MOVES[key]
    #         if key in ''.join(' '.join(map(str, self.currBoard[:, pos[1]]))):
    #             value += KNOWN_MOVES[key]
    #         if key in ''.join(' '.join(map(str, np.flipud(self.currBoard).diagonal(pos[1]-pos[0])))):
    #             value += KNOWN_MOVES[key]
    #         if key in ''.join(' '.join(map(str, self.currBoard.diagonal(pos[0]-pos[1])))):
    #             value += KNOWN_MOVES[key]

    #     return value



    # if maximizingPlayer:
    #         board = self.currBoard    
    #     else:
    #         board = -1*self.currBoard

    #     attackValue = 0
    #     for key in KNOWN_MOVES:
    #         occurences = 0
    #         occurences+=len(re.findall(key, ''.join(' '.join(map(str, board[pos[0], :])))))
    #         occurences+=len(re.findall(key, ''.join(' '.join(map(str, board[:, pos[1]])))))
    #         occurences+=len(re.findall(key, ''.join(' '.join(map(str, np.flipud(board).diagonal(pos[1]-pos[0]))))))
    #         occurences+=len(re.findall(key, ''.join(' '.join(map(str, board.diagonal(pos[0]-pos[1]))))))
    #         attackValue += occurences*KNOWN_MOVES[key]
        
    #     #defense
    #     defenseValue = 0
    #     for key in KNOWN_MOVES:
    #         occurences = 0
    #         occurences+=len(re.findall(key, ''.join(' '.join(map(str, -board[pos[0], :])))))
    #         occurences+=len(re.findall(key, ''.join(' '.join(map(str, -board[:, pos[1]])))))
    #         occurences+=len(re.findall(key, ''.join(' '.join(map(str, np.flipud(-board).diagonal(pos[1]-pos[0]))))))
    #         occurences+=len(re.findall(key, ''.join(' '.join(map(str, -board.diagonal(pos[0]-pos[1]))))))
    #         defenseValue += occurences*KNOWN_MOVES[key]
        
    #     return attackValue + defenseValue


    # if maximizingPlayer:
    #         board = self.currBoard    
    #     else:
    #         board = -1*self.currBoard
        
    #     diag = [board.diagonal(i) for i in range(-board.shape[0]+1, board.shape[1])]
    #     inv_diag = [np.fliplr(board).diagonal(i) for i in range(-board.shape[0]+1, board.shape[1])]

    #     attackValue = 0
    #     for key in KNOWN_MOVES:
    #         occurences = 0
    #         #recorrer todas las filas
    #         occurences+=len(re.findall(key, ''.join(' '.join(map(str, row)) for row in board)))
    #         occurences+=len(re.findall(key, ''.join(' '.join(map(str, board.T)))))
    #         occurences+=len(re.findall(key, ''.join(' '.join(map(str, diag)))))
    #         occurences+=len(re.findall(key, ''.join(' '.join(map(str, inv_diag)))))
    #         attackValue += occurences*KNOWN_MOVES[key]
        
    #     #defense
    #     defenseValue = 0
    #     for key in KNOWN_MOVES:
    #         occurences = 0
    #         occurences+=len(re.findall(key, ''.join(' '.join(map(str, -board)))))
    #         occurences+=len(re.findall(key, ''.join(' '.join(map(str, -board.T)))))
    #         occurences+=len(re.findall(key, ''.join(' '.join(map(str, -1*diag)))))
    #         occurences+=len(re.findall(key, ''.join(' '.join(map(str, -1*inv_diag)))))
    #         defenseValue += occurences*KNOWN_MOVES[key]
        
    #     return attackValue + defenseValue
import numpy as np

def heuristic(board, maximizingPlayer):
    if not maximizingPlayer:
        board = -1*board
    #agregar 2 columas de cada lado con un 3 para marcar las paredes
    board = np.concatenate((np.full((board.shape[0],1),3),board,np.full((board.shape[0],1),3)),axis=1)
    #agregar 2 filas de arriba y abajo con un 3 para marcar las paredes
    board = np.concatenate((np.full((1,board.shape[1]),3),board,np.full((1,board.shape[1]),3)),axis=0)
    print(board)
    attackValue = 0
    strRow = ''.join(' '.join(map(str, row)) for row in board if not np.all(row==0))
    strCol = ''.join(' '.join(map(str, col)) for col in board.T if not np.all(col==0))
    strDiag1 = ''.join(' '.join(map(str,board.diagonal(i))) for i in range(-board.shape[0]+1, board.shape[1]) if len(board.diagonal(i))>=4 and not np.all(board.diagonal(i)==0))
    strDiag2 = ''.join(' '.join(map(str,np.fliplr(board).diagonal(i))) for i in range(-board.shape[0]+1, board.shape[1]) if len(np.fliplr(board).diagonal(i))>=4 and not np.all(np.fliplr(board).diagonal(i)==0))
    # print("attack")
    # print("Rows: ", strRow)
    # print("Cols: ", strCol)
    print("Diag1: ", strDiag1)
    print("Diag2: ", strDiag2)
    
    for key in KNOWN_MOVES:
        occurences = 0
        # occurences+=strRow.count(key)
        # occurences+=strCol.count(key)
        occurences+=strDiag1.count(key)
        occurences+=strDiag2.count(key)
        print("key: ", key, "occurences: ", occurences)

        attackValue += occurences*KNOWN_MOVES[key]

    board = -1*board
    
    strRow = ''.join(' '.join(map(str, row)) for row in board if not np.all(row==0))
    strCol = ''.join(' '.join(map(str, col)) for col in board.T if not np.all(col==0))
    strDiag1 = ''.join(' '.join(map(str,board.diagonal(i))) for i in range(-board.shape[0]+1, board.shape[1]) if len(board.diagonal(i))>=4 and not np.all(board.diagonal(i)==0))
    strDiag2 = ''.join(' '.join(map(str,np.fliplr(board).diagonal(i))) for i in range(-board.shape[0]+1, board.shape[1]) if len(np.fliplr(board).diagonal(i))>=4 and not np.all(np.fliplr(board).diagonal(i)==0))
    # print("defense")
    # print("Rows: ", strRow)
    # print("Cols: ", strCol)
    # print("Diag1: ", strDiag1)
    # print("Diag2: ", strDiag2)
    #defense
    defenseValue = 0
    for key in KNOWN_MOVES:
        occurences = 0
        occurences+=strRow.count(key)
        occurences+=strCol.count(key)
        occurences+=strDiag1.count(key)
        occurences+=strDiag2.count(key)
        # print("key: ", key, "occurences: ", occurences)
        defenseValue += occurences*KNOWN_MOVES[key]
    print("Attack: ", attackValue)
    print("Defense: ", defenseValue)
    return attackValue - defenseValue


#checking if the heuristic is correct

board = np.array([  [ -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  -8],
                    [ -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                    [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                    [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                    [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                    [ 0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0],
                    [ 0,  0,  0,  0,  0,  0,  0,  1,  1, -1,  1,  0,  0,  0,  0],
                    [ 0,  0,  0,  0,  0,  0,  0,  1,  0, -1,  0,  0,  0,  0,  0],
                    [ 0,  0,  0,  0,  0,  0, -1,  1, -1,  0,  0,  0,  0,  0,  0],
                    [ 0,  0,  0,  0,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0],
                    [ 0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0],
                    [ 0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                    [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                    [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                    [ -8,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],

])

print(heuristic(board,False))



# Initializes the zHashTable for this board
def initTable():
    zTable = [[[None] * 2 for _ in range(8)] for _ in range(8)]
    currNumber = 0

    for row in range(8):
        for col in range(8):
            for i in range(2):
                zTable[row][col][i] = currNumber
                currNumber += 1

    for subList in zTable:
        print(id(subList))

    print(zTable)


initTable()