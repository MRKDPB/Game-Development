import pygame
pygame.init()
 
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,80,255)
RED = (200,0,0)

brick_sound = pygame.mixer.Sound("mixkit-game-ball-tap-2073.wav")
paddle_sound = pygame.mixer.Sound("mixkit-hard-typewriter-hit-1364.wav")



bricks1=[pygame.Rect(10 + i* 100,60,80,30) for i in range(6)]
bricks2=[pygame.Rect(10 + i* 100,100,80,30) for i in range(6)]
bricks3=[pygame.Rect(10 + i* 100,140,80,30) for i in range(6)]

def draw_brick(brick_list):
    for i in brick_list:
        pygame.draw.rect(screen,RED,i)
  
score = 0

velocity=[1,1]
size = (600, 600)
screen = pygame.display.set_mode(size)
my_image = pygame.image.load('wood-g0c071ddb1_1280.jpg').convert()

 
pygame.display.set_caption("Breakout Game")
paddle=pygame.Rect(300,550,60,15) #(x,y,width,height)
center=(200,200)
radius = 8
ball=pygame.Rect(center[0]-radius, center[1]-radius, radius*2, radius*2)
carryOn = True
while carryOn:
    for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                  carryOn = False # Flag that we are done so we exit this loop             
    screen.fill(DARKBLUE)
    screen.blit(my_image, (0,0))
    pygame.draw.rect(screen,LIGHTBLUE,paddle)
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20,10))
    
    
    #paddle movement
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            if paddle.x<540: 
                paddle.x+=5
        if event.key == pygame.K_LEFT:
            if paddle.x>0:
                paddle.x-=5
    # brick wall   
    draw_brick(bricks1)
    draw_brick(bricks2)
    draw_brick(bricks3)
    
    
    #ball movement    
    ball.x+=velocity[0]
    ball.y+=velocity[1]  
    
    if ball.x>=590 or ball.x<=0:
        velocity[0] = -velocity[0]
    if ball.y<=38  :
        velocity[1] = -velocity[1]
    if paddle.collidepoint(ball.x,ball.y):
        pygame.mixer.Sound.play(paddle_sound)
        velocity[1]=-velocity[1]
    if ball.y>=590:
        font = pygame.font.Font(None, 74)
        text = font.render("GAME OVER", 1, RED)
        screen.blit(text, (150,350))
        pygame.display.flip()
        pygame.time.wait(2000)
        break
    pygame.draw.circle(screen, WHITE, ball.center, radius)
    #score
    for i in bricks1:
        if i.collidepoint(ball.x,ball.y):
            pygame.mixer.Sound.play(brick_sound)
            bricks1.remove(i)
            velocity[0] = -velocity[0]
            velocity[1]=-velocity[1]
            score+=1
    for i in bricks2:
        if i.collidepoint(ball.x,ball.y):
            pygame.mixer.Sound.play(brick_sound)
            bricks2.remove(i)
            velocity[0] = -velocity[0]
            velocity[1]=-velocity[1]
            score+=1
    for i in bricks3:
        if i.collidepoint(ball.x,ball.y):
            pygame.mixer.Sound.play(brick_sound)
            velocity[0] = -velocity[0]
            velocity[1]=-velocity[1]
            bricks3.remove(i)
            score+=1
                
    if score==18:
        font = pygame.font.Font(None, 74)
        text = font.render("YOU WON!!", 1, RED)
        screen.blit(text, (150,350))
        pygame.display.flip()
        pygame.time.wait(2000)
        break
    pygame.time.wait(5)
    pygame.display.flip()       
pygame.quit(  )
