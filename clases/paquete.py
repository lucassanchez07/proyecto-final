import pyxel

class Paquete:
    def __init__(self):
        self.posicion_x = 152
        self.posicion_y = 102
    
    def draw(self):
        pyxel.blt(self.posicion_x, self.posicion_y, 0, 48, 0, 16, 16, 0 )    
        