import pygame
from constants import *
from player import Player
from logger import log_state, log_event
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys




def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroid_field_group = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)



    player1 = Player(x = SCREEN_WIDTH / 2,y = SCREEN_HEIGHT / 2)
    asteroid_field1 = AsteroidField()


    clock = pygame.time.Clock()
    dt = 0

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                return
        screen.fill("black")

        updatable.update(dt)

        for obj in asteroids:
            for shot in shots:
                if shot.collides_with(obj) == True:
                    log_event("asteroid_shot")
                    shot.kill()
                    obj.split()

            if obj.collides_with(player1) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            



        for drawing in drawable:
            drawing.draw(screen)


        pygame.display.flip()
        # frame limit
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
