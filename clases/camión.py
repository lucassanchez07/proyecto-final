import pyxel
class camion:
    def __init__(self):
        self.x_inicial = 2
        self.posicion_x = self.x_inicial
        self.posicion_y = 62
        self.paquetes = 0
        self.contador_camion = 0
    
    def draw(self,paquete):#HEMOS PINTADO UN CAMION ENCIMA DE OTRO
        if self.contador_camion == 0:
            pyxel.blt(self.posicion_x, self.posicion_y, 0, 0, 56, 32, 32, 0)

        for i in range(3):
            
            if self.contador_camion == 1:
                    pyxel.blt(self.posicion_x, self.posicion_y, 0, 0, 88, 32, 32, 0 )

            elif self.contador_camion == 2:
                    pyxel.blt(self.posicion_x, self.posicion_y, 0, 0, 120, 32, 32, 0 )

            elif self.contador_camion == 3:
                    pyxel.blt(self.posicion_x, self.posicion_y, 0, 0, 152, 32, 32, 0 )
        
            elif self.contador_camion == 4:
                    pyxel.blt(self.posicion_x, self.posicion_y, 0, 0, 184, 32, 32, 0 )

            elif self.contador_camion == 5:
                    pyxel.blt(self.posicion_x, self.posicion_y, 0, 0, 216, 32, 32, 0 )
        
            elif self.contador_camion == 6:
                    pyxel.blt(self.posicion_x, self.posicion_y, 0, 48, 216, 32, 32, 0 )
        
            elif self.contador_camion == 7:
                    pyxel.blt(self.posicion_x, self.posicion_y, 0, 48, 176, 32, 32, 0 )
        
            elif self.contador_camion == 8:
                    pyxel.blt(self.posicion_x, self.posicion_y, 0, 48, 144, 32, 32, 0 )

            elif self.contador_camion == 9:
                    pyxel.blt(self.posicion_x, self.posicion_y, 0,168, 0, 48, 48, 0 )

            elif self.contador_camion == 10:
                   self.contador_camion=1