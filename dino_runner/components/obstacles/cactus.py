from dino_runner.components.obstacles.obstacle import Obstacle 
import random

class Cactus(Obstacle):
    def __init__(self, images):
    
        self.type = random.randint(0,2)
        super().__init__(images, self.type)
        self.rect.y = 320    

class CactusLarge(Obstacle):  #Criada Uma class para os Cactus maiores.
    def __init__(self, images):
    
        self.type = random.randint(0,2)
        super().__init__(images, self.type)
        self.rect.y = 300 #Posição alterada para que ambos os cactus fiquem alinhados ao solo.   

        

  
