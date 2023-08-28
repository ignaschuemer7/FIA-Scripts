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

KNOWED_MOVES = {'5':[100000, [1, 1, 1, 1, 1]],
                '4':[15000, [0, 1, 1, 1, 1, 0]],
                '4-':[10000, [0 ,1 , 1, 1, 1, -1]],
                '1_3':[10000, [1, 0, 1, 1, 1]],
                '2_2':[10000, [1, 1, 0, 1, 1]], 
                '_3_':[5000, [0, 1, 1, 1, 0]], 
                '1_2' :[4000, [0, 1, 0, 1, 1, 0]], 
                '_3-' :[1000, [0, 1, 1, 1, -1]],
                '_1_2-':[1000, [0, 1, 0, 1, 1, -1]],
                '_2_1-':[1000, [0, 1, 1, 0, 1, -1]],
                '_1__2':[700, [0, 1, 0, 0, 1, 1]],
                '1_1_1':[700, [1, 0, 1, 0, 1]],
                '-_3_-':[5000, [-1, 0, 1, 1, 1, 0, -1]], 
                '1___1': [100, [1, 0, 0, 0, 1]],
                '_1_1_':[500, [0, 1, 0, 1, 0]],
                '1__1_':[300, [1, 0, 0, 1, 0]],
                '_1__1-':[200, [0, 1, 1, -1]],
                '_1_1-':[200, [0, 1, 0, 1, -1]],
                '1__1-':[150, [1, 0, 0, 1, -1]],
                '_2_':[500, [0, 1, 1, 0]]}

def heuristicValue(board, position, player):
    "Returns the heuristic value of the board"
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
def prints():
    print("BEST_POSITIONS")
