import pygame
import sys
import random



class Player:
    name = "Nobody"
    health = 0 
    baseAtk = 0
    mana = 0
    luck = 10
    skill = None
   

    def __init__(self):
         self.invent = []
    
    def inventory(self):
        return self.invent
    
    def addItem(self, item):
        self.invent.append(item)
    
    def hasItem(self, item):
        return item in self.invent

    
    def setName(self, name):
        self.name = name

    def selectionMenu(self):
        #print choose your class: 

        return
    
    def set_mage(self):
        self.health = 8
        self.baseAtk = 3
        self.mana = 10
        sound_effect = pygame.mixer.Sound('Voices/Mage1.wav')
        sound_effect.play()
        #print you have selected mage

    def set_knight(self):
        self.health = 12
        self.baseAtk = 5
        self.mana = 5
        sound_effect = pygame.mixer.Sound('Voices/Knight1.wav')
        sound_effect.play()
        #print in animation you have selected knight

    def set_archer(self):
        self.health = 10
        self.baseAtk = 4
        self.mana = 7
        sound_effect = pygame.mixer.Sound('Voices/Archer1.wav')
        sound_effect.play()
        #print in animation you have selected archer

    def set_unfortunate(self):
        self.health = 1
        self.baseAtk = 1
        self.mana = 20
        self.luck = 30
        sound_effect = pygame.mixer.Sound('Voices/Unfortunate1.wav')
        sound_effect.play()
        #print in animation you have selected unfortunate


player = Player()
ememy = None

class Enemy:
   
    def __init__(self, health, baseAtk, mana, luck, skill, cooldown, name):
        self.health = health
        self.baseAtk = baseAtk
        self.mana = mana
        self.luck = luck
        self.skill = skill
        self.cooldown = 0
        self.name = name

    def attack(self):
        print("Enemy used Basic Attack!!")
        return self.baseAtk
    
    def skillAtk(self):
        print("Enemy used special attack!!")
        return self.skill
    
    def chooseAttack(self):
        if self.cooldown == 0:
            attackType = random.choice['normal', 'special']
        else:
            attackType = 'normal'

        if attackType == 'special':
            self.cooldown = 3
            return self.attack()
        else: 
            return self.skillAtk()
        
    def spAtkCooldown(self):
        if self.cooldown > 0:
            self.cooldown -=1


#Subclasses of the general Enemy Class: 

class Gnome(Enemy):

    #level one enemies

    def __init__(self):
        super().__init__(health = 10, baseAtk = 1, mana = 2, skill = 3)

    
    def neighbor(self):
        self.health = 10
        baseAtk = 1
        mana = 50
        luck = 5
        skill = None
        self.name = "Tom (your spawn of the devil neighbor)"




def randomEnemy1():
    chooseEnemey = [Gnome, None, None]
    currentEnemy = random.choice(chooseEnemey)
    return currentEnemy




    

# Story Node class to hold story content, choices, and actions
class StoryNode:
    def __init__(self, text, choices=None, action=None, condition=None, actions=None):
        self.text = text
        self.choices = choices
        self.actions = actions if actions is not None else {}
        self.action = action if action is not None else {}
        self.condition = condition if condition is not None else {}
    
    def exe_action(self, player):
        if self.action:
            self.action(player)
    def check_condition(self, player):
        if self.condition:
            return self.condition(player)
        return True


# Define functions for actions

def found_key():
    print("You have found a mysterious key!")
    

def unlocked_door():
    print("You unlocked the door and step into the unknown.")

def went_back_to_sleep():
    print("You have gone back to sleep.")

def special_message():
    print("This is a special action!")

def inventory():
    items = player.inventory()  # Get the inventory list
    if items:  # Check if there are any items
        return "Your inventory contains: " + ", ".join(items)
    else:
        return "Your inventory is empty."


    

# Function for drawing characters based on location
def draw_characters():
    return


def choose_story(input):
    if input == "Lost Throne":
        return
    elif input == "King of Tournaments":
        return




# Define the story nodes
story_nodes = {

    "start": StoryNode(
        "Hello Player! Welcome to our Game!!!",
        {"start game": "choose_bg", "quit game": "are_u_sure"}, 
        actions={},
    ),
    "are_u_sure": StoryNode(
        "ARE YOU SURE YOU WANT TO EMBRACE COWARDICE YOU LITTLE CHILD BABY", 
        {"YES": "quit", "NO": "start1"}, 
        actions={"YES": [quit]},
    ),
    "quit": StoryNode(
        "", 
        {}, 
        actions={},
    ),
     "choose_bg": StoryNode(
        "Choose your background of your character(This will dictate the story)", 
        {"Lost Throne": "choose_ch", "King of Tournaments": "choose_ch"}, 
        actions={"Lost Throne": [choose_story("Lost Throne")], "King of Tournaments": [choose_story("King of Tournaments")] },
    ),
     "choose_ch": StoryNode(
        "Hello adventurer! Choose your class:", 
        {"Mage": "explore_room", "Knight": "explore_room", "Archer": "explore_room", "Unfortunate": "explore_room"},
        actions={"Mage": [player.set_mage], "Knight": [player.set_knight], "Archer": [player.set_archer], "Unfortunate": [player.set_unfortunate]},
    )
}
lost_throne_nodes = {
    "quit": StoryNode(
        "", 
        {}, 
        actions={},
    ),
    "quit": StoryNode(
        "", 
        {}, 
        actions={},
    ),"quit": StoryNode(
        "", 
        {}, 
        actions={},
    ),"quit": StoryNode(
        "", 
        {}, 
        actions={},
    ),
}



# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Screen dimensions
screen_width = 720
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE, pygame.SCALED)
pygame.display.set_caption("Dead End Adventurer")

def updateDimensions():
    global screen_width 
    screen_width = pygame.display.Info().current_w

    global screen_height
    screen_height = pygame.display.Info().current_h

    global font
    font = pygame.font.Font(None, int(36*screen_height/480))

    global choice_font
    choice_font = pygame.font.Font(None, int(28*screen_height/480))

def adjust_w(num):
    return int(num*screen_width/720)

def adjust_h(num):
    return int(num*screen_height/480)


# Font settings
font = pygame.font.Font(None, 36)
choice_font = pygame.font.Font(None, 28)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)

# Set the frame rate
clock = pygame.time.Clock()
FPS = 60

# Initial story state
current_node = "start"

# Function to draw the current story node
def draw_story(node):
    screen.fill(GREY)

    draw_characters()

    pygame.draw.rect(screen, BLACK, [0, adjust_h(300), screen_width, adjust_h(200)])
    
    # Render the main story text
    story_text = font.render(story_nodes[node].text, True, WHITE)
    screen.blit(story_text, (adjust_w(10), adjust_h(310)))
    
    
    # Render choices
    choices = story_nodes[node].choices
    y_offset = adjust_h(350)  # Start point for choices on the screen
    for i, (choice_text, _) in enumerate(choices.items()):
        choice_surface = choice_font.render(f"{i + 1}. {choice_text}", True, WHITE)
        screen.blit(choice_surface, (adjust_w(20), y_offset))
        y_offset += adjust_h(30)  # Move down for the next choice

def draw_inventory(inventory_text):
    screen.fill(GREY)  # Clear the screen with a background color
    # Draw the inventory text
    inventory_surface = font.render(inventory_text, True, WHITE)
    screen.blit(inventory_surface, (adjust_w(10), adjust_h(10)))

    # Adds a back button option
    back_surface = choice_font.render("Press any key to go back", True, WHITE)
    screen.blit(back_surface, (adjust_w(10), adjust_h(50)))

# Function to handle user input
def handle_input(node, event):
    choices = list(story_nodes[node].choices.items())

    if event.type == pygame.KEYDOWN:
        if pygame.K_1 <= event.key <= pygame.K_9:  # Handle number keys
            choice_index = event.key - pygame.K_1
            if 0 <= choice_index < len(choices):
                choice_text = choices[choice_index][0]
                next_node = choices[choice_index][1]
                
                # Execute the actions associated with the choice, if any
                if choice_text in story_nodes[node].actions:
                    for action in story_nodes[node].actions[choice_text]:
                        action()  # Call each action function
                
                 # Execute node's action when transitioning
                story_nodes[node].exe_action(player)
                story_nodes[next_node].exe_action(player)
                

                return next_node  # Return the next node key
    return node  # Return the current node if no valid input

# Main game loop
running = True
inventory_display = False
previous_node = current_node
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not inventory_display:
            current_node = handle_input(current_node, event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    inventory_display = True  # Enter inventory mode
                    previous_node = current_node
        

        else:
            
            if event.type == pygame.KEYDOWN:
                inventory_display = False  # Exit inventory mode
                current_node = previous_node  # Go back to the previous node

        if current_node is None:
            running = False
        
    updateDimensions()
    
    
    if not inventory_display:
        # Draw the current story and choices
        draw_story(current_node)
    else:
        # Draw the inventory
        inventory_text = inventory()
        draw_inventory(inventory_text)  


    # print(pygame.display.Info().current_w, pygame.display.Info().current_h)
    

    # Update the screen
    pygame.display.flip()
    
    # Frame rate
    clock.tick(30)

pygame.quit()


#Here lies the code that I don't want to delete because I might need it later graveyard

#action=lambda state: state.addItem('key'),


#Here is the graveyard for code I want to use later but am not there just yet
# missChance = random.random()
# if missChance <= player.luck/100:
#     print("your attack missed!")
    
