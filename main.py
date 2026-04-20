import pygame
from constants import *
from player import *
from logger import log_state
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)



    player1 = Player(x = SCREEN_WIDTH / 2,y = SCREEN_HEIGHT / 2)

    clock = pygame.time.Clock()
    dt = 0

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                return
        screen.fill("black")

        updatable.update(dt)

        for drawing in drawable:
            drawing.draw(screen)


        pygame.display.flip()
        # frame limit
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
