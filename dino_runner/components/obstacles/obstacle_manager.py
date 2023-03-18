import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

random_cactus = random.randint(0, 1) 
if random_cactus == 0:
    random_cactus = SMALL_CACTUS # Caso o random retorne 0 os cactus pequenos serão usados
else:
     random_cactus = LARGE_CACTUS # caso seja 1 os cactus grandes serão usados.

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(random_cactus)) #Recebe um dos dois tipos de cacto.

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)    

            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)