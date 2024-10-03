import pygame
import pygame_gui
import sys
import random

from pygame_gui.elements import UITextEntryLine

pygame.init()
pygame.mixer.init()


welcome_message_timer = 0
welcome_message_duration = 5000  #Duration in milliseconds (2 seconds)
welcome_message_displayed = False


TEXT_INPUT = None
width = 720
height = 480
default_font = pygame.font.Font(None, 48)

# MANAGER = pygame_gui.UIManager((width, height), 'Font.json')


# def name_input():
#     global TEXT_INPUT
#     TEXT_INPUT = pygame_gui.elements.UITextEntryLine(relative_rect=  pygame.Rect((50, 50), (200, 50)),
#                                                        manager = MANAGER, object_id = "main_text_entry")
#     print("Input field created")
    

def show_text(text_to_show):  
    screen.fill("white")  # Clear the screen
    text_surface = font.render(text_to_show, True, BLACK)  # Render the text
    screen.blit(text_surface, (50, 50))  # Draw text at the specified position
    pygame.display.flip()  # Update the display
    pygame.time.delay(2000)  # Wait for 2 seconds to allow the player to read


def start_menu():
    # This menu should be displayed at the start of the game and at the end. 

    # it'll display the start menu with the options to start the game or quit the game
    return
        
       




class Player:

    name = "Nobody"
    health = 0 
    baseAtk = 0
    mana = 0
    luck = 10
    skills = None
   
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

ememy1 = None

class Enemy:
   
    def __init__(self, health, baseAtk, mana, mana_cost, luck, skill, cooldown, name):
        self.health = health
        self.baseAtk = baseAtk
        self.mana = mana
        self.mana_cost = mana_cost
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
        if self.cooldown == 0 and self.mana >= self.mana_cost:
            attackType = random.choice(['normal', 'special'])
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
#level one enemies
class Gnome(Enemy):
    def __init__(self):
        super().__init__(health = 10, baseAtk = 1, mana = 2, mana_cost=1, skill = 3)
class Rat(Enemy):
    def __init__(self):
        super().__init__(health = 5, baseAtk= 1, mana = 0, skill = None)


def neighbor(self):
    self.health = 10
    baseAtk = 1
    mana = 50
    luck = 5
    skill = None
    self.name = "Tom (your spawn of the devil neighbor)"


def randomEnemy1():
    chooseEnemey = [Gnome, Rat, None]
    currentEnemy = random.choice(chooseEnemey)
    return currentEnemy

battle_mode = False  # Initially false, will switch to True during battles
battle_log = [] 

def battle(player, enemy):
    global battle_mode
    battle_mode = True  # Switch to battle mode when the battle starts
    battle_over = False
    battle_turn = 'Player'
    battle_log.clear()  # Clear the battle log before starting
    
    while not battle_over:
        if battle_turn == 'Player':
            # Player's turn: choose an action
            battle_log.append(f"{player.name}'s turn!")
            # Display attack options and let the player choose
            player_action = player_turn()  # Function that handles player input (attack, skill, etc.)
            
            if player_action == 'attack':
                damage = player.baseAtk  # Player's base attack damage
                enemy.health -= damage
                battle_log.append(f"{player.name} attacked {enemy.name} for {damage} damage!")
            # Add other actions like skills or items here
            
            battle_turn = 'Enemy'  # Switch turn after player action
            
        elif battle_turn == 'Enemy':
            # Enemy's turn: choose an attack
            battle_log.append(f"{enemy.name}'s turn!")
            damage = enemy.attack()  # Enemy's basic attack
            player.health -= damage
            battle_log.append(f"{enemy.name} attacked {player.name} for {damage} damage!")
            
            battle_turn = 'Player'  # Switch turn after enemy action
        
        # Check if battle is over
        if player.health <= 0:
            battle_over = True
            battle_log.append(f"{player.name} has been defeated!")
        elif enemy.health <= 0:
            battle_over = True
            battle_log.append(f"{enemy.name} has been defeated!")

        


    # return "battle_ended"  # Return to the appropriate story node when the battle is over

def draw_battle():






    return

def player_turn():
    # Display choices for the player (e.g., Attack, Use Skill)
    # Capture player's input and return the chosen action (like 'attack' or 'skill')
    # Placeholder for user input, this could be a Pygame event or key press
    return 'attack'
    
def display_battle_log(screen, font, log, player, enemy):
    screen.fill((50, 50, 50))  # Fill the screen with a dark background
    
    # Display the player and enemy health
    player_health_text = font.render(f"Player Health: {player.health}", True, (255, 255, 255))
    enemy_health_text = font.render(f"Enemy Health: {enemy.health}", True, (255, 255, 255))
    
    screen.blit(player_health_text, (50, 20))
    screen.blit(enemy_health_text, (50, 50))
    
    # Display the last few battle log entries
    y_offset = 100
    for message in log[-5:]:  # Show the last 5 battle log entries
        text_surface = font.render(message, True, (255, 255, 255))
        screen.blit(text_surface, (50, y_offset))
        y_offset += 30


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

def set_battle_mode(temp):
    global battle_mode
    battle_mode = temp
    

# Function for drawing characters based on location
def draw_characters():
    return


def choose_story(input):
    if input == "Lost Throne":
        story_nodes.update(lost_throne_nodes)
    elif input == "King of Tournaments":
        story_nodes.update(tournament_nodes)




# Define the story nodes
story_nodes = {

    "start": StoryNode(
        "Welcome to the game! Press any key to start.",
        {"": "main_menu"}, 
        actions={},
    ),

    "main_menu": StoryNode(
        "Hello Player! Welcome to our Game!!!",
        {"start game": "choose_ch", "quit game": "are_u_sure"}, 
        actions={},
    ),
    "are_u_sure": StoryNode(
        "ARE YOU SURE YOU WANT TO EMBRACE COWARDICE YOU LITTLE CHILD BABY", 
        {"YES": "quit", "NO": "start"}, 
        actions={"YES": [quit]},
    ),
    "quit": StoryNode(
        "", 
        {}, 
        actions={},
    ),
     "choose_ch": StoryNode(
        "Hello adventurer! Choose your class:", 
        {"Mage": "choose_bg", "Knight": "choose_bg", "Archer": "choose_bg", "Unfortunate": "choose_bg"},
        actions={"Mage": [player.set_mage], "Knight": [player.set_knight], "Archer": [player.set_archer], "Unfortunate": [player.set_unfortunate]},
    ),
     "choose_bg": StoryNode(
        "Choose your background of your character(This will dictate the story)", 
        {"Lost Throne": "begin_story", "King of Tournaments": "begin_story"}, 
        actions={"Lost Throne": [lambda: choose_story("Lost Throne")], "King of Tournaments": [lambda: choose_story("King of Tournaments")] },
    ),
    
}

lost_throne_nodes = {

    "begin_story": StoryNode(
        "You wake up in a dark room. You have no idea how you got here. You see a door in front of you. What do you do?", 
        {"Open the door": "door", "Go back to sleep": "sleep"}, 
        actions={},
    ),
    "sleep": StoryNode(
        "You are sleeping", 
        {"Wake up": "begin_story"}, 
        actions={},
    ),
    "door": StoryNode(
        "You open the door and see a fugly rat. What do you do?", 
        {"Attack the rat": "attacked_beginning_rat", "Go back to sleep": "tutor"}, 
        actions={"Attack the rat": [lambda: set_battle_mode(True), ]},
    ),
    "attacked_beginning_rat": StoryNode(
        "The rat lies dead on the floor. You see baby rats with big wide eyes crying. What do you do?", 
        {"Suicide": "beginning"}, 
        actions={},
    ),
     "tutor": StoryNode(
        "This is a remainder! There will be some scenes with only dispostion and story. These scenes will not have an option to select. To continue to the next"
        " scene, click the 1 key! Have fun playing our game :)", 
        {"": "beginning"}, 
        actions={},
    ),
    "beginning": StoryNode(
        "Sleep encumbers your body as you begin to fall deep into slumber. Night upon night, you see the same vision in"
        "your dreams. The king, your father, being brutally stabbed again and again. You watch in horror before you get"
        "get pulled awayn by a mysterious figure and rushed out of the castle's walls.", 
        {"" : "WakeDream"}, 
        actions={},
    ),
    "WakeDream": StoryNode(
        "You awake from your dream with sweat dripping down your forehead, however this time you feel your eyes begin"
        "to tear up as the memory of your father fade away. Around you is a room surrounded by wood walls beginning to rot"
        "This is the room you have grown up in from an early age every since that fateful night", 
        {"" : "roomBack"}, 
        actions={},
    ),
    "roomBack": StoryNode(
        "Countess Adala owns this rundown shack. She is the person who saved you from that young age of 10 . She took you"
        "in as her own kin and has raised you all this time. On your 17th birthday Adala finally told you what happend"
         "to your father and the kingdom. The kingdom that is rightfully yours as you are the heir to the king.", 
        {"" : "finalExpo"}, 
        actions={},
    ),
    "finalExpo": StoryNode(
        "An image replays in your head as you recall your 17th birthday. Adala sitting you down telling you how the throne"
        "is falsely claimed. That your father was killed and replaced and it is your right to take it back and save the kingdom."
        "Your Kingdom. Adala tells you that she supports whatever choice you make but will support you if you choose a path of revenge", 
        {"" : "throneBegin"}, 
        actions={},
    ),
    "throneBegin": StoryNode(
        "", 
        {}, 
        actions={},
    ),
    "": StoryNode(
        "", 
        {}, 
        actions={},
    ),
    "": StoryNode(
        "", 
        {}, 
        actions={},
    ),
    "": StoryNode(
        "", 
        {}, 
        actions={},
    ),
}

tournament_nodes = {
    "begin_story": StoryNode(
        "you enter a battle with a rat!", 
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
LGREY = (230, 230, 230)

# Set the frame rate
clock = pygame.time.Clock()
FPS = 60



def wrap_text(text, font, max_width):
    # Split the text into words
    words = text.split(' ')
    wrapped_lines = []
    current_line = ""
    
    for word in words:
        # Try adding the next word
        test_line = current_line + word + " "
        # Check the width of the current line
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            wrapped_lines.append(current_line)
            current_line = word + " "
    
    # Add the last line
    if current_line:
        wrapped_lines.append(current_line)
    
    return wrapped_lines

# Initial story state
current_node = "main_menu"

# Function to draw the current story node
def draw_story(node):
    global welcome_message_timer, welcome_message_displayed
    screen.fill(GREY)

    draw_characters()

    pygame.draw.rect(screen, BLACK, [0, adjust_h(250), screen_width, adjust_h(230)])
    
    # Render the main story text
    story_text_lines = wrap_text(story_nodes[node].text, font, screen_width - adjust_w(20))
    y_offset = adjust_h(260)
    
    for line in story_text_lines:
        story_surface = font.render(line, True, LGREY)
        screen.blit(story_surface, (adjust_w(10), y_offset))
        y_offset += adjust_h(30)    


    # Render choices
    choices = story_nodes[node].choices
    y_offset = adjust_h(350)  # Start point for choices on the screen
    for i, (choice_text, _) in enumerate(choices.items()):
        choice_surface = choice_font.render(f"{i + 1}. {choice_text}", True, WHITE)
        screen.blit(choice_surface, (adjust_w(10), y_offset))
        y_offset += adjust_h(30)  # Move down for the next choice

    # if node == "main_menu":
    #     if not welcome_message_displayed:
    #         show_text("Welcome to the game, " + player.name + "!")  # Display the player's name
    #         welcome_message_displayed = True  # Set flag to indicate message is shown
    #         welcome_message_timer = pygame.time.get_ticks()  # Start the timer

    # # Check if welcome message duration has passed
    # if welcome_message_displayed and (pygame.time.get_ticks() - welcome_message_timer > welcome_message_duration):
    #     welcome_message_displayed = False  # Reset flag


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

                # if node == "rat":  # Check if this is the battle node
                #     battle(player, Rat())  # Start a battle with a Rat
                #     return next_node
                
                # Execute the actions associated with the choice, if any
                if choice_text in story_nodes[node].actions:
                    for action in story_nodes[node].actions[choice_text]:
                        action()  # Call each action function
                
                 # Execute node's action when transitioning
                story_nodes[node].exe_action(player)
                story_nodes[next_node].exe_action(player)
                

                return next_node  # Return the next node key
    return node  # Return the current node if no valid input


player.setName("player_name")


# Main game loop
running = True
inventory_display = False
paused = False
start_menu_mode = False
previous_node = current_node

while running:
    Refresh_rate = clock.tick(FPS) / 1000.0
    # screen.fill((0, 0, 0)) 
    updateDimensions()

    for event in pygame.event.get():
        # Check if the player wants to quit
        if event.type == pygame.QUIT:
            running = False
        
        # Handles start menu events
        if start_menu_mode:
            start_menu()
            continue

        # Handles paused events
        elif paused:
            continue

        # Handles battle_mode events
        elif battle_mode:
            print("Battle mode")
            draw_battle()
            # battle(player, enemy)
 
        elif inventory_display:
            if event.type == pygame.KEYDOWN:
                inventory_display = False
            
            # Draw the inventory
            inventory_text = inventory()
            draw_inventory(inventory_text)  

        # Handles general events 
        else:
            current_node = handle_input(current_node, event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    inventory_display = True
    
            if current_node is None:
                running = False

            draw_story(current_node)

    # Update the screen
    pygame.display.flip()
    

pygame.quit()


#Here lies the code that I don't want to delete because I might need it later graveyard

#action=lambda state: state.addItem('key'),


#Here is the graveyard for code I want to use later but am not there just yet
# missChance = random.random()
# if missChance <= player.luck/100:
#     print("your attack missed!")
    
