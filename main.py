import pygame, sys, random

pygame.init()

GAME_WINDOW = pygame.display.set_mode((700, 700), 0, 32)

pygame.display.set_caption("Snake")

snakeX = [315,350,385] + [0]*70
snakeY = [315,315,315] + [0]*70
SNAKE_LENGHT = 3
FIELD_SIZE = 35
EAT = True
appleX = random.randint(2,20) * FIELD_SIZE
appleY = random.randint(2,20) * FIELD_SIZE

def draw_game_window():
    GAME_WINDOW.fill((0, 0, 0))
    pygame.draw.rect(GAME_WINDOW,(255,0,0),((0,0),(700,700)),FIELD_SIZE)

def draw_snake():
    for i in range(0,SNAKE_LENGHT) :
        pygame.draw.circle(GAME_WINDOW,(0,0,255),(snakeX[i],snakeY[i]),17)

def apple(appleX,appleY):
    if EAT == True:
        appleX = random.randint(2,20) * FIELD_SIZE
        appleY = random.randint(2,20) * FIELD_SIZE
    pygame.draw.circle(GAME_WINDOW, (255, 0, 0), (appleX, appleY), 10)
    return False

def move():
    if event.type == pygame.KEYDOWN:
        #strzałka w górę
        if event.key == pygame.K_UP:
            pomX = snakeX[0]
            pomY = snakeY[0]
            snakeY[0] -= FIELD_SIZE
            for i in range(1, SNAKE_LENGHT):
                pomY, snakeY[i] = snakeY[i], pomY
                pomX, snakeX[i] = snakeX[i], pomX
        #strzałka w dół
        if event.key == pygame.K_DOWN:
            pomX = snakeX[0]
            pomY = snakeY[0]
            snakeY[0] += FIELD_SIZE
            for i in range(1, SNAKE_LENGHT):
                pomY, snakeY[i] = snakeY[i], pomY
                pomX, snakeX[i] = snakeX[i], pomX
        #strzalka w lewo
        if event.key == pygame.K_LEFT:
            pomX = snakeX[0]
            pomY = snakeY[0]
            snakeX[0] -= FIELD_SIZE
            for i in range(1, SNAKE_LENGHT):
                pomY, snakeY[i] = snakeY[i], pomY
                pomX, snakeX[i] = snakeX[i], pomX
        #strzalka w prawo
        if event.key == pygame.K_RIGHT:
            pomX = snakeX[0]
            pomY = snakeY[0]
            snakeX[0] += FIELD_SIZE
            for i in range(1, SNAKE_LENGHT):
                pomY, snakeY[i] = snakeY[i], pomY
                pomX, snakeX[i] = snakeX[i], pomX

def eat_apple(EAT,SNAKE_LENGHT):
    if snakeX[0] == appleX and snakeY[0] == appleY:
        EAT = True
        snakeX[SNAKE_LENGHT] = snakeX[SNAKE_LENGHT - 1]
        snakeY[SNAKE_LENGHT] = snakeY[SNAKE_LENGHT - 1]
        SNAKE_LENGHT += 1

def exit():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

while 1:
    for event in pygame.event.get():
        exit()
        move()
        eat_apple(EAT,SNAKE_LENGHT)

    GAME_WINDOW.fill((0, 0, 0))
    draw_game_window()
    draw_snake()
    EAT = apple(appleX, appleY)
    pygame.display.update()