import pygame, sys, random

pygame.init()

GAME_WINDOW = pygame.display.set_mode((700, 700), 0, 32)

pygame.display.set_caption("Snake")

snakeX = [315,350,385] + [1]*70
snakeY = [315,315,315] + [1]*70
SNAKE_LENGHT = 3
FIELD_SIZE = 35
EAT = True
appleX = random.randint(2,19) * FIELD_SIZE
appleY = random.randint(2,19) * FIELD_SIZE
SCORE = 0
X_change = 0
Y_change = 0

# wypisujemy winik
def draw_score():
    fontObj = pygame.font.Font('freesansbold.ttf', 16)
    text = 'Score: ' + str(SCORE)
    text_obr = fontObj.render(text, True, (255,255,255))
    text_prost = text_obr.get_rect()
    text_prost.center = (600, 692)
    GAME_WINDOW.blit(text_obr, text_prost)
# robimy okno gry
def draw_game_window():
    GAME_WINDOW.fill((0, 0, 0))
    pygame.draw.rect(GAME_WINDOW,(255,0,0),((0,0),(700,700)),FIELD_SIZE)
# rysujemy snake'a
def draw_snake():
    for i in range(0,SNAKE_LENGHT) :
        pygame.draw.circle(GAME_WINDOW,(0,0,255),(snakeX[i],snakeY[i]),17)
# losuje jablko
def apple():
    global appleX
    global appleY
    if EAT == True:
        pygame.draw.circle(GAME_WINDOW, (0, 0, 0), (appleX, appleY), 10)
        appleX = random.randint(2,19) * FIELD_SIZE
        appleY = random.randint(2,19) * FIELD_SIZE
        #zabezpieczamy przed losowaniem jablka na wezu
        for i in range (0,SNAKE_LENGHT):
            if appleX == snakeX[i] or appleY == snakeY[i]:
                apple()
    #rysuje jalbko
    pygame.draw.circle(GAME_WINDOW, (0, 255, 0), (appleX, appleY), 10)
    return False
#funkcja odpowiedzialna za poruszanie sie
def move(X_change,Y_change):
    pomX = snakeX[0]
    pomY = snakeY[0]
    snakeX[0] += X_change
    snakeY[0] += Y_change
    for i in range(1, SNAKE_LENGHT):
        pomY, snakeY[i] = snakeY[i], pomY
        pomX, snakeX[i] = snakeX[i], pomX
# funkcja ktora mowi co sie dzieje po zjedzeniu jablka
def eat_apple():
    if snakeX[0] == appleX and snakeY[0] == appleY:
        global SNAKE_LENGHT
        global SCORE
        # move jest tak zrobiony, ze wystarczy zwiekszyc wielkosc weza i nastepna czesc sie dodaje
        SNAKE_LENGHT += 1
        SCORE += 1 # wynik
        return True
# funkcja ktora odpowiada za przywalenie w sciane lub siebie
def collide():
    if snakeX[0] == 0:
        sys.exit()
    if snakeX[0] == 700:
        sys.exit()
    if snakeY[0] == 0:
        sys.exit()
    if snakeY[0] == 700:
        sys.exit()
    for i in range (1,SNAKE_LENGHT):
        if snakeX[0] == snakeX[i] and snakeY[0] == snakeY[i]:
            sys.exit()
# konczymy program
def exit():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
#glowna petla
while True:
    for event in pygame.event.get():
        pressed_key = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Y_change = -FIELD_SIZE
                X_change = 0
            if event.key == pygame.K_DOWN:
                Y_change = FIELD_SIZE
                X_change = 0
            if event.key == pygame.K_LEFT:
                X_change = -FIELD_SIZE
                Y_change = 0
            if event.key == pygame.K_RIGHT:
                X_change = FIELD_SIZE
                Y_change = 0
        exit()
        #collide()

    FPS = 30
    fpsClock = pygame.time.Clock()
    pygame.time.wait(500)
    move(X_change,Y_change)
    GAME_WINDOW.fill((0, 0, 0))
    draw_game_window()
    draw_snake()
    EAT = eat_apple()
    EAT = apple()
    draw_score()
    fpsClock.tick(FPS)
    pygame.display.update()