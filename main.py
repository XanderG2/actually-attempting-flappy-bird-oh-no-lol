import pygame
import sys
import random

pygame.init()
pygame.font.init()
width, height = 900, 500 #height must be above 201...
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (254, 254, 51)
blue = (0,0,255)
lightblue = (0, 155, 255)
green = (0,255,0)
textfont = pygame.font.SysFont("comicsans", 12)

def createPipe(type):
    if type == "bottom":
        pipeheight = height//2 - random.randint(50, 200)
        return pygame.Rect(width-50, height-pipeheight, 50, height-pipeheight)
    elif type == "top":
        return pygame.Rect(width-50, 0, 50, height//2 - random.randint(50, 200))

while True:
    bird = pygame.Rect(200, height//2-50//2, 50, 50)
    pipe = createPipe("bottom")
    pipe2 = createPipe("top")
    score = 0
    vel = 0
    pipevel = 10
    gravity = 0.5
    fps = 60
    clock = pygame.time.Clock()
    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                vel = -10
        vel += gravity
        bird.y += vel
        pipe.x -= pipevel
        pipe2.x -= pipevel
        if bird.y <= 0:
            print(score)
            break
        elif bird.y + bird.height >= height:
            print(score)
            break
        if pipe.x + pipe.width <= 0:
            pipe = createPipe("bottom")
        if pipe2.x + pipe2.width <= 0:
            pipe2 = createPipe("top")
        screen.fill(lightblue)
        pygame.draw.rect(screen, yellow, (bird.x, bird.y, bird.width, bird.height))
        pygame.draw.rect(screen, green, (pipe.x, pipe.y, pipe.width, pipe.height))
        pygame.draw.rect(screen, green, (pipe2.x, pipe2.y, pipe2.width, pipe2.height))
        text = textfont.render(str(score), True, black)
        if pygame.Rect.colliderect(bird, pipe) or pygame.Rect.colliderect(bird, pipe2):
            print(score)
            break
        elif bird.x == pipe.x:
            score += 1
        screen.blit(text, text.get_rect())
        pygame.display.flip()