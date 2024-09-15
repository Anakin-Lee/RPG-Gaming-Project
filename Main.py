import pygame
import sys
import random
pygame.init()
pygame.mixer.init()

# Set up the game window
screen = pygame.display.set_mode((720, 480))
pygame.display.set_caption('Adventure')

clock = pygame.time.Clock()
FPS = 60

class characterSelect:
    name = "Nobody"
    health = 0 
    baseAtk = 0
    mana = 0
    luck = 10
    skill = None

    def __init__(self):
        return
    
    def setName(self, name):
        self.name = name

    def selectionMenu(self):
        #print choose your class: 

        return
    
    def mage(self):
        self.health = 8
        self.baseAtk = 3
        self.mana = 10
        sound_effect = pygame.mixer.Sound('Voices/Mage1.wav')
        sound_effect.play()
        #print you have selected mage

    def knight(self):
        self.health = 12
        self.baseAtk = 5
        self.mana = 5
        sound_effect = pygame.mixer.Sound('Voices/Knight1.wav')
        sound_effect.play()
        #print in animation you have selected knight

    def archer(self):
        self.health = 10
        self.baseAtk = 4
        self.mana = 7
        sound_effect = pygame.mixer.Sound('Voices/Archer1.wav')
        sound_effect.play()
        #print in animation you have selected archer

    def unfortunate(self):
        self.health = 1
        self.baseAtk = 1
        self.mana = 20
        self.luck = 30
        sound_effect = pygame.mixer.Sound('Voices/Unfortunate1.wav')
        sound_effect.play()
        #print in animation you have selected unfortunate

    
BG = (128, 128, 128)
def draw_bg():
    screen.fill(BG)
# class gameController:


#Sets up display text and settings
font = pygame.font.SysFont(None, 30)
""" def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y)) """
    
#setting up the animation for texts
timer = pygame.time.Clock()
menuMessage = ['this is a test for animation, this is pretty cool right?', 
               'if you press the space bar you go to the next message',
               'That way we can display multiple strings of texts in one executable list']
activeMessage = 0
message = menuMessage[activeMessage]

snip = font.render('', True, 'white')
counter = 0
speed = 2
done = False

#The while loop that keeps the game window open
run = True
while run:
    draw_bg()
    timer.tick(60)
    pygame.draw.rect(screen, 'black', [0, 300, 800, 200])

    #draw_text("Test of display text", text_font, (0,0,0), 220, 150)
#this counter is what runs the text animation
    if counter < speed *len(message):
        counter += 1
    elif counter >= speed*len(message):
        done = True
#This loop quits the game once the x is clicked on the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and done and activeMessage < len(menuMessage):
                activeMessage += 1
                done = False
                message = menuMessage[activeMessage]
                counter = 0

#snip is what makes the text animation happen and takes a snip of message
#Scrren.blit is what puts it into the window
    snip = font.render(message[0:counter//speed], True, 'white')
    screen.blit(snip, (10, 310))

    pygame.display.flip()
pygame.quit()








    
