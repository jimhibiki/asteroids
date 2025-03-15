# this allows us to use code from
# the open-source pygame library
# throughout this file
# cd ~/workspace/github.com/jimhibiki/asteroids
# source venv/bin/activate  (to leave type deactivate)
# MAN I STRUGGLED WITH THIS.  So... always activate the virtual environment: source venv/bin/activate
# Run VcXsrv
# Also, not sure if it was needed but added the following to ~/.bashrc
# export DISPLAY=$(ip route list default | awk '{print $3}'):0
# export LIBGL_ALWAYS_INDIRECT=1
import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    asteroids=pygame.sprite.Group()
    shots=pygame.sprite.Group()
    Asteroid.containers=(asteroids, updatable, drawable)
    Shot.containers=(shots, updatable, drawable)
    Player.containers=(updatable,drawable)
    AsteroidField.containers=(updatable)
    linf=1
    black=[0,0,0]
    dt=0
    clock=pygame.time.Clock()
    
    asteroidfield=AsteroidField()
    player=Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while linf==1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        player.shot_timer-=dt
        for asteroid in asteroids:
            if asteroid.collision(player)==True:
                print('Game over!')
                sys.exit()
            for shot in shots:
                if asteroid.collision(shot)==True:
                    asteroid.split()
                    shot.kill()
        pygame.Surface.fill(screen,black)
        #player.update(dt)
        #player.draw(screen)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        # limit the framerate to 60 FPS
        dt=clock.tick(60)/1000
        


if __name__ == "__main__":
    main()
