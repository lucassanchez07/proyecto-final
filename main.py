import pyxel
SCREEN_WIDTH = 256
SCREEN_HEIGHT = 144
class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH,SCREEN_HEIGHT, title = "Mario Bros 1983")
        pyxel.images[1].load(0,0,"assets/fondo.png")
        pyxel.run(self.update,self.draw)
    
    
    def update(self):
        # Este método se llama en cada frame para ACTUALIZAR la lógica del juego.
        # Aquí es donde iría:
        # 1. El manejo de la entrada del usuario (teclas de Mario y Luigi).
        # 2. El cálculo de la posición de los personajes y paquetes.
        # 3. La detección de colisiones y caídas de paquetes.
        # 4. La actualización de la puntuación y el tiempo.
        pass # 'pass' indica que el método está vacío por ahora.

    def draw(self):
        # Dibujo: todo lo que se ve en pantalla
        pyxel.cls(0) # Borra la pantalla al negro
        # Limpia la pantalla completa. El número '0' es el código del color 
        # negro en la paleta de Pyxel (el color de fondo inicial).
        
        # pyxel.blt(x_destino, y_destino, img_banco, x_origen, y_origen, ancho, alto)
        pyxel.blt(0,0,1,0,0,SCREEN_WIDTH,SCREEN_HEIGHT)

app = App()
#HASTA AQUI ENTENDIDO


