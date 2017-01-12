#######################
#  SNAKE BY WOJTEK G. #
#######################
import pygame, sys, random

pygame.init()

GAME_WINDOW = pygame.display.set_mode((700, 700), 0, 32)

pygame.display.set_caption("Snake")

# globanie ###################################
snakeX = [315,350,385] + [-1]*70
snakeY = [315,315,315] + [-1]*70
SNAKE_LENGHT = 3
FIELD_SIZE = 35
EAT = True
SCORE = 0
appleX = random.randint(2, 19) * FIELD_SIZE
appleY = random.randint(2, 19) * FIELD_SIZE
X_change = -FIELD_SIZE
Y_change = 0
clock = pygame.time.Clock()
LEVEL = 7
start = 0
HS = 0
###############################################

# wypisujemy winik
def draw_score():
    fontObj = pygame.font.Font('freesansbold.ttf', 16)
    text = 'Score: ' + str(SCORE)
    text_obr = fontObj.render(text, True, (255, 255, 255))
    text_prost = text_obr.get_rect()
    text_prost.center = (600, 692)
    GAME_WINDOW.blit(text_obr, text_prost)

def highscore():
    fontObj = pygame.font.Font('freesansbold.ttf', 16)
    text = 'Highscore: ' + open('highscore.txt').read()
    HS = open('highscore.txt').read()
    text_obr = fontObj.render(text, True, (255, 255, 255))
    text_prost = text_obr.get_rect()
    text_prost.center = (100, 692)
    GAME_WINDOW.blit(text_obr, text_prost)

# robimy okno gry
def draw_game_window():
    GAME_WINDOW.fill((0, 0, 15))
    pygame.draw.rect(GAME_WINDOW,(150,0,0),((0,0),(700,700)),FIELD_SIZE)

# wypisuje wynik na koncu
def draw_end_score():
    fontObj = pygame.font.Font('freesansbold.ttf', 64)
    text = 'Your score is: ' + str(SCORE)
    text_obr = fontObj.render(text, True, (255, 255, 255))
    text_prost = text_obr.get_rect()
    text_prost.center = (350, 350)
    GAME_WINDOW.blit(text_obr, text_prost)
    pygame.display.update()

# rysujemy snake'a
def draw_snake():
    color = 150
    for i in range(0,SNAKE_LENGHT) :
        if i == 0 :
            pygame.draw.circle(GAME_WINDOW, (0, 0, 200), (snakeX[i], snakeY[i]), 17)
        else :
            pygame.draw.circle(GAME_WINDOW, (0, 0, color), (snakeX[i], snakeY[i]), 17)
            color -= 2

# losuje jablko
def apple():
    global appleX
    global appleY
    if EAT == True :
        appleX = random.randint(2, 19) * FIELD_SIZE
        appleY = random.randint(2, 19) * FIELD_SIZE
        pygame.draw.circle(GAME_WINDOW, (0, 0, 255), (appleX, appleY), 10)
            #zabezpieczamy przed losowaniem jablka na wezu
            #for i in range (0,SNAKE_LENGHT):
               # if appleX == snakeX[i] or appleY == snakeY[i]:
                 #   n = False
    #rysuje jalbko
    pygame.draw.circle(GAME_WINDOW, (0, 150, 0), (appleX, appleY), 10)
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
        global LEVEL
        # move jest tak zrobiony, ze wystarczy zwiekszyc wielkosc weza i nastepna czesc sie dodaje
        SNAKE_LENGHT += 1
        SCORE += 1 # wynik
        LEVEL += 0.5
        return True

# funkcja ktora odpowiada za przywalenie w sciane lub siebie
def collide():
    if snakeX[0] == 0 or snakeX[0] == 700 or snakeY[0] == 0 or snakeY[0] == 700:
        draw_end_score()
        pygame.time.delay(3000)
        if HS < SCORE :
            open('highscore.txt', 'w').write(str(SCORE))
        return 1
    for i in range (1,SNAKE_LENGHT):
        if snakeX[0] == snakeX[i] and snakeY[0] == snakeY[i]:
            draw_end_score()
            pygame.time.delay(3000)
            if HS < SCORE:
                open('highscore.txt', 'w').write(str(SCORE))
            return 1

# konczymy program
def exit():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

# glowna petla
while True :
    start = 0
    SNAKE_LENGHT = 3
    snakeX = [315, 350, 385] + [-1] * 70
    snakeY = [315, 315, 315] + [-1] * 70
    X_change = -FIELD_SIZE
    Y_change = 0
    SCORE = 0
    LEVEL = 7
    while start != 1 :
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

        start = collide()
        move(X_change,Y_change)
        GAME_WINDOW.fill((0, 0, 0))
        draw_game_window()
        draw_snake()
        EAT = apple()
        EAT = eat_apple()
        draw_score()
        highscore()
        pygame.display.update()
        clock.tick(LEVEL)