import pyxel

class Luigi:
    def __init__(self):
        self.posicion = 1 
        self.posicion_x = 55
        self.posicion_y = 96
        self.posicion_2_y = 62
        self.posicion_3_y = 28
    
    def draw(self):
        #pyxel.blt(self.posicion_x, self.posicion_y, 0, 32, 0, 16, 16, 0) # imagen, eje x, eje y , el numero de bites que coje del eje x
        if self.posicion == 1:
            pyxel.blt(self.posicion_x, self.posicion_y, 0, 16, 0, 16, 16, 0) 
        if self.posicion == 2:
            pyxel.blt(self.posicion_x, self.posicion_2_y, 0, 16, 0, 16, 16, 0) 
        if self.posicion == 3:
            pyxel.blt(self.posicion_x, self.posicion_3_y, 0, 16, 0, 16, 16, 0) 
         #lo mismo pero en el eje y , para que el fondo NO sea negro
    def move(self):# btn regresa true si KEY se presiona
        if pyxel.btnp(pyxel.KEY_W) and self.posicion < 3:
            self.posicion += 1
        elif pyxel.btnp(pyxel.KEY_S) and self.posicion > 1:
            self.posicion -= 1