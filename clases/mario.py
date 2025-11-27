import pyxel

class Mario:
    def __init__(self):
        self.posicion = 1 
        self.posicion_x = 182
        self.posicion_y = 109
        self.posicion_2_y = 79
        self.posicion_3_y = 45
        self.tiempo = 0
    def draw(self):
        #pyxel.blt(destino del eje x, destino del eje y , imagen, origen eje x, origen eje y , el numero de bites que coje del eje x
        #lo mismo pero en el eje y , para que el fondo NO sea negro
        if self.tiempo > 0:
            self.tiempo -= 1
            pyxel.blt(self.posicion_x, self.posicion_y, 0, 0, 32, 16, 16, 0) 
        else:
            if self.posicion == 1:
                pyxel.blt(self.posicion_x, self.posicion_y, 0, 32, 0, 16, 16, 0) 
            if self.posicion == 2:
                pyxel.blt(self.posicion_x, self.posicion_2_y, 0, 0, 32, 16, 16, 0) 
            if self.posicion == 3:
                pyxel.blt(self.posicion_x, self.posicion_3_y, 0, 0, 32, 16, 16, 0) 
    def move(self):# btn regresa true si KEY se presiona
        if pyxel.btnp(pyxel.KEY_UP) and self.posicion < 3:
            self.posicion += 1
        elif pyxel.btnp(pyxel.KEY_DOWN) and self.posicion > 1:
            self.posicion -= 1

    def coger(self):
        self.tiempo = 10
