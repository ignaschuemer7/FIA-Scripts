import numpy as np

#posible plays
def posible_actions(board):
    return np.flatnonzero(board == 0)

#evaluation/heuristic function 
def evaluate(board):
    #CHECK hardcodeo de patterns y sus valores
    patterns_value_count = {"XXXXX": [100000,0],"XXXX": [100,0],"XXX": [15,0],"XX": [5,0],"OOOOO": [-100000,0],"OOOO": [-100000,0],"OOO": [-5000,0],"OO": [-2,0]}
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]

    #poray hay algo mas eficiente cuando el tablero ya tiene bastantes piezas...
    #ver si puedo reducir el espacio de busqueda basado en centroides o algo asi...

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 1 or board[row][col] == -1:
                for dr, dc in directions:
                    pattern = ""
                    for i in range(-1, 4):
                        r = row + i * dr
                        c = col + i * dc
                        if 0 <= r < len(board) and 0 <= c < len(board[r]):
                            if board[r][c] == 1:
                                str = "X" 
                                pattern += str
                            if board[r][c] == -1:
                                str = "O" 
                                pattern += str
                            #si es _ no hago nada. asi contemplo casos como X_X_X que si deberian sumar puntos
                        if pattern in patterns_value_count:
                            
                            patterns_value_count[pattern][1] += 1
                
    total_score = 0
    for pattern in patterns_value_count:
        total_score += patterns_value_count[pattern][0] * patterns_value_count[pattern][1]
    return total_score

def minimax(board):
    #tener los primeros movimientos de apertura hardcodeados...?

        if np.all(board == 0): #si es el primer turno
            return 112
        #else minimax depth2
        board_value = evaluate(board)
        new_board=board.copy()
        best_move = np.random.choice(posible_actions(board))
        best_value = -10000000
        for move in posible_actions(board):
            new_board[move // 15][move % 15] = 1
            new_board_value = evaluate(new_board)
            if new_board_value - board_value > 6: #si es una jugada significativa. CHECK EL NRO HARDCODEADO
                #hay algo mas heuristico que se pueda hacer aca? aca con ver si ese move esta al lado de un -1 o 1 alcanza? me ahorraria el evaluate.
                value2=10000000
                possible_moves2 = posible_actions(new_board)
                new_board2= new_board.copy()
                for move2 in possible_moves2:
                    new_board2[move2 // 15][move2 % 15] = -1
                    a=evaluate(new_board2)
                    if a < -100000: #si encuentro una jugada de muy bajo valor, dejo de mirar los otros hijos. CHECK EL NRO HARDCODEADO
                        #hacer algo mas heuristico aca
                        value2 = a
                        break
                    if a < value2:
                        value2 = a
                    new_board2[move2 // 15][move2 % 15] = 0
                if value2 > best_value:
                    best_value = value2
                    best_move = move
            new_board[move // 15][move % 15] = 0
            #aca agregar una heuristica para q si ya vi una buena jugada. termino de evaluar otras. 
        return best_move

class VidelaAgent:
    def action(self, board): 
        return minimax(board)
            
    def name(self):
        return {"nombre": "Maximo", "apellido": "Videla", "legajo": "45602"}
    
    def __str__(self):
        return "**Videla**"

