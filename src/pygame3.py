# Authored by Rishikesh
# Python Gaming
import pygame
import time


pygame.init()
#Pygame understand the rgd value so we need to update color variables
white=(255,255,255)
black=(0,0,0)
red=(255,0,0) #(r,g,b,alpha)
display_width=800
display_height=600
gameDisplay=pygame.display.set_mode((display_width,display_height))
#pygame.diaplay.flip()
pygame.display.set_caption("Rishikesh")
#pygame.display.update()
clock=pygame.time.Clock()   #System Clock SetUp 


#Defining the font which I use
font= pygame.font.SysFont(None,25)

# Adding messages to the screen
def message_to_screen(msg,color):
    screen_text=font.render(msg,True,color)
    gameDisplay.blit(screen_text,[display_width/2,display_height/2])

# Main Game Loop
def gameLoop():
    
    lead_x=display_width/2
    lead_y=display_height/2
    lead_x_change=0;
    lead_y_change=0;
    gameExit= False
    gameOver=False
    block_size=10
    FPS=30
    
    while not gameExit:
        # After Game Over Menu
        while gameOver==True:
            message_to_screen("Game Over, Press C to play or Q to quit",red)
            pygame.display.update()
            for event in pygame.event.get():
                 if event.type==pygame.KEYDOWN:  
                    if event.key==pygame.K_q:
                        gameExit=True
                        gameOver=False
                    elif event.key==pygame.K_c:
                        gameLoop()
                    
        
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                gameOver=True               # Game Over indication
            if event.type==pygame.KEYDOWN:  # for start the movement of rect
                if event.key==pygame.K_LEFT:
                    lead_x_change=-block_size       # change x-axis
                    lead_y_change=0;        # change y-axis
                elif event.key==pygame.K_RIGHT:
                    lead_x_change=block_size
                    lead_y_change=0;
                elif event.key==pygame.K_UP:
                    lead_y_change=-block_size
                    lead_x_change=0;
                elif event.key==pygame.K_DOWN:
                    lead_y_change=block_size
                    lead_x_change=0;
            if event.type==pygame.KEYUP:  # for stopping the movement of rect
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    lead_x_change=0;
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    lead_y_change=0;

        # For establishing the boundary
        if lead_x>=display_width:
            lead_x=0
        if lead_y>=display_height:
            lead_y=0
        if lead_x<0:
            lead_x=display_width
        if lead_y<0:
            lead_y=display_height
            
             
                
        lead_x+=lead_x_change #reflecting the change
        lead_y+=lead_y_change 
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay,black,[lead_x,lead_y,10,10])   
        
        pygame.display.update()
        clock.tick(FPS) # 30 fps speed

    
    
    pygame.quit()   #quiting the pygame
    quit()          #quiting python


gameLoop()
