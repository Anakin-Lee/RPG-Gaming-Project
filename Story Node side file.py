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

    "start_menu": StoryNode(
        "Hello Player! Welcome to our Game!!!",
        {"start game": "choose_bg", "quit game": "are_u_sure"}, 
        actions={},
    ),
    "are_u_sure": StoryNode(
        "ARE YOU SURE YOU WANT TO EMBRACE COWARDICE YOU LITTLE CHILD BABY", 
        {"YES": "quit", "NO": "start_menu"}, 
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
    "start_lost": StoryNode(
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







# story_nodes = {
#     "start": StoryNode(
#         "Hello adventurer! Choose your class:", 
#         {"Mage": "explore_room", "Knight": "explore_room", "Archer": "explore_room", "Unfortunate": "explore_room"},
#         actions={"Mage": [player.set_mage], "Knight": [player.set_knight], "Archer": [player.set_archer], "Unfortunate": [player.set_unfortunate]},
#     ),
#     "explore_room": StoryNode(
#         "You find a mysterious key. What now?", 
#         {"take key": "to_door", "leave key": "to_door"},
#         actions={"take key": [found_key, lambda: player.addItem('key'),special_message]}
        
#     ),
#     "go_back_to_sleep": StoryNode(
#         "You fall back asleep. What now?", 
#         {"wake up": "start"},
#         actions={"wake up": [went_back_to_sleep]}
#     ),
#     "to_door": StoryNode(
#     "You arrive at the door, what do you do?", 
#     {"open the door": "open_door", "go back": "start"},
#     ),
#     "open_door": StoryNode(
#         "You open the door and step into the unknown. End.",
#          {"continue": [lambda: print("Thank you for playing!")]},
        
#     ),

# }
# battle_node = {

# }