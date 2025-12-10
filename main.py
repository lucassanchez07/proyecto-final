import pyxel
from clases.mario import Mario
from clases.luigi import Luigi
from clases.paquete import Paquete
from clases.camión import camion

SCREEN_WIDTH = 256
SCREEN_HEIGHT = 144
mario = Mario()
luigi = Luigi()
paquete = Paquete()
camión = camion()

class App:
    def __init__(self):
        
        self.lista_paquetes=[]
        self.tiempo_entre_paquetes = 120
        self.contador_aparicion = 0
        self.ganar_partida = False
        self.puntos = 0 #Contador de puntos
        self.game_over = False
        

        pyxel.init(SCREEN_WIDTH,SCREEN_HEIGHT, title = "Mario Bros 1983")
        pyxel.load("./assets/resources.pyxres")
        pyxel.images[1].load(0,0,"assets/image.png")#Coge el BANCO DE IMÁGENES número 1, y dentro de él, 
#         empezando en la esquina (0, 0), pega el contenido del archivo 'image.png'
        pyxel.run(self.update,self.draw) #abandona el __init__ y comienza el bucle update y draw 
    
    
    def update(self):# Este método se llama en cada frame para ACTUALIZAR la lógica del juego.
        
        if self.game_over == True:#Si no ponemos esto el juego cuando la pantalla esta en negro sigue sumando puntos 
            return
        
        self.contador_aparicion += 1

        if self.contador_aparicion >= self.tiempo_entre_paquetes:
            nuevo_paquete = Paquete()
            self.lista_paquetes.append(nuevo_paquete)
            self.contador_aparicion = 0
            
        mario.move()
        luigi.move()

        for paquete in self.lista_paquetes:
            paquete.move()
            paquete.subir(mario, luigi,self, camión)
            if paquete.caerse == True: #(con el objetivo de que se genere un bucle porque sino la bola se queda quieta y no cae ya que es puntual y solo baja un fotograma)
                paquete.caer()
        
        #Si el camión se llena (llega a 9), sumamos viaje y lo vaciamos
        if camión.contador_camion >= 9:
            camión.viajes_hechos += 1
            camión.contador_camion = 1 # Vaciamos el camión para que empiece de nuevo
        
        # Si llegamos a 3 viajes, ganamos vida
        if camión.viajes_hechos >= 3: 
            # Solo restamos fallo si tenemos alguno (para no tener fallos negativos)
            if camión.fallos > 0:
                camión.fallos -= 1
            
            camión.viajes_hechos = 0 # Reiniciamos el contador de viajes

        

        
    def draw(self):
        # Dibujo: todo lo que se ve en pantalla
        pyxel.cls(0) # Borra la pantalla al negro
        # Limpia la pantalla completa. El número '0' es el código del color 
        # negro en la paleta de Pyxel (el color de fondo inicial).
        
        # pyxel.blt(x_destino, y_destino, img_banco, x_origen, y_origen, ancho, alto)
        pyxel.blt(0,0,1,0,0,SCREEN_WIDTH,SCREEN_HEIGHT)
        
        mario.draw()
        luigi.draw()
        camión.draw()
        
        for paquete in self.lista_paquetes:
          paquete.draw()
        
        pyxel.text(5, 5, f"PUNTOS: {self.puntos}", 0) #Los puntos se pintan aqui

        
        if camión.fallos == 1: #Vidas del jugador(dos jefes y una pantalla negro game over)
            pyxel.blt(225, 79, 0, 0, 16, 16, 16, 0)
        elif camión.fallos == 2:
            pyxel.blt(8, 120, 0, 80, 0, 16, 16, 0)
            pyxel.blt(225, 79, 0, 0, 16, 16, 16, 0)
        elif camión.fallos >= 3:
            self.game_over = True
            pyxel.cls(0)
            pyxel.text(100, 70, "GAME OVER", 4)
            pyxel.text(5, 5, f"PUNTOS: {self.puntos}", 7)
            return
            

App()



