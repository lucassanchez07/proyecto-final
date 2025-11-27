import pyxel

class Paquete:
    def __init__(self):
        self.posicion_x = 249
        self.posicion_y = 102
        self.velocidad = 1
        self.altura = [102,85,68,51,34]
    def draw(self):
        pyxel.blt(self.posicion_x, self.posicion_y, 0, 48, 0, 16, 16, 0 )
        
    def move(self): #con esto movemos el paquete hacia la derecha y hacia la izqueirda dependiendo del piso
        if self.posicion_y == self.altura[0] or self.posicion_y == self.altura[2] or self.posicion_y == self.altura[4]:
            self.posicion_x -= self.velocidad
        elif self.posicion_y == self.altura[1] or self.posicion_y == self.altura[3]:
            self.posicion_x += self.velocidad

    def subir(self,mario,luigi):
        if mario.posicion == 1 and self.posicion_y == self.altura[0] and self.posicion_x == 205:
            mario.coger()
            self.posicion_x = 148
        elif luigi.posicion == 1 and self.posicion_y == self.altura[0] and self.posicion_x == 82:
            self.posicion_x = 92 
            self.posicion_y = self.altura[1]