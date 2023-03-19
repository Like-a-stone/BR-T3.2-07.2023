
import random
from dino_runner.components.obstacles.obstacle import Obstacle 

class Bird(Obstacle):
    random_POS= [260, 200]
    def __init__(self, images): #images[0,1]
        random_POS= [260, 200]
        self.type =0
        super().__init__(images, self.type)
        self.rect.y = random.choice(random_POS)
  
          


        