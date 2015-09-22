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

gameExit= False
while not gameExit:
    for event in pygame.event.get():
        #print(event)
        if event.type==pygame.QUIT:
            gameExit=True
        if event.type==pygame.KEYUP:
            gameDisplay.fill(white)
        if event.type==pygame.MOUSEBUTTONUP:
            gameDisplay.fill(red)
        if event.type==pygame.KEYDOWN:
            gameDisplay.fill(black)
    
    pygame.display.update()
pygame.quit()
quit()
