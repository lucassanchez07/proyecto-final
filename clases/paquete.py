import pyxel


class Paquete:
    def __init__(self):
        self.posicion_x = 249
        self.posicion_y = 102
        self.velocidad = 1
        self.pisos = [102,85,68,51,34]
        self.caerse = False
        self.contador_malo=0


    def draw(self,luigi): #PINTAMOS POR RANGOS LOS PAQUETES (no en un punto exacto)
        if self.caerse == True:
            #self.posicion_y += self.velocidad (LUCAS)
            pyxel.blt(self.posicion_x, self.posicion_y, 0, 48, 64, 16, 16, 7)
        
        if self.posicion_x<=249 and self.posicion_x >= 118 and self.posicion_y==self.pisos[0]:
            pyxel.blt(self.posicion_x, self.posicion_y, 0, 48, 0, 16, 16, 0 )

        elif self.posicion_x<=118 and self.posicion_y==self.pisos[0] or self.posicion_x<=118 and self.posicion_y==self.pisos[1] :
            pyxel.blt(self.posicion_x, self.posicion_y, 0, 48, 16, 16, 16, 0 )

        elif self.posicion_x >= 118 and self.posicion_y==self.pisos[1] or self.posicion_x >= 118 and self.posicion_y==self.pisos[2] :
            pyxel.blt(self.posicion_x, self.posicion_y, 0, 48, 32, 16, 16, 0 )

        elif self.posicion_x <= 118 and self.posicion_y==self.pisos[2] or self.posicion_x <= 118 and self.posicion_y==self.pisos[3] :
            pyxel.blt(self.posicion_x, self.posicion_y, 0, 64, 0, 16, 16, 0 )

        elif self.posicion_x >= 118 and self.posicion_y==self.pisos[3] or self.posicion_x >= 118 and self.posicion_y==self.pisos[4]:
            pyxel.blt(self.posicion_x, self.posicion_y, 0, 64, 16, 16, 16, 0 )

        elif self.posicion_x <= 118 and self.posicion_y==self.pisos[4] and self.posicion_x > 70 and self.posicion_y==self.pisos[4]:
            pyxel.blt(self.posicion_x, self.posicion_y, 0, 64, 32, 16, 16, 0 )
        #DE ARRIBA A LA POSICION 1 
        #elif self.posicion_x <= 70  and self.posicion_y == self.pisos[4]:
            #pyxel.blt(234, 102, 0, 48, 0, 16, 16, 0 )
        elif self.contador_malo ==1:
            pyxel.blt( 225, 81, 0, 0, 16, 16, 16, 0)
            
        elif self.contador_malo ==2:
            pyxel.blt( 8, 125, 0, 80, 0, 16, 16, 0)

        elif self.contador_malo == 3:
            pass
            
    def move(self): #con esto movemos el paquete hacia la derecha y hacia la izqueirda dependiendo del piso
        if self.posicion_y == self.pisos[0] or self.posicion_y == self.pisos[2] or self.posicion_y == self.pisos[4]:
            self.posicion_x -= self.velocidad
        elif self.posicion_y == self.pisos[1] or self.posicion_y == self.pisos[3]:
            self.posicion_x += self.velocidad

    def subir(self,mario,luigi,camion):
        if mario.posicion == 1 and self.posicion_y == self.pisos[0] and self.posicion_x == 205:
            mario.coger()
            self.posicion_x = 148
        elif mario.posicion != 1 and self.posicion_y == self.pisos[0] and self.posicion_x == 205:
            self.caer()

        if luigi.posicion == 1 and self.posicion_y == self.pisos[0] and self.posicion_x == 70:#EL INICIAL ERA 82 Y LO HEMOS CAMBIADO A 70 PARA QUE NO COINCIDA 
            self.posicion_x = 92 
            self.posicion_y = self.pisos[1]
        elif luigi.posicion != 1 and self.posicion_y == self.pisos[0] and self.posicion_x == 70:
            self.caer()


        #otro piso
        if mario.posicion == 2 and self.posicion_y == self.pisos[1] and self.posicion_x == 171:
            self.posicion_x = 148
            self.posicion_y = self.pisos[2]
        elif mario.posicion != 2 and self.posicion_y == self.pisos[1] and self.posicion_x == 171:
            self.caer()

        if luigi.posicion == 2 and self.posicion_y == self.pisos[2] and self.posicion_x == 70:
            self.posicion_x = 92
            self.posicion_y = self.pisos[3]  
        elif luigi.posicion != 2 and self.posicion_y == self.pisos[2] and self.posicion_x == 70:
            self.caer()

        #otro piso 3
        if mario.posicion == 3 and self.posicion_y == self.pisos[3] and self.posicion_x == 171:
            self.posicion_x = 148
            self.posicion_y = self.pisos[4]
        elif mario.posicion != 3 and self.posicion_y == self.pisos[3] and self.posicion_x == 171:
            self.caer()
        
        if luigi.posicion == 3 and self.posicion_y == self.pisos[4] and self.posicion_x == 70:
            camion.contador_camion +=1
        elif luigi.posicion != 3 and self.posicion_y == self.pisos[4] and self.posicion_x == 70:
            self.caer()

    def caer(self): # MARGENES CON EL OBJETIVO DE QUE LA BOLA NO SE MUEVA HACIA LOS LADOS
        if self.posicion_y < 130 :
            if self.posicion_x > 118 and self.posicion_x < 171:
                self.posicion_x += 1
            elif self.posicion_x < 118 and self.posicion_x > 70:
                self.posicion_x -= 1
            self.caerse = True

            self.posicion_y += self.velocidad
            
            
        if self.posicion_y >= 130:
            self.contador_malo+=1
            self.caerse = False



        



        