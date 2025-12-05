import pyxel

class camion:
    def __init__(self):
        #self.x_inicial = 2
        self.pos_x = 2
        self.pos_y = 54
        self.paquetes = 0
    
    def draw(self,luigi,paquete):
        pyxel.blt(self.pos_x, self.pos_y, 0, 0, 48, 32, 32, 0)
        if  luigi.posicion == 3 and paquete.posicion_x == 70  and paquete.posicion_y != paquete.pisos[4]:
            pyxel.blt(self.posicion_x, self.posicion_y, 0, 0, 64, 32, 32, 0 )