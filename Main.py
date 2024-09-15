import pygame
import sys
import random

# Story Node class to hold story content, choices, and actions
class StoryNode:
    def __init__(self, text, choices, actions=None):
        self.text = text
        self.choices = choices
        self.actions = actions if actions is not None else {}

# Define functions for actions
def found_key():
    print("You have found a mysterious key!")

def unlocked_door():
    print("You unlocked the door and step into the unknown.")

def went_back_to_sleep():
    print("You have gone back to sleep.")

def special_message():
    print("This is a special action!")

# Define the story nodes
story_nodes = {
    "start": StoryNode(
        "You wake up in a dark room. What will you do?", 
        {"explore": "explore_room", "sleep": "go_back_to_sleep"}
    ),
    "explore_room": StoryNode(
        "You find a mysterious key. What now?", 
        {"take key": "open_door", "leave key": "start"},
        actions={"take key": [found_key, special_message]}  # Multiple actions
    ),
    "go_back_to_sleep": StoryNode(
        "You fall back asleep. What now?", 
        {"wake up": "start"},
        actions={"wake up": [went_back_to_sleep]}
    ),
    "open_door": StoryNode(
        "You open the door and step into the unknown. End.", 
        {},
        actions={}  # No actions for this node
    ),
}

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



# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Screen dimensions
screen_width, screen_height = 720, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Interactive Story")

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
    pygame.draw.rect(screen, BLACK, [0, 300, 800, 200])
    
    # Render the main story text
    story_text = font.render(story_nodes[node].text, True, WHITE)
    screen.blit(story_text, (10, 310))
    
    # Render choices
    choices = story_nodes[node].choices
    y_offset = 350  # Start point for choices on the screen
    for i, (choice_text, _) in enumerate(choices.items()):
        choice_surface = choice_font.render(f"{i + 1}. {choice_text}", True, WHITE)
        screen.blit(choice_surface, (20, y_offset))
        y_offset += 30  # Move down for the next choice

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
                
                return next_node  # Return the next node key
    return node  # Return the current node if no valid input

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Handle input and move to the next story node
        current_node = handle_input(current_node, event)
    
    # Draw the current story and choices
    draw_story(current_node)
    
    # Update the screen
    pygame.display.flip()
    
    # Frame rate
    clock.tick(30)

pygame.quit()
