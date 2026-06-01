# This is a thriller-like cave exploration game.
# AI usage: I used gemini a lot for this task, because it was very overwhelming to me.

import sys
import time
import textwrap
import os

# --- PATH REDIRECTION LOGIC TO FIND WEEK 7 ---
# Tells Python to step up out of week6 and add the week7 directory to search paths
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'week7')))

try:
    import scoresaving
except ImportError:
    print("\n" + "!" * 60)
    print("CRITICAL ERROR: Could not locate 'scoresaving.py' inside 'week7' folder.")
    print("Please ensure your folder layout matches exactly:")
    print("YourProjectName/")
    print("  ├── week6/ (Contains this game file)")
    print("  └── week7/ (Must contain scoresaving.py)")
    print("!" * 60 + "\n")
    sys.exit() # Stops execution immediately so you don't get a NameError crash later

# --- DEBUG SYSTEM ---
DEBUG = True


# --- Game State ---
current_room = 1
game_over = False
player_name = ""
player_ready = False
ending_achieved = "Unknown"

# ---Room 3 puzzle state---
room3_revealed = False
bone_placed = False
bracelet_placed = False

# --- Questions ---
NAME_REQUEST = "What's your name? "
PLAYER_READY = "Are you up for the challenge? Answer with 'yes' or 'no': "
FINAL_CHOICE = "You gaze at the skeleton for a few more moments. You could ‘drop map’ and tell Mr. McMoney there is nothing to be found here, or 'map room 3' and head back to tell Mr. McMoney about your findings."

# --- Intros ---
WELCOME_MESSAGE = "Welcome to Trembling Tunnels, a cave exploration game."

INTRO_PART1 = "You stand on a meadow in front of a rather small hill made up of big rocks, which are covered in moss. On the meadow people have setup tents and some workers run around carrying all kinds of electric devices from one tent to the other. You have just introduced yourself to a funny looking man, who ran over to you the second you pulled up to the site. He is wearing a top hat, and greeted you with an audaciously strong handshake."

# --- Room Introductions ---
INTRO_ROOM1 = "After a safety briefing by Mr. McMoney’s team, you are led to a small opening between some of the rocks. The edges are sharp and uninviting, the opening seemingly too narrow. But a job is a job, you decide, and climb in head first, needing to twist your head to the side to make it fit. You feel the cold edges of the stone pressing against your ears as you wiggle forth. Breathing soon becomes more challenging as you have to let out your breath at strategic times to make your body fit through the narrow pathway. You feel yourself going down as the path starts decreasing in altitude, and sure enough, shortly after you find yourself upside down. Your heart rate quickens and you feel your blood rushing into your head as the only sound in this tunnel. It's clouding your thoughts briefly but you keep pushing, knowing the dangers of staying upside down for too long. Sure enough, you come to an opening into a sort of small room, where you can barely stand. You lay there for a few seconds, appreciating the feeling of being able to expand your ribcage while breathing. It's pretty dark though."

INTRO_ROOM2 = "You quickly map the first room and head on deeper into the cave. It gets damper the further you go and your nose picks up an increasingly rotten smell. The walls are covered in some sort of slimy green and grey algae. The deeper you go, the more you wish to return to the surface, but it's too late to turn back now. You arrive in the next room."

INTRO_ROOM3 = "You quickly map room two. You just want to get out of the cave at this point as the lingering scent assaults your nasal cavities. You find a small path that has you crawling in a sludge of mud and algae as you feel a wind gust of wind. Might the next room have an exit, or were you just imagining things? After a while you feel around and are able to get up in the darkness."

# --- Player Choices & Endings ---
PLAYER_READY_YES = "“Very Well, you will need some equipment like a flashlight, so try to pick it up. I’m guessing you can probably carry about..hmm 5 items at once? So make sure not to carry unnecessary things with you.” Mr. McMoney reaches into his suit jacket and pulls out a flashlight."

PLAYER_READY_NO = "Mr. McMoney furrows his brows. “You’re kidding, right? I’M PAYING YOU FOR THIS.” Weirded out by his outburst, you get back into your car and decide it might be best to not take this job. You have a bad gut feeling about all of this… As you turn the car around to drive it onto the makeshift path you came on, you hear Mr. McMoney screaming, his voice becoming more unintelligible the further you get away: “{name} I WILL REMEMBER YOU! DON’T think you can get away with this……”"

PLAYER_END_MONEY = "You are not here for sentimentalism. You map up room 3 and head back to Mr. McMoney, where your handsome payment awaits you."

PLAYER_END_DROP_MAP = "You decide to drop the map of the other rooms and tell Mr. McMoney the cave is unimportant and small. You are determined to finally let this entity rest. You head back the way you came."

# --- Using flashlight ---
SEE_ROOM1 = "The first room is uneventcentful. It's damp, with a few small puddles on the floor. You question your choice of occupation as a cold shiver runs over your spine and you feel like suddenly you are being watched."

SEE_ROOM2 = "After a while the path leads into another room, a bigger one this time, where you can finally stand up straight in. It could almost be described as a hall with big and sharp stalactites. Every now and again you hear the sound of water dripping off of them."

SEE_ROOM3 = "You look around with the flashlight again and your gasp fills the almost round chamber you are now standing in. A few feet in front of you lies a human skeleton with a rib bone missing. Your heart starts pounding as you consider that if you had crawled further, you would’ve crawled right over it. Another gust of wind pulls you out of your thoughts."

# --- Items in rooms ---
items_in_room1 = [
    {"name": "rocks", "description": "You pick up a few rocks... why not?"},
    {"name": "critters",
     "description": "You pick up a slimy worm-like thing, that was too slow to get away from you. As you try to put it into your jacket pocket, you feel your hand start to burn, as you suddenly gasp for air: seems like the worm was poisonous…"},
    {"name": "bone",
     "description": "You get closer and pick up the bone that’s perfectly white, as if it’s been here in the dark for a long time."}
]

items_in_room2 = [
    {"name": "more rocks", "description": "You pick up a few more rocks... why not?"},
    {"name": "bracelet",
     "description": "You pick up the bracelet. It looks quite delicately made and was probably very beautiful once. Now it’s scratched up and the green stones embedded in silver joints are dull. You wonder how it got here."}
]

items_in_room3 = [
    {"name": "skeleton",
     "description": "You try to pick up the skeleton but you fall over into the bones. Rightfully so, why would you disturb the dead? The sound of the bones echo through the cave. The entity didn’t like that. You feel one final wind, before tiredness overcomes you and you close your eyes forever."},
    {"name": "entity",
     "description": "You can’t really see it but you pick up a sense of an entity in this room. There is definitely a presence of something. “Hello?” You try your luck. Your vocal cords are strained from the journey and from not speaking for a prolonged time. A strong gust of wind makes you tumble a step back and it doesn’t seem to abate this time. Perhaps it’s best to give back what was never yours to begin with."}
]

current_room_items = items_in_room1

# --- Pickup Messages ---
PICKUP_FLASHLIGHT = "You take the Flashlight. It is now added to your Inventory."

# --- Drop Messages ---
DROP_FLASHLIGHT = "You drop your flashlight… bad idea in a cave… you never find the exit and are stranded there forever… sowwy !!"
DROP_ROCKS = "You drop the rocks you've collected. It has been removed from your inventory."
DROP_BONE_ROOM3 = "You try whether the bone fits on the corpse and it does. You put it in its rightful place. The wind is still strong, but it feels, sort of welcoming now, giving you fresh air to breathe. However you feel like you are not finished yet. There is something else that doesn't belong to you still."
DROP_BRACELET_ROOM3 = "You carefully lift one of the arms on the bone and slide the bracelet around it. The wind now fully abides. You look at the final resting place of whoever this person was."
DROP_BRACELET = "You drop the bracelet. It has been removed from your inventory."
DROP_BONE = "You drop the bone. It has been removed from your inventory."

# --- Map room3 early ---
MAP_ROOM3_EARLY = "You are not here for sentimentalism. You start mapping room 3 to head back to Mr. McMoney, where your handsome payment awaits you. Before you can even start putting your pen down on your paper, you feel super tired. The soft wind helps you sleep and rest forever."

# --- Inventory System ---
inventory = []
MAX_INVENTORY_SIZE = 5


# --- Custom Delay Writer ---
def delay_print(text, speed=0.03, delay_after=2.5):
    if not text:
        return
    paragraphs = text.split('\n')
    for idx, paragraph in enumerate(paragraphs):
        if not paragraph.strip():
            print()
            continue
        wrapped_lines = textwrap.wrap(paragraph, width=80)
        for line in wrapped_lines:
            for char in line:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(speed)
            sys.stdout.write('\n')
            sys.stdout.flush()
        if idx < len(paragraphs) - 1:
            print()
    if delay_after > 0:
        time.sleep(delay_after)


# --- Functions ---
def get_user_choice(prompt, valid_options):
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_options:
            return choice
        else:
            print(f"Please choose one of: {', '.join(valid_options)}")


def show_inventory():
    if len(inventory) == 0:
        delay_print("You have no items in inventory.")
    else:
        delay_print("Your inventory:")
        for item in inventory:
            delay_print(f" - {item['name']}", delay_after=0.2)


def show_room_items():
    if current_room == 3 and not room3_revealed:
        delay_print("It's pitch black! You can't see any items here. Maybe you should use something?")
        return

    if len(current_room_items) == 0:
        delay_print("There are no items in this room.")
    else:
        delay_print("Items in this room:")
        for item in current_room_items:
            delay_print(f" - {item['name']}", delay_after=0.2)


def pick_up(item_name):
    global game_over, ending_achieved
    item_name = item_name.strip().lower()

    if current_room == 3 and not room3_revealed:
        delay_print("It's pitch black! You can't safely grab anything without being able to see.")
        return

    # Game Over Trigger for picking up critters
    if item_name == "critters" and any(item["name"].lower() == "critters" for item in current_room_items):
        delay_print(items_in_room1[1]["description"])
        ending_achieved = "Poisoned by Critters"
        game_over = True
        return

    # Game Over Trigger for picking up skelleton
    if item_name == "skeleton" and any(item["name"].lower() == "skeleton" for item in current_room_items):
        delay_print(items_in_room3[0]["description"])
        ending_achieved = "Crushed by Skeleton"
        game_over = True
        return

    # normal pickup
    for item in current_room_items:
        if item["name"].lower() == item_name:
            if len(inventory) >= MAX_INVENTORY_SIZE:
                delay_print("Your inventory is full. You cannot pick up more items.")
                return
            current_room_items.remove(item)
            inventory.append(item)
            delay_print(item["description"])
            return

    delay_print(f"You cannot pick up {item_name}. It is not in this room.")


def drop(item_name):
    global game_over, bone_placed, bracelet_placed, ending_achieved
    item_name = item_name.strip().lower()

    # game over flashlight
    if item_name == "flashlight":
        for item in inventory:
            if item["name"].lower() == "flashlight":
                delay_print(DROP_FLASHLIGHT)
                ending_achieved = "Lost in Darkness"
                game_over = True
                return

    # drop bone and bracelet in room 3
    if current_room == 3 and room3_revealed:
        if item_name == "bone":
            for item in inventory:
                if item["name"].lower() == "bone":
                    inventory.remove(item)
                    bone_placed = True
                    delay_print(DROP_BONE_ROOM3)
                    check_puzzle_completion()
                    return
        elif item_name == "bracelet":
            for item in inventory:
                if item["name"].lower() == "bracelet":
                    inventory.remove(item)
                    bracelet_placed = True
                    delay_print(DROP_BRACELET_ROOM3)
                    check_puzzle_completion()
                    return

    # normal drop
    for item in inventory:
        if item["name"].lower() == item_name:
            inventory.remove(item)
            current_room_items.append(item)
            if item_name == "rocks" or item_name == "more rocks":
                delay_print(DROP_ROCKS)
            elif item_name == "bracelet":
                delay_print(DROP_BRACELET)
            elif item_name == "bone":
                delay_print(DROP_BONE)
            else:
                delay_print(f"You dropped the {item['name']}.")
            return

    delay_print(f"You cannot drop {item_name}. It is not in your inventory.")


def use(item_name):
    global room3_revealed, bone_placed, bracelet_placed
    item_name = item_name.strip().lower()

    has_item = any(item["name"].lower() == item_name for item in inventory)
    if not has_item:
        delay_print(f"You cannot use {item_name}. It is not in your inventory.")
        return

    if item_name == "flashlight":
        if current_room == 1:
            delay_print(SEE_ROOM1)
        elif current_room == 2:
            delay_print(SEE_ROOM2)
        elif current_room == 3:
            if not room3_revealed:
                room3_revealed = True
                delay_print(SEE_ROOM3)
            else:
                delay_print("Your flashlight is already illuminating the chamber.")

    elif item_name == "bone" and current_room == 3 and room3_revealed:

        for item in inventory:
            if item["name"].lower() == "bone":
                inventory.remove(item)
                bone_placed = True
                delay_print(DROP_BONE_ROOM3)
                check_puzzle_completion()
                return

    elif item_name == "bracelet" and current_room == 3 and room3_revealed:

        for item in inventory:
            if item["name"].lower() == "bracelet":
                inventory.remove(item)
                bracelet_placed = True
                delay_print(DROP_BRACELET_ROOM3)
                check_puzzle_completion()
                return
    else:
        delay_print(f"You use the {item_name}. Nothing special happens.")


def check_puzzle_completion():
    global game_over, ending_achieved
    if bone_placed and bracelet_placed:
        delay_print("\nThe wind has fully calmed down. The entities seem to be appeased and at peace now.")
        delay_print(FINAL_CHOICE)
        choice = get_user_choice("What will you do? (drop map / map room 3): ", ["drop map", "map room 3"])
        if choice == "drop map":
            delay_print(PLAYER_END_DROP_MAP)
            ending_achieved = "Let Entity Rest"
            game_over = True
        elif choice == "map room 3":
            delay_print(PLAYER_END_MONEY)
            ending_achieved = "Rich Explorer"
            game_over = True


def enter_room(room_num):
    global current_room, current_room_items
    if room_num == 1:
        current_room = 1
        current_room_items = items_in_room1
        delay_print(INTRO_ROOM1)
    elif room_num == 2:
        current_room = 2
        current_room_items = items_in_room2
        delay_print(INTRO_ROOM2)
    elif room_num == 3:
        current_room = 3
        current_room_items = items_in_room3
        delay_print(INTRO_ROOM3)


# --- Game Loop ---
def game_loop():
    global game_over, current_room, player_ready, player_name, current_room_items, ending_achieved

    start_time = time.time()

    if DEBUG:
        print("\n--- DEBUG MODUS: Main gameplay body skipped ---")
        player_name = input("Please enter your name for testing purposes: ").strip()
        ending_achieved = "DEBUG Placeholder Ending"
        total_time_used = 12.5

        # Trigger execution inside week7 module
        scoresaving.end_game_processing(player_name, total_time_used, ending_achieved)
        return

    # Welcome & Name
    delay_print(WELCOME_MESSAGE, delay_after=1.5)
    player_name = input(NAME_REQUEST).strip()

    # Intro
    delay_print(INTRO_PART1, delay_after=5.0)

    mc_money_greeting = f"“{player_name}! Such a fitting name for our most beloved explorer! I am Mr. McMoney, a pretty well known beneficiary around here, if I dare say so myself. I have been doing my best to discover this unkempt forest, which I’ve bought a couple of years ago. As you know, we’ve recently uncovered a new cave system, the ‘trembling caves’."
    delay_print(mc_money_greeting, delay_after=5.0)

    mc_money_trembling = "The name sounds odd to you? Don’t worry… Trembling is just the name of the nearest town… and what all the other explorers were doing after getting out of the cave… Oh… did I say that out loud?”"
    delay_print(mc_money_trembling, delay_after=5.0)

    mc_money_objective = "“Whatever, that’s why we have you here anyway! I’M sure you’ll be able to map the entire cave and get back in one piece!”"
    delay_print(mc_money_objective, delay_after=4.0)

    mc_money_scanners = "“Usually we would map the cave from the outside to determine whether its safe to enter, but for some strange reason the scanners don’t pick up on it… Anyways… Be safe out there, you can always contact my workers by walkie talkie to get some help about your options by inputting ‘help’!”"
    delay_print(mc_money_scanners, delay_after=3.0)

    # Ready?
    choice = get_user_choice(PLAYER_READY, ["yes", "no"])
    if choice == "no":
        delay_print(PLAYER_READY_NO.format(name=player_name))
        ending_achieved = "Declined Job"
        total_time_used = round(time.time() - start_time, 1)
        scoresaving.end_game_processing(player_name, total_time_used, ending_achieved)
        return
    else:
        delay_print(PLAYER_READY_YES, delay_after=2.5)

    # pickup flashlight
    delay_print("\nThe flashlight is sitting right in front of you. You cannot enter the dark caves without it.")
    while True:
        action = input("\nWhat will you do? ").strip().lower()
        if action == "pickup flashlight" or action == "pick up flashlight":
            inventory.append(
                {"name": "flashlight", "description": "A flashlight. Your primary light source."})
            delay_print(PICKUP_FLASHLIGHT)
            break
        elif "flashlight" in action:
            delay_print("Be precise. Type: 'pickup flashlight'")
        else:
            delay_print("Mr. McMoney clears his throat. 'You are going to need that flashlight, buddy.'")

    # first room
    enter_room(1)

    # Start Game Loop
    while not game_over:
        user_input = input("\n> ").strip().lower()
        if not user_input:
            continue

        if user_input.startswith("pick up "):
            user_input = "pickup " + user_input[8:]

        parts = user_input.split(" ", 1)
        command = parts[0]
        argument = parts[1].strip() if len(parts) > 1 else ""

        if command == "help":
            delay_print(
                "Commands: inventory, look, pickup [item], drop [item], use [item], map room 1, map room 2, map room 3, quit",
                delay_after=0.5)
        elif command == "inventory":
            show_inventory()
        elif command == "look":
            show_room_items()
        elif command == "pickup":
            if not argument:
                delay_print("What do you want to pick up?")
            else:
                pick_up(argument)
        elif command == "drop":
            if not argument:
                delay_print("What do you want to drop?")
            else:
                drop(argument)
        elif command == "use":
            if not argument:
                delay_print("What do you want to use?")
            else:
                use(argument)

        elif user_input == "map room 1":
            if current_room == 1:
                delay_print("You successfully map out Room 1. You decide to go deeper...")
                enter_room(2)
            else:
                delay_print("You have already mapped Room 1.")

        elif user_input == "map room 2":
            if current_room == 2:
                delay_print("You successfully map out Room 2, but the cave calls to you. You decide to go deeper...")
                enter_room(3)
            elif current_room == 1:
                delay_print(
                    "You can't map Room 2 yet! You haven't even finished or mapped Room 1!")
            else:
                delay_print("You have already mapped Room 2.")

        elif user_input == "map room 3":
            if current_room == 3:
                if not room3_revealed:
                    delay_print("It is completely dark! You cannot map anything in pitch black darkness.")
                elif bone_placed and bracelet_placed:
                    check_puzzle_completion()
                else:
                    delay_print(MAP_ROOM3_EARLY)
                    ending_achieved = "Eternal Sleep"
                    game_over = True
            else:
                delay_print("You haven't even reached Room 3 yet! How do you want to map it?")

        elif command == "quit":
            delay_print("Thanks for playing!")
            ending_achieved = "Abandoned Cave"
            break
        else:
            delay_print("Unknown command. Type 'help' to see available commands.")

    # End Game
    total_time_used = round(time.time() - start_time, 1)
    delay_print("\n--- Game Over ---", delay_after=1.0)

    # Trigger execution inside week7 module
    scoresaving.end_game_processing(player_name, total_time_used, ending_achieved)


# --- Main Entry Point ---
if __name__ == "__main__":
    game_loop()
