import numpy as np

class RandomAgent():
    def action(self, board):
        return np.random.choice(np.flatnonzero(board == 0))
    
    def name(self):
        return {'nombre': 'Random', 'apellido': 'Agent', 'legajo': 0}
    
    def __str__(self):
        return 'Random'