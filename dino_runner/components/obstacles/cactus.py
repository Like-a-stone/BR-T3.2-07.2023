from dino_runner.components.obstacles.obstacle import Obstacle 
import random

class Cactus(Obstacle):
    def __init__(self, images, POS_Y):    
        self.type = random.randint(0,2) #Imagem aleatória
        super().__init__(images, self.type)
        self.rect.y = POS_Y  #Posição de definida pelo parametro.   
   

        

  
