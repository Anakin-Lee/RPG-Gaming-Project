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







# Define the story nodes
story_nodes = {
    "start": StoryNode(
        "Hello adventurer! Choose your class:", 
        {"Mage": "explore_room", "Knight": "explore_room", "Archer": "explore_room", "Unfortunate": "explore_room"},
        actions={"Mage": [player.set_mage], "Knight": [player.set_knight], "Archer": [player.set_archer], "Unfortunate": [player.set_unfortunate]},
    ),
    "explore_room": StoryNode(
        "You find a mysterious key. What now?", 
        {"take key": "to_door", "leave key": "to_door"},
        action=lambda state: (print("Adding key in explore_room"), state.addItem('key')),
        actions={"take key": [found_key, special_message]}
        
    ),
    "go_back_to_sleep": StoryNode(
        "You fall back asleep. What now?", 
        {"wake up": "start"},
        actions={"wake up": [went_back_to_sleep]}
    ),
    "to_door": StoryNode(
    "You arrive at the door, what do you do?", 
    {"check inventory": "inventory", "open the door": "open_door", "go back": "start"},
    condition=lambda state: state.hasItem('key'),  # No actions for this node
    actions={"check inventory": [inventory]}
    ),
    "inventory": StoryNode(
        "Here is your inventory, what would you like to do now?",
        {"you go back to the door": "to_door",},
        
    ),
    "open_door": StoryNode(
        "You open the door and step into the unknown. End.",
         {"continue": [lambda: print("Thank you for playing!")]},
        
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

    # Optionally, you can add a "Back" option
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

                if next_node == "to_door":
                    has_key = story_nodes[next_node].check_condition(player)  # Check if the player has the key
                    print(f"Player inventory: {player.inventory()}")
                    print(f"Condition to enter {next_node}: {has_key}")  # Debugging print
                    if not has_key:
                        print(f"Condition to enter {next_node} not met.")  # For debugging purposes
                        return node  # Stay in the current node
                
                 # Execute node's action (like adding key) when transitioning
                story_nodes[node].exe_action(player)
                story_nodes[next_node].exe_action(player)
                
                
                if choice_text == "check inventory":
                    return "inventory"  # Stay in the inventory node until key press
                

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

            if current_node is not "inventory":
                previous_node = current_node

            if current_node == "inventory":
                inventory_display = True  # Enter inventory mode
                current_node = "inventory"

        else:
            # If in inventory, any key press returns to the last node
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
        inventory_text = inventory()  # Get the inventory text
        draw_inventory(inventory_text)  # Use the function to draw on the Pygame window


    # print(pygame.display.Info().current_w, pygame.display.Info().current_h)
    
    print(screen_width, screen_height)

    # Update the screen
    pygame.display.flip()
    
    # Frame rate
    clock.tick(30)

pygame.quit()
