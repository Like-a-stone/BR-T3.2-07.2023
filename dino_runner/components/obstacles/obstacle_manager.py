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
            random_obstacle = random.randint(0, 4) 
            if random_obstacle == 0:            
                self.obstacles.append(Cactus(SMALL_CACTUS, 320))
                self.item = 1
            elif random_obstacle == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS, 300))
                self.item = 1
            elif random_obstacle == 2:
                self.obstacles.append(Bird(BIRD))
                self.item = 2
            elif random_obstacle == 3:
                self.obstacles.append(Bird(BIRD2))
                self.item = 2
            elif random_obstacle == 4:
                self.obstacles.append(Meteor(METEOR))
                self.item = 4    

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    DEATH_SOUND.play()
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count+=1
                    break 
                elif game.player.has_power_up:
                    if game.player.type == HAMMER_TYPE and self.item == 1: 
                        self.obstacles.remove(obstacle)
                    elif game.player.type == SHIELD_TYPE and self.item == 2:
                        self.obstacles.remove(obstacle)
                    else:
                        game.player.type = DEFAULT_TYPE
                        DEATH_SOUND.play()
                        pygame.time.delay(500)
                        game.playing = False
                        game.death_count+=1
                        break

    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
       self.obstacles.clear()