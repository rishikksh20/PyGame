import pygame
pygame.init()
#Pygame understand the rgd value so we need to update color variables
white=(255,255,255)
black=(0,0,0)
red=(255,0,0) #(r,g,b,alpha)
gameDisplay=pygame.display.set_mode((800,600))
#pygame.diaplay.flip()
pygame.display.set_caption("Rishikesh")
#pygame.display.update()
lead_x=300
lead_y=300
lead_x_change=0;
clock=pygame.time.Clock()
gameExit= False
while not gameExit:
    for event in pygame.event.get():
        #print(event)
        if event.type==pygame.QUIT:
            gameExit=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                lead_x_change=-10
            if event.key==pygame.K_RIGHT:
                lead_x_change=10
    lead_x+=lead_x_change    
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay,black,[lead_x,lead_y,10,10])   
    
    pygame.display.update()
    clock.tick(30)
pygame.quit()
quit()
