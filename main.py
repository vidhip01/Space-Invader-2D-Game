import pygame
from pygame import mixer #a class which handles all kinds of music and sounds
import random
import math

#initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))

#background
background = pygame.image.load("background.png")

#background music
mixer.music.load("backgroundm.wav")
mixer.music.play(-1)


#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load("player.png")
playerX = 345
playerY = 450
playerX_change = 25

# Enemy
enemyImg =[]
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 7

for i in range(num_of_enemies):         #for loops running 6 times
    enemyImg.append(pygame.image.load("enemy.png")) # dot append to add them to the list
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(10)

# Bullet

# Ready- We can't see the bullet on screen
# Fire - The bullet is currently moving
bulletImg = pygame.image.load("bullet1.png")
bulletX = 0
bulletY = 400
bulletX_change = 0
bulletY_change = 15
bullet_state = "ready"


# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf",32)
textX = 10
textY = 10


# Game over Text
over_font = pygame.font.Font("freesansbold.ttf" , 64)


def show_score(x,y):
    score = font.render("Score : " + str(score_value), True , (255,255,255))
    screen.blit(score,(x, y))


def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y , i):
    screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg ,(x +16, y + 10)) #  x coordinate So that bullet will appear on the center of the spaceship
                                             # y coordinate so that it will appear a little above spaceship

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt( (math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True #collision has occured
    else:
        return


def game_over_text():
    over_text = over_font.render("GAME OVER" , True , (255,255,255))
    screen.blit(over_text, (200,250))








#Game Loop
running = True
while running:
    # RGB- Red green blue
    screen.fill((0, 0, 0))

    #background image
    screen.blit(background,(0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
        # if keyboard is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:

            if event.key ==pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_Sound = mixer.Sound("laser.wav")
                    bullet_Sound.play()
                    # Get the current x coordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    # example 5 = 5 + (-0.1) = 4.95  so do not worry about

    #boundary check so that it doesn't go out of the screen
    playerX += playerX_change
    if playerX <=0:
        playerX= 0
    elif playerX >= 695:
        playerX = 695

    # Enemy Movement
    for i in range(num_of_enemies):

        #Game mover
        if enemyY[i] > 400:
            for j in range(num_of_enemies):
                enemy[j] = 2000
            game_over_text()
            break



        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 8
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 726:
            enemyX_change[i] = -8
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_Sound = mixer.Sound("explosion.wav")
            explosion_Sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1

            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i],i)

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state ='ready'

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change





    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()


























