import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.meteor import Meteor
from dino_runner.utils.constants import * 

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):

        if len(self.obstacles) == 0:
            random_obstacle = random.randint(0, 3) #Random para decidir qual objeto irá aparecer
            #Possibilidades: 
            if random_obstacle == 0:            
                self.obstacles.append(Cactus(SMALL_CACTUS, 320))
            elif random_obstacle == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS, 300))
            elif random_obstacle == 2:
                self.obstacles.append(Bird(BIRD))
            elif random_obstacle == 3:
                self.obstacles.append(Meteor(METEOR))    

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)    #Mover para esquerda e deletar.
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                game.death_count += 1
                break
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
       self.obstacles.clear()        