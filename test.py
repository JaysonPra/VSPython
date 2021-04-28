import pygame
import os
pygame.init()
pygame.font.init()

#Window
WIDTH,HEIGHT = 800,600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

#Colours
WHITE = (255,255,255)
BLACK = (0,0,0)

#Images
player_Img = pygame.transform.scale(pygame.image.load(os.path.join('Assets','running.png')),(64,64))

#Others
player_Width = 64
player_Height = 64


def draw(land,player,obstacle): #Drawing on the screen
    WIN.fill(WHITE)
    WIN.blit(player_Img, (player.x,player.y))
    pygame.draw.rect(WIN,BLACK,land)
    pygame.draw.rect(WIN,BLACK,obstacle)

def collision(font):
    
        WIN.fill(WHITE)
        loss_txt = font.render("You lost!",1,BLACK)
        WIN.blit(loss_txt,(WIDTH//2-140, 240))
        pygame.display.update()
        pygame.time.delay(5000)



def main():
    #Main Values
    FPS = 60
    clock = pygame.time.Clock()
    land = pygame.Rect(0,350,WIDTH,250)
    player = pygame.Rect(200,290,player_Width,player_Height)
    obstacle = pygame.Rect(900,310,40,40)
    font = pygame.font.SysFont('comicsans',100)

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
        
        if obstacle.x + 40 > 0:
            obstacle.x -= 5
        else:
            obstacle.x = 900
        
        if player.colliderect(obstacle):
            collision(font)
            main()

        clock.tick(FPS) #FPS
        #Functions
       
        draw(land,player,obstacle)
        pygame.display.update()

main()