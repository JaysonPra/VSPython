import pygame
import os
import random
pygame.init()
pygame.font.init()
pygame.mixer.init()

#Window
WIDTH,HEIGHT = 800,600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Dinosaur Game Rip Off")
icon = pygame.transform.scale(pygame.image.load(os.path.join('Assets','icon.png')),(32,32))
pygame.display.set_icon(icon)

#Colours
WHITE = (255,255,255)
BLACK = (0,0,0)

#Images
player_Img = pygame.transform.scale(pygame.image.load(os.path.join('Assets','running.png')),(64,64))
bird_Img = pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('Assets','dove.png')),(40,40)),True,False)

#music
pygame.mixer.music.load(os.path.join('Assets','background_music.mp3'))

#Others
player_Width = 64
player_Height = 64


def draw(land,player,score_font,score_count): #Drawing on the screen
    WIN.fill(WHITE)
    WIN.blit(player_Img, (player.x,player.y))
    pygame.draw.rect(WIN,BLACK,land)
    score_txt = score_font.render("Score: " + str(score_count), 1, BLACK)
    WIN.blit(score_txt, (660,20))
    
def obs(on_screen):
    rng = random.randint(1,3)
    if rng == 1:
        on_screen.append("B")
    elif rng > 1:
        on_screen.append("O")

def Enemy(on_screen,obstacle,bird,VEL,player,font,score_count):
    if len(on_screen) == 0:
            obs(on_screen)
    if len(on_screen) != 0 and on_screen[0] == "O":
            pygame.draw.rect(WIN, BLACK, obstacle)
            if obstacle.x + 40 > 0:
                obstacle.x -= VEL
            else:
                on_screen.pop()
                obstacle.x = 900
    if len(on_screen) != 0 and on_screen[0] == "B":
        WIN.blit(bird_Img, (bird.x,bird.y))
        if bird.x + 40 > 0:
            bird.x -= VEL
        else:
            on_screen.pop()
            bird.x = 900

    if player.colliderect(obstacle) or player.colliderect(bird):
        collision(font,score_count)
        main()
         
def collision(font,score_count):
    WIN.fill(WHITE)
    loss_txt = font.render("You lost!",1,BLACK)
    WIN.blit(loss_txt,(WIDTH//2-140, 240))

    losing_score_font = pygame.font.SysFont('comicsans', 100)
    losing_score_txt = losing_score_font.render("Score: " + str(score_count), 1, BLACK)
    WIN.blit(losing_score_txt,(WIDTH//2-140,320))

    pygame.display.update()
    pygame.mixer.music.stop()
    pygame.time.delay(5000)

def main():
    pygame.mixer.music.play(-1) #music
    #Main Values
    FPS = 60
    clock = pygame.time.Clock()
    land = pygame.Rect(0,350,WIDTH,250)
    player = pygame.Rect(200,290,player_Width,player_Height)
    obstacle = pygame.Rect(900,310,40,40)
    bird = pygame.Rect(900,200,40,40)
    font = pygame.font.SysFont('comicsans',100)
    score_font = pygame.font.SysFont('comicsans',40)
    score_count = 0
    on_screen = []
    VEL = 10

    isJump = False
    jump_count = 7

    while True: #Game Loop
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    isJump = True

        if isJump:
            if jump_count >= -7:
                player.y -= (jump_count*abs(jump_count)) * 0.5
                jump_count -= 0.5
            else:
                jump_count = 7
                isJump = False
                player.y = 290
        
        if player.x == obstacle.x + 10 or player.x == bird.x + 10:
            score_count += 1
        clock.tick(FPS) #FPS

        #Functions
        draw(land,player,score_font,score_count)
        Enemy(on_screen,obstacle,bird,VEL,player,font,score_count)
        pygame.display.update()

main()