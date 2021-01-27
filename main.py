import pygame
import random
import math
pygame.init()
screen = pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)
background = pygame.image.load('sss.jpg')


#Player
playerImg = pygame.image.load('spaceship.png')
playerx=370
playery=540
playerx_change = 0
playery_change = 0

#Bullet
bulletImg = pygame.image.load('bullet.png')
bulletx=0
bullety=0
bullet_change = 0.4
bullet_state = "ready"
#score
score_value=0
font =pygame.font.Font("freesansbold.ttf",32)
scorex = 10
scorey = 10

#enemy
enemyImg =[]
enemyx=[]
enemyy=[]
enemyx_change = []
enemyy_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('penis.png'))
    enemyx.append(random.randint(0,800))
    enemyy.append(40)
    enemyx_change.append(0.3)
    enemyy_change.append(0.2)
def show_score(x,y):
    score = font.render("Score:"+str(score_value),True,(255,255,255))
    screen.blit(score, (x, y))

def player(x,y):
    screen.blit(playerImg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+10,y+10))
def isCollision(enemyx,enemyy,bulletx,bullety):
    distance = math.sqrt((math.pow(enemyx - bulletx,2))+(math.pow(enemyy - bullety,2)))
    if distance<27 and bullet_state is not "ready":
        return True
    else:
        return False

#Game Loop
running = True
while running:
      #Red-Green-blue
    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #if keystroke is pressed check whether is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -0.4

            if event.key == pygame.K_RIGHT:
                playerx_change = 0.4

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playery_change = -0.4

            if event.key == pygame.K_DOWN:
                playery_change = 0.4

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready" or "fire":
                    bulletx = playerx
                    bullety = playery
                    fire_bullet(bulletx,playery)



        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT:
                playerx_change = 0
            if event.key == pygame.K_UP or  event.key == pygame.K_DOWN:
                playery_change = 0

        


    playerx +=playerx_change
    playery +=playery_change
    #player boundary conditions

    if playerx <= 0:
        playerx = 0
    elif playerx >= 768:
        playerx = 768
    if playery >= 568:
        playery = 568
    elif playery <= 0:
        playery = 0


    for i in range(num_of_enemies):
        enemyx[i] += enemyx_change[i]
        enemyy[i] += enemyy_change[i]
        if enemyx[i] <= 0:
            enemyx_change[i] = 0.2
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] >= 768:
            enemyx_change[i] = -0.2
            enemyy[i] +=enemyy_change[i]
        if enemyy[i]>=580:
            enemyy_change[i]= -enemyy_change[i]
        elif enemyy[i]<=10:
            enemyy_change[i] = -enemyy_change[i]
        enemy(enemyx[i], enemyy[i],i)
        collision = isCollision(enemyx[i], enemyy[i], bulletx, bullety)
        if collision:
            score_value += 1
            bullety = 480
            bullet_state = "ready"
            enemyx[i]=random.randint(0,730)
            enemyy[i]=random.randint(50,150)

    #display of enemy and player
    if bullety <=0:
        bullety = playery
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletx, bullety)
        bullety = bullety-bullet_change



    player(playerx,playery)
    show_score(scorex,scorey)
    pygame.display.update()
