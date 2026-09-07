"""
⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
 TREMBLING TUNNELS -- HOW THIS FILE WORKS
⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
CHAPTER NUMBERING
⫘⫘⫘⫘⫘⫘⫘⫘
    Chapter 1 -> intro
    Chapter 2 -> transition into Room 1
    Chapter 3 -> Room 1
    Chapter 4 -> transition into Room 2
    Chapter 5 -> Room 2
    Chapter 6 -> transition into Room 3
    Chapter 7 -> Room 3 and the ending
"""

import pygame
import os
import achievements


pygame.font.init()


# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# SCREEN
# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# COLORS
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

TEXTBOX_BG = (20, 20, 20)
TEXTBOX_BORDER = (200, 200, 200)


#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# ASSETS
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

script_dir = os.path.dirname(os.path.abspath(__file__))

Background_path_intro = os.path.join(script_dir, "assets", "backgrounds", "intro.JPG")
Background_path_two_four_six = os.path.join(script_dir, "assets", "backgrounds", "room_two_four_six.png")
Background_path_drkchap3 = os.path.join(script_dir, "assets", "backgrounds", "room_one_dark.jpg")
Background_path_chap3 = os.path.join(script_dir, "assets", "backgrounds", "room_one.jpg")
Background_path_drkchap5 = os.path.join(script_dir, "assets", "backgrounds", "room_two_dark.PNG")
Background_path_chap5 = os.path.join(script_dir, "assets", "backgrounds", "room_two.jpg")
Background_path_drkchap7 = os.path.join(script_dir, "assets", "backgrounds", "room_three_dark.jpg")
Background_path_chap7 = os.path.join(script_dir, "assets", "backgrounds", "room_three.jpg")

FLASHLIGHT_PATH = os.path.join(script_dir, "assets", "items", "lamp.PNG")
MAP_PATH = os.path.join(script_dir, "assets", "items", "map.PNG")
BRACELET_PATH = os.path.join(script_dir, "assets", "items", "bracelet.PNG")
ROCKS_PATH = os.path.join(script_dir, "assets", "items", "rocks.PNG")
SKULL_PATH = os.path.join(script_dir, "assets", "items", "skull.PNG")
WORM_PATH = os.path.join(script_dir, "assets", "items", "worm_mini.PNG")

SKELETON_BEGINNING_PATH = os.path.join(script_dir, "assets", "other", "skelleton_beginning.PNG")
SKELETON_W_BRACELET_PATH = os.path.join(script_dir, "assets", "other", "skelleton_w_bracelet.PNG")
SKELETON_W_HEAD_PATH = os.path.join(script_dir, "assets", "other", "skelleton_w_head.PNG")
SKELETON_W_HEADNBRACELET_PATH = os.path.join(script_dir, "assets", "other", "skelleton_w_headnbracelet.PNG")
SPIRIT_PATH = os.path.join(script_dir, "assets", "other", "spirit_10.PNG")


#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# FONT
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

font = pygame.font.SysFont("Poor Richard", 28)


# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# BACKGROUNDS
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

def load_background(path):
    image = pygame.image.load(path)
    return pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))


Intro_background = load_background(Background_path_intro)
TwoFourSix_background = load_background(Background_path_two_four_six)
Room1_dark_background = load_background(Background_path_drkchap3)
Room1_lit_background = load_background(Background_path_chap3)
Room2_dark_background = load_background(Background_path_drkchap5)
Room2_lit_background = load_background(Background_path_chap5)
Room3_dark_background = load_background(Background_path_drkchap7)
Room3_lit_background = load_background(Background_path_chap7)


# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# DIALOGUE
# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

INTRO_LINES = [
    "*Welcome to Trembling Tunnels, a cave exploration game. To proceed press enter, to use items, double tap*",
    "You are standing on a meadow with tents set up around a strange-looking rock formation.",
    "There are workers hurrying running around, carrying all kinds of ominous devices.",
    "However, most of your attention is focused on the man in front of you, who is dressed way too formally for the outdoors.",
    "He shakes your hand firmly. 'You must be {name}, our great explorer, yes?'",
    "'My name is Mr. McMoney™ the benefactor to this entire operation and owner of this meadow.'",
    "'As you can see we are preparing everything for your adventure into the cave system. The entrance has only been discovered recently.'",
    "'Some of my people have tried the descent, but none of them had anything sensible to say after returning.'",
    "'But I, for one, do not believe in hocus-pocus like ghosts, monsters, or even horoscopes! ... and I'm sure you don't either.'",
    "'Therefore, you will be able to do what your predecessors have failed to do: explore and then map the cave!'",
    "'That's all you need to do, and you'll be paid handsomely.'",
    "After all, people like us only believe in profit, right?",
    "'...hm... cave-explorers believe in thrill too, I suppose... But enough talking! Time is money after all.'"
]

INTRO_DECISION = ["'So, are you up for the challenge?'"]

INTRO_DECISION_YES = [
    "'Very well. Now, you will need some equipment. Let's start with picking up this flashlight.'",
    "'Alright, you now have a flashlight and your mapping tools... Why am I even explaining that? You see them... off you go.'",
    "Mr. McMoney™'s people give you one last safety brief before you make your way to the cave entrance."
]

INTRO_DECISION_NO = [
    "You notice your immediate distrust in Mr. McMoney™ and a gut feeling of danger.",
    "As a cave explorer, you know when to listen to your body. It's best to leave.",
    "Without another word you get back into your car and drive off.",
    "You hear Mr. McMoney™ screaming after you: 'Don't you dare! I will remember you {name}!'",
    "Still, a lingering curiosity of what might have waited for you in that cave stays with you.",
    "Who knows when that feeling will subside..."
]

CHAPTER_2_LINES = [
    "You are led to a small opening between some rocks. The edges are sharp and uninviting, the opening seemingly too narrow.",
    "You contort your head to the side, climbing into the cave head first.",
    "As you twist and wiggle your body, you feel the cold edges of the stone pressing against your ears.",
    "Breathing soon becomes harder, as the passages becomes more narrow, you start stragegically holding your breath.",
    "Blood pulses in your head as the path starts decreasing in altitude.",
    "You keep pushing, knowing the dangers of staying upside-down for too long.",
    "Sure enough, you come to an opening."
]

CHAPTER_3_LINES = [
    "You lie still for a few seconds, appreciating the feeling of being able to expand your ribcage fully. It is pretty dark, though."
]
CHAPTER_3_LINES_LIGHT = [
    "You turn on your flashlight to look for anything interesting this room might have to offer."
]
CHAPTER_3_CRITTER_ENDING = [
    "You pick up a critter that squirms in your hands, trying to get away from you.",
    "Just as you try to put it into your pocket, you feel your hand start to burn. Soon after, you suddenly gasp for air:",
    "Seems like the worm was poisonous…",
    "Maybe someone else less interested in wildlife will map the cave someday...",
    "GAME OVER\n-visit the Achievements page to see how many endings you have unlocked-"
]

ROCKS_DESCRIPTION = ["You pick up a few rocks from the ground."]
BRACELET_DESCRIPTION = [
    "You pick up a scratched up bracelet. It was probably very beautiful once.",
]

CHAPTER_4_LINES = [
    "You quickly map the first room and head deeper into the cave.",
    "The walls get damper the further you go.",
    "Your nose picks up an increasingly rotten smell coming from slimy algae on the walls.",
    "After a while, you arrive in the next room."
]

CHAPTER_5_LINES_DARK = [
    "Your breath echoes through the room- you can tell it is bigger than the last one."
]
CHAPTER_5_LINES = [
    " The hall is filled with big and sharp stalactites. Every now and then you hear the sound of water dripping off of them."
]
CHAPTER_5_MAP_FAIL = [
    "You map this room to the best of your ability, but the stalactites block your way."
]
CHAPTER_5_NO_ROCKS_ENDING = [
    "You try to squeeze through the stalactites but you get stuck between them. If only you had a tool to break them...",
    "GAME OVER\n-visit the Achievements page to see how many endings you have unlocked-"
]
CHAPTER_5_ROCKS = [
    "You slam the rocks against the stalactites blocking your way to the next room.",
    "Did you know stalactites only grows one centimeter every one hundred years?"
]

SKULL_DESCRIPTION = ["You feel a knot form in your stomach as you pick up a human skull."]

CHAPTER_6_LINES = [
    "You crawl along a small, muddy path. Your hands and legs sink into it with every forward motion.",
    "After a while, you feel a gust of wind swirling around your face.",
    "Wind this deep in a cave? How curious...",
    "After a while you feel around and are able to get up again."
]

CHAPTER_7_LINES = [
    "You look around with the flashlight, and a gasp fills the empty chamber in which you stand.",
    "In front of you lies a skeleton, unmistakably human.",
    "Your heart starts pounding as you realize that, if you had crawled farther, you would have crawled right over it.",
    "The wind whispers around your ears."
]
CHAPTER_7_MISSING_ITEMS_ENDING = [
    "The wind is stronger this time. It disrupts your flashlight.",
    "You feel like you have invaded this space. Something or someone else is clearly occupying it.",
    "'Hello?' You try your luck. Your vocal cords are strained from the journey and from not speaking for a prolonged period of time.",
    "You feel the wind again, harsh and hostile. Did it say '{name}'?",
    "Maybe she was hoping you'd give back what was hers to begin with.",
    "You feel one final wind, before tiredness overcomes you.",
    "Eyes closing, the wind being your lullaby, as you drift to sleep forever.",
    "GAME OVER\n-visit the Achievements page to see how many endings you have unlocked-"
]
CHAPTER_7_GIVE_SKULL = [
    "Carefully, you balance the skull you found on top of the head of the skeleton. A gentle breeze meets your face and gives you fresh air to breathe."
]
CHAPTER_7_GIVE_BRACELET = [
    "You carefully slide the bracelet around one of the arms of the skeleton. The wind becomes stronger once more, then peacefully abides.",
    "You can't help but stare at the final resting place and wonder about who this person was."
]
CHAPTER_7_DECISION = [
    "A quiet peacefulness settles over the room. You sit down, resting for a while and pondering your experiences in this strange cave.",
    "Do you want to map the last room and report back to Mr. McMoney™, or do you leave the map here and tell him the cave is nothing special?"
]
CHAPTER_7_MONEY_ENDING = [
    "You map the third room and head back to Mr. McMoney™, where your payment awaits you.",
    "GAME OVER\n-visit the Achievements page to see how many endings you have unlocked-"
]
CHAPTER_7_LEAVE_MAP_ENDING = [
    "You place the map carefully next to the skeleton and leave it there, determined to let this entity rest.",
    "You plan to report to Mr. McMoney™ that the cave is unimportant and small and that it should be sealed. You head back the way you came.",
    "GAME OVER\n-visit the Achievements page to see how many endings you have unlocked-"
]


# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# TEXTBOX
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

TEXTBOX_RECT = pygame.Rect(40, SCREEN_HEIGHT - 140, SCREEN_WIDTH - 80, 95)
MS_PER_CHARACTER = 30


# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# DEBUG
# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

DEBUG_MODE = False
START_SCENE = "intro"
DOUBLE_CLICK_TIME = 400


#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# BUTTONS
# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

BUTTON_LEFT_RECT = pygame.Rect(160, 340, 200, 60)
BUTTON_RIGHT_RECT = pygame.Rect(440, 340, 200, 60)


# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# FLASHLIGHT
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

FLASHLIGHT_RECT = pygame.Rect(280, 480, 120, 120)


# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# INVENTORY
# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

INVENTORY_X = 500
INVENTORY_Y = 20
INVENTORY_SLOT_SIZE = 50
INVENTORY_SLOT_GAP = 10
MAX_INVENTORY_SLOTS = 5


#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# ROOM LAYOUT
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

ROOM_ITEM_SIZE = 60

ROOM1_ROCKS_RECT = pygame.Rect(400, 260, ROOM_ITEM_SIZE, ROOM_ITEM_SIZE)
ROOM1_BRACELET_RECT = pygame.Rect(600, 400, ROOM_ITEM_SIZE, ROOM_ITEM_SIZE)
ROOM1_CRITTER_RECT = pygame.Rect(100, 100, ROOM_ITEM_SIZE, ROOM_ITEM_SIZE)

ROOM2_SKULL_RECT = pygame.Rect(300, 400, ROOM_ITEM_SIZE, ROOM_ITEM_SIZE)

ROOM3_SKELETON_RECT = pygame.Rect(280, 220, 180, 140)


#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# ITEM IMAGES
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

def load_scaled(path, size):
    image = pygame.image.load(path)
    return pygame.transform.scale(image, (size, size))



Flashlight_image = load_scaled(FLASHLIGHT_PATH, FLASHLIGHT_RECT.width)
# Here it's full size for when it sits on the ground in the intro scene


MAP_ICON_SIZE = INVENTORY_SLOT_SIZE - 10
# Smaller version that fits neatly inside an inventory slot.
Flashlight_icon_image = load_scaled(FLASHLIGHT_PATH, MAP_ICON_SIZE)
Map_image = load_scaled(MAP_PATH, MAP_ICON_SIZE)
Bracelet_image = load_scaled(BRACELET_PATH, MAP_ICON_SIZE)
Bracelet_room_image = load_scaled(BRACELET_PATH, ROOM_ITEM_SIZE)
Rocks_image = load_scaled(ROCKS_PATH, MAP_ICON_SIZE)
Rocks_room_image = load_scaled(ROCKS_PATH, ROOM_ITEM_SIZE)
Skull_image = load_scaled(SKULL_PATH, MAP_ICON_SIZE)
Skull_room_image = load_scaled(SKULL_PATH, ROOM_ITEM_SIZE)
Worm_room_image = load_scaled(WORM_PATH, ROOM_ITEM_SIZE)

Skeleton_beginning_image = pygame.transform.scale(
    pygame.image.load(SKELETON_BEGINNING_PATH),
    (ROOM3_SKELETON_RECT.width, ROOM3_SKELETON_RECT.height)
)
Skeleton_w_bracelet_image = pygame.transform.scale(
    pygame.image.load(SKELETON_W_BRACELET_PATH),
    (ROOM3_SKELETON_RECT.width, ROOM3_SKELETON_RECT.height)
)
Skeleton_w_head_image = pygame.transform.scale(
    pygame.image.load(SKELETON_W_HEAD_PATH),
    (ROOM3_SKELETON_RECT.width, ROOM3_SKELETON_RECT.height)
)
Skeleton_w_headnbracelet_image = pygame.transform.scale(
    pygame.image.load(SKELETON_W_HEADNBRACELET_PATH),
    (ROOM3_SKELETON_RECT.width, ROOM3_SKELETON_RECT.height)
)
Spirit_image = pygame.image.load(SPIRIT_PATH)
ROOM3_SPIRIT_RECT = pygame.Rect(700, 190, 120, 140)

ITEM_IMAGES = {
    "flashlight": Flashlight_icon_image,
    "map": Map_image,
    "bracelet": Bracelet_image,
    "rocks": Rocks_image,
    "skull": Skull_image,
}

ITEM_TOOLTIPS = {
    "flashlight": "Flashlight",
    "map": "Map",
    "bracelet": "Bracelet",
    "rocks": "Rocks",
    "skull": "Skull",
}

inventory_tooltip_font = pygame.font.SysFont("Poor Richard", 22)


def get_skeleton_image(skull_given, bracelet_given):
    if skull_given and bracelet_given:
        return Skeleton_w_headnbracelet_image
    if skull_given:
        return Skeleton_w_head_image
    if bracelet_given:
        return Skeleton_w_bracelet_image
    return Skeleton_beginning_image


# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# TEXT WRAPPING
# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

def wrap_text(text, font, max_width):
    """Turns one long string into a list of shorter strings that each
    fit inside max_width pixels. """
    paragraphs = text.split("\n")

    lines = []

    for paragraph in paragraphs:

        # An empty paragraph (from a leading/trailing \n) becomes a
        # blank line in the output.
        if paragraph.strip() == "":
            lines.append("")
            continue

        words = paragraph.split(" ")
        current_line = ""

        for word in words:
            test_line = (current_line + " " + word).strip()
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word

        if current_line:
            lines.append(current_line)

    return lines

# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# PLAYER NAME
# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

def get_player_name(screen):
    player_name = ""
    clock = pygame.time.Clock()
    QUESTION_RECT = pygame.Rect(200, 180, 400, 70)
    INPUT_RECT = pygame.Rect(200, 280, 400, 70)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                elif event.key == pygame.K_RETURN:
                    if player_name.strip() != "":
                        return player_name.strip()
                else:
                    if event.unicode.isprintable():
                        if len(player_name) < 20:
                            player_name += event.unicode

        screen.blit(Intro_background, (0, 0))

        pygame.draw.rect(screen, TEXTBOX_BG, QUESTION_RECT)
        pygame.draw.rect(screen, TEXTBOX_BORDER, QUESTION_RECT, 2)
        question_text = font.render("What is your name?", True, WHITE)
        screen.blit(question_text, (
            QUESTION_RECT.centerx - question_text.get_width() // 2,
            QUESTION_RECT.centery - question_text.get_height() // 2
        ))

        pygame.draw.rect(screen, TEXTBOX_BG, INPUT_RECT)
        pygame.draw.rect(screen, TEXTBOX_BORDER, INPUT_RECT, 2)
        typed_name = font.render(player_name, True, WHITE)
        screen.blit(typed_name, (
            INPUT_RECT.centerx - typed_name.get_width() // 2,
            INPUT_RECT.centery - typed_name.get_height() // 2
        ))

        instruction_font = pygame.font.SysFont("Poor Richard", 20)
        instruction = instruction_font.render("Press Enter to continue", True, WHITE)
        screen.blit(instruction, (SCREEN_WIDTH // 2 - instruction.get_width() // 2, 380))

        pygame.display.update()
        clock.tick(60)


# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# DEBUG KEYS
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

def get_debug_scene(event):
    if not DEBUG_MODE:
        return None
    debug_keys = {
        pygame.K_F1: "intro",
        pygame.K_F2: "chapter_2",
        pygame.K_F3: "chapter_3",
        pygame.K_F4: "chapter_4",
        pygame.K_F5: "chapter_5",
        pygame.K_F6: "chapter_6",
        pygame.K_F7: "chapter_7",
    }
    if event.key in debug_keys:
        return debug_keys[event.key]
    return None


#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# INVENTORY DRAWING
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

def get_inventory_slot_rect_for_item(inventory, item_name):
    if item_name not in inventory:
        return None
    slot_index = inventory.index(item_name)
    if slot_index >= MAX_INVENTORY_SLOTS:
        return None
    slot_x = INVENTORY_X + slot_index * (INVENTORY_SLOT_SIZE + INVENTORY_SLOT_GAP)
    return pygame.Rect(slot_x, INVENTORY_Y, INVENTORY_SLOT_SIZE, INVENTORY_SLOT_SIZE)


def draw_inventory(screen, inventory):
    mouse_position = pygame.mouse.get_pos()
    hovered_item_name = None
    hovered_slot_rect = None

    inventory_width = (
        MAX_INVENTORY_SLOTS * INVENTORY_SLOT_SIZE
        + (MAX_INVENTORY_SLOTS - 1) * INVENTORY_SLOT_GAP
        + 20
    )
    inventory_rect = pygame.Rect(
        INVENTORY_X - 10, INVENTORY_Y - 10,
        inventory_width, INVENTORY_SLOT_SIZE + 20
    )
    pygame.draw.rect(screen, TEXTBOX_BG, inventory_rect)
    pygame.draw.rect(screen, TEXTBOX_BORDER, inventory_rect, 2)

    for slot_number in range(MAX_INVENTORY_SLOTS):
        slot_x = INVENTORY_X + slot_number * (INVENTORY_SLOT_SIZE + INVENTORY_SLOT_GAP)
        slot_rect = pygame.Rect(slot_x, INVENTORY_Y, INVENTORY_SLOT_SIZE, INVENTORY_SLOT_SIZE)
        pygame.draw.rect(screen, (60, 60, 60), slot_rect)
        pygame.draw.rect(screen, WHITE, slot_rect, 2)

        if slot_number < len(inventory):
            item_name = inventory[slot_number]
            item_image = ITEM_IMAGES.get(item_name)
            if item_image is not None:
                screen.blit(item_image, item_image.get_rect(center=slot_rect.center))
            if slot_rect.collidepoint(mouse_position):
                hovered_item_name = item_name
                hovered_slot_rect = slot_rect

    if hovered_item_name is not None:
        tooltip_surface = inventory_tooltip_font.render(
            ITEM_TOOLTIPS.get(hovered_item_name, hovered_item_name), True, WHITE
        )
        screen.blit(tooltip_surface, tooltip_surface.get_rect(
            midtop=(hovered_slot_rect.centerx, hovered_slot_rect.bottom + 5)
        ))


def draw_simple_tooltip(screen, label, mouse_position):
    tooltip_surface = inventory_tooltip_font.render(label, True, WHITE)
    screen.blit(tooltip_surface, tooltip_surface.get_rect(
        midbottom=(mouse_position[0], mouse_position[1] - 10)
    ))


def check_double_click(clicked_name, last_click_name, last_click_time, now):
    is_double = clicked_name == last_click_name and now - last_click_time <= DOUBLE_CLICK_TIME
    return is_double, clicked_name, now


#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# DIALOGUE
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

def run_dialogue(screen, dialogue_lines, player_name, inventory=None, background=None):
    if background is None:
        background = Intro_background

    clock = pygame.time.Clock()
    line_index = 0
    visible_chars = 0
    last_char_time = pygame.time.get_ticks()

    while line_index < len(dialogue_lines):
        current_line = dialogue_lines[line_index].replace("{name}", player_name)
        line_fully_shown = visible_chars >= len(current_line)
        now = pygame.time.get_ticks()

        if not line_fully_shown and now - last_char_time >= MS_PER_CHARACTER:
            visible_chars += 1
            last_char_time = now

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                debug_scene = get_debug_scene(event)
                if debug_scene is not None:
                    return debug_scene
                if event.key == pygame.K_ESCAPE:
                    return "quit"
                elif event.key in (pygame.K_SPACE, pygame.K_RETURN):
                    if not line_fully_shown:
                        visible_chars = len(current_line)
                    else:
                        line_index += 1
                        visible_chars = 0
                        last_char_time = pygame.time.get_ticks()

        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, TEXTBOX_BG, TEXTBOX_RECT)
        pygame.draw.rect(screen, TEXTBOX_BORDER, TEXTBOX_RECT, 2)

        wrapped_lines = wrap_text(current_line[:visible_chars], font, TEXTBOX_RECT.width - 20)
        y = TEXTBOX_RECT.top + 10
        for wrapped_line in wrapped_lines:
            screen.blit(font.render(wrapped_line, True, WHITE), (TEXTBOX_RECT.left + 10, y))
            y += font.get_height() + 4

        if inventory is not None:
            draw_inventory(screen, inventory)

        pygame.display.update()
        clock.tick(60)

    return None


#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# TWO-BUTTON CHOICE
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

def run_choice_scene(screen, question_line, player_name, left_label, right_label,
                     background=None, inventory=None):
    if background is None:
        background = Intro_background

    clock = pygame.time.Clock()
    current_line = question_line.replace("{name}", player_name)
    visible_chars = 0
    last_char_time = pygame.time.get_ticks()

    while True:
        line_fully_shown = visible_chars >= len(current_line)
        now = pygame.time.get_ticks()

        if not line_fully_shown and now - last_char_time >= MS_PER_CHARACTER:
            visible_chars += 1
            last_char_time = now

        mouse_position = pygame.mouse.get_pos()
        left_hover = BUTTON_LEFT_RECT.collidepoint(mouse_position)
        right_hover = BUTTON_RIGHT_RECT.collidepoint(mouse_position)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                debug_scene = get_debug_scene(event)
                if debug_scene is not None:
                    return debug_scene
                if event.key == pygame.K_ESCAPE:
                    return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if BUTTON_LEFT_RECT.collidepoint(event.pos):
                    return "left"
                if BUTTON_RIGHT_RECT.collidepoint(event.pos):
                    return "right"

        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, TEXTBOX_BG, TEXTBOX_RECT)
        pygame.draw.rect(screen, TEXTBOX_BORDER, TEXTBOX_RECT, 2)

        wrapped_lines = wrap_text(current_line[:visible_chars], font, TEXTBOX_RECT.width - 20)
        y = TEXTBOX_RECT.top + 10
        for wrapped_line in wrapped_lines:
            screen.blit(font.render(wrapped_line, True, WHITE), (TEXTBOX_RECT.left + 10, y))
            y += font.get_height() + 4

        pygame.draw.rect(screen, (120, 120, 120) if left_hover else (70, 70, 70), BUTTON_LEFT_RECT)
        pygame.draw.rect(screen, WHITE, BUTTON_LEFT_RECT, 3)
        pygame.draw.rect(screen, (120, 120, 120) if right_hover else (70, 70, 70), BUTTON_RIGHT_RECT)
        pygame.draw.rect(screen, WHITE, BUTTON_RIGHT_RECT, 3)

        left_text = font.render(left_label, True, WHITE)
        right_text = font.render(right_label, True, WHITE)
        screen.blit(left_text, (
            BUTTON_LEFT_RECT.centerx - left_text.get_width() // 2,
            BUTTON_LEFT_RECT.centery - left_text.get_height() // 2
        ))
        screen.blit(right_text, (
            BUTTON_RIGHT_RECT.centerx - right_text.get_width() // 2,
            BUTTON_RIGHT_RECT.centery - right_text.get_height() // 2
        ))

        if inventory is not None:
            draw_inventory(screen, inventory)

        pygame.display.update()
        clock.tick(60)


def run_decision(screen, player_name, inventory=None):
    result = run_choice_scene(
        screen, INTRO_DECISION[0], player_name, "Leave", "Stay",
        background=Intro_background, inventory=inventory
    )
    if result == "left":
        return "leave"
    if result == "right":
        return "stay"
    return result


# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# FLASHLIGHT PICKUP
# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

def run_flashlight_scene(screen, inventory):
    clock = pygame.time.Clock()
    last_click_time = None

    while True:
        mouse_position = pygame.mouse.get_pos()
        hovering_flashlight = FLASHLIGHT_RECT.collidepoint(mouse_position)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                debug_scene = get_debug_scene(event)
                if debug_scene is not None:
                    return debug_scene
                if event.key == pygame.K_ESCAPE:
                    return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if FLASHLIGHT_RECT.collidepoint(event.pos):
                    now = pygame.time.get_ticks()
                    if last_click_time is not None and now - last_click_time <= DOUBLE_CLICK_TIME:
                        if "flashlight" not in inventory:
                            inventory.append("flashlight")
                        return "picked_up"
                    last_click_time = now

        screen.blit(Intro_background, (0, 0))
        draw_inventory(screen, inventory)
        screen.blit(Flashlight_image, FLASHLIGHT_RECT)
        if hovering_flashlight:
            draw_simple_tooltip(screen, "Flashlight", (FLASHLIGHT_RECT.centerx, FLASHLIGHT_RECT.top))

        pygame.display.update()
        clock.tick(60)


# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# INTRO
# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

def run_intro(screen, player_name, inventory):
    result = run_dialogue(screen, INTRO_LINES, player_name, inventory)
    if result is not None:
        return result

    decision = run_decision(screen, player_name, inventory)
    if decision not in ("leave", "stay"):
        return decision

    if decision == "leave":
        result = run_dialogue(screen, INTRO_DECISION_NO, player_name, inventory)
        # unlock BEFORE returning so the save always happens
        achievements.unlock_ending("intro_decision_no")
        if result is not None:
            return result
        return None

    result = run_dialogue(screen, [INTRO_DECISION_YES[0]], player_name, inventory)
    if result is not None:
        return result

    flashlight_result = run_flashlight_scene(screen, inventory)
    if flashlight_result != "picked_up":
        return flashlight_result

    result = run_dialogue(screen, INTRO_DECISION_YES[1:], player_name, inventory)
    if result is not None:
        return result

    return "chapter_2"


# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# ROOM 1 PREP
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

def run_room_scene(screen, dark_background, lit_background, ground_items, inventory, room_state):
    """Room 1 exploration loop. room_state is created once in
    run_chapter_3() and passed in every call so revealed and collected
    flags survive between calls."""
    clock = pygame.time.Clock()
    last_click_name = None
    last_click_time = 0

    while True:
        mouse_position = pygame.mouse.get_pos()
        now = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                debug_scene = get_debug_scene(event)
                if debug_scene is not None:
                    return debug_scene
                if event.key == pygame.K_ESCAPE:
                    return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                flashlight_slot_rect = get_inventory_slot_rect_for_item(inventory, "flashlight")
                if (not room_state["revealed"]
                        and flashlight_slot_rect is not None
                        and flashlight_slot_rect.collidepoint(event.pos)):
                    is_double, last_click_name, last_click_time = check_double_click(
                        "flashlight", last_click_name, last_click_time, now
                    )
                    if is_double:
                        room_state["revealed"] = True
                        return "revealed"
                    continue

                if room_state["revealed"]:

                    map_slot_rect = get_inventory_slot_rect_for_item(inventory, "map")
                    if map_slot_rect is not None and map_slot_rect.collidepoint(event.pos):
                        is_double, last_click_name, last_click_time = check_double_click(
                            "map", last_click_name, last_click_time, now
                        )
                        if is_double:
                            return "mapped"
                        continue

                    for item in ground_items:
                        if item.get("collected"):
                            continue
                        if item["rect"].collidepoint(event.pos):
                            is_double, last_click_name, last_click_time = check_double_click(
                                item["name"], last_click_name, last_click_time, now
                            )
                            if is_double:
                                if item["result"] is not None:
                                    return item["result"]
                                if item["pickup"] is not None and item["pickup"] not in inventory:
                                    inventory.append(item["pickup"])
                                item["collected"] = True
                                return "picked_up_" + item["name"]
                            break

        background = lit_background if room_state["revealed"] else dark_background
        screen.blit(background, (0, 0))

        if room_state["revealed"]:
            for item in ground_items:
                if item.get("collected"):
                    continue
                screen.blit(item["room_image"], item["rect"])
                if item["rect"].collidepoint(mouse_position):
                    draw_simple_tooltip(screen, item["tooltip"], mouse_position)

        draw_inventory(screen, inventory)
        pygame.display.update()
        clock.tick(60)


#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# CHAPTER 2
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

def run_chapter_2(screen, player_name, inventory):
    result = run_dialogue(screen, CHAPTER_2_LINES, player_name, inventory,
                          background=TwoFourSix_background)
    if result is not None:
        return result
    return "chapter_3"


#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# CHAPTER 3 -- Room 1
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

def run_chapter_3(screen, player_name, inventory):

    result = run_dialogue(screen, CHAPTER_3_LINES, player_name, inventory,
                          background=Room1_dark_background)
    if result is not None:
        return result

    ground_items = [
        {
            "name": "rocks", "room_image": Rocks_room_image, "rect": ROOM1_ROCKS_RECT,
            "tooltip": "Rocks", "pickup": "rocks", "result": None,
        },
        {
            "name": "bracelet", "room_image": Bracelet_room_image, "rect": ROOM1_BRACELET_RECT,
            "tooltip": "Bracelet", "pickup": "bracelet", "result": None,
        },
        {
            "name": "critter", "room_image": Worm_room_image, "rect": ROOM1_CRITTER_RECT,
            "tooltip": "???", "pickup": None, "result": "poisoned",
        },
    ]

    room_state = {"revealed": False}

    while True:
        room_result = run_room_scene(
            screen, Room1_dark_background, Room1_lit_background,
            ground_items, inventory, room_state
        )

        if room_result == "revealed":
            result = run_dialogue(screen, CHAPTER_3_LINES_LIGHT, player_name, inventory,
                                  background=Room1_lit_background)
            if result is not None:
                return result
            continue

        if room_result == "picked_up_rocks":
            result = run_dialogue(screen, ROCKS_DESCRIPTION, player_name, inventory,
                                  background=Room1_lit_background)
            if result is not None:
                return result
            continue

        if room_result == "picked_up_bracelet":
            result = run_dialogue(screen, BRACELET_DESCRIPTION, player_name, inventory,
                                  background=Room1_lit_background)
            if result is not None:
                return result
            continue

        if room_result == "poisoned":
            # unlock BEFORE returning
            achievements.unlock_ending("chapter_3_critter")
            result = run_dialogue(screen, CHAPTER_3_CRITTER_ENDING, player_name, inventory,
                                  background=Room1_lit_background)
            return result

        if room_result == "mapped":
            return "chapter_4"

        return room_result


# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# CHAPTER 4
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

def run_chapter_4(screen, player_name, inventory):
    result = run_dialogue(screen, CHAPTER_4_LINES, player_name, inventory,
                          background=TwoFourSix_background)
    if result is not None:
        return result
    return "chapter_5"


#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# CHAPTER 5 -- Room 2
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

def run_chapter_5_room(screen, inventory, room_state):
    clock = pygame.time.Clock()
    last_click_name = None
    last_click_time = 0

    while True:
        mouse_position = pygame.mouse.get_pos()
        now = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                debug_scene = get_debug_scene(event)
                if debug_scene is not None:
                    return debug_scene
                if event.key == pygame.K_ESCAPE:
                    return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                flashlight_slot_rect = get_inventory_slot_rect_for_item(inventory, "flashlight")
                if (not room_state["revealed"]
                        and flashlight_slot_rect is not None
                        and flashlight_slot_rect.collidepoint(event.pos)):
                    is_double, last_click_name, last_click_time = check_double_click(
                        "flashlight", last_click_name, last_click_time, now
                    )
                    if is_double:
                        room_state["revealed"] = True
                        return "revealed"
                    continue

                if room_state["revealed"]:

                    if not room_state["skull_collected"] and ROOM2_SKULL_RECT.collidepoint(event.pos):
                        is_double, last_click_name, last_click_time = check_double_click(
                            "skull", last_click_name, last_click_time, now
                        )
                        if is_double:
                            if "skull" not in inventory:
                                inventory.append("skull")
                            room_state["skull_collected"] = True
                            return "skull_pickup"
                        continue

                    map_slot_rect = get_inventory_slot_rect_for_item(inventory, "map")
                    if map_slot_rect is not None and map_slot_rect.collidepoint(event.pos):
                        is_double, last_click_name, last_click_time = check_double_click(
                            "map", last_click_name, last_click_time, now
                        )
                        if is_double:
                            if room_state["stalactites_broken"]:
                                return "mapped"
                            elif not room_state["map_attempted"]:
                                room_state["map_attempted"] = True
                                return "map_fail"
                            elif "rocks" in inventory:
                                return "map_fail"
                            else:
                                return "rocks_not_break"
                        continue

                    rocks_slot_rect = get_inventory_slot_rect_for_item(inventory, "rocks")
                    if (room_state["map_attempted"]
                            and not room_state["stalactites_broken"]
                            and rocks_slot_rect is not None
                            and rocks_slot_rect.collidepoint(event.pos)):
                        is_double, last_click_name, last_click_time = check_double_click(
                            "rocks", last_click_name, last_click_time, now
                        )
                        if is_double:
                            inventory.remove("rocks")
                            room_state["stalactites_broken"] = True
                            return "rocks_break"
                        continue

        background = Room2_lit_background if room_state["revealed"] else Room2_dark_background
        screen.blit(background, (0, 0))

        if room_state["revealed"]:
            if not room_state["skull_collected"]:
                screen.blit(Skull_room_image, ROOM2_SKULL_RECT)
                if ROOM2_SKULL_RECT.collidepoint(mouse_position):
                    draw_simple_tooltip(screen, "Skull", mouse_position)

        draw_inventory(screen, inventory)
        pygame.display.update()
        clock.tick(60)


def run_chapter_5(screen, player_name, inventory):

    result = run_dialogue(screen, CHAPTER_5_LINES_DARK, player_name, inventory,
                          background=Room2_dark_background)
    if result is not None:
        return result

    room_state = {
        "revealed": False,
        "map_attempted": False,
        "stalactites_broken": False,
        "skull_collected": "skull" in inventory,
    }

    while True:
        room_result = run_chapter_5_room(screen, inventory, room_state)

        if room_result == "revealed":
            result = run_dialogue(screen, CHAPTER_5_LINES, player_name, inventory,
                                  background=Room2_lit_background)
            if result is not None:
                return result
            continue

        if room_result == "skull_pickup":
            result = run_dialogue(screen, SKULL_DESCRIPTION, player_name, inventory,
                                  background=Room2_lit_background)
            if result is not None:
                return result
            continue

        if room_result == "map_fail":
            result = run_dialogue(screen, CHAPTER_5_MAP_FAIL, player_name, inventory,
                                  background=Room2_lit_background)
            if result is not None:
                return result
            if "rocks" not in inventory:
                # unlock BEFORE returning
                achievements.unlock_ending("chapter_5_no_rocks")
                result = run_dialogue(screen, CHAPTER_5_NO_ROCKS_ENDING, player_name, inventory,
                                      background=Room2_lit_background)
                return result
            continue

        if room_result == "rocks_not_break":
            # unlock BEFORE returning
            achievements.unlock_ending("chapter_5_no_rocks")
            result = run_dialogue(screen, CHAPTER_5_NO_ROCKS_ENDING, player_name, inventory,
                                  background=Room2_lit_background)
            return result

        if room_result == "rocks_break":
            result = run_dialogue(screen, CHAPTER_5_ROCKS, player_name, inventory,
                                  background=Room2_lit_background)
            if result is not None:
                return result
            continue

        if room_result == "mapped":
            return "chapter_6"

        return room_result


#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# CHAPTER 6
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

def run_chapter_6(screen, player_name, inventory):
    result = run_dialogue(screen, CHAPTER_6_LINES, player_name, inventory,
                          background=TwoFourSix_background)
    if result is not None:
        return result
    return "chapter_7"


#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# CHAPTER 7 -- Room 3
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

def run_chapter_7(screen, player_name, inventory):

    room_state = {
        "revealed": False,
        "skull_given": False,
        "bracelet_given": False,
    }

    while True:
        room_result = run_chapter_7_room(screen, inventory, room_state)

        if room_result == "revealed":
            result = run_dialogue(screen, CHAPTER_7_LINES, player_name, inventory,
                                  background=Room3_lit_background)
            if result is not None:
                return result
            continue

        if room_result == "give_skull":
            result = run_dialogue(screen, CHAPTER_7_GIVE_SKULL, player_name, inventory,
                                  background=Room3_lit_background)
            if result is not None:
                return result
            continue

        if room_result == "give_bracelet":
            result = run_dialogue(screen, CHAPTER_7_GIVE_BRACELET, player_name, inventory,
                                  background=Room3_lit_background)
            if result is not None:
                return result
            continue

        if room_result == "mapped_too_early":
            # unlock BEFORE returning
            achievements.unlock_ending("chapter_7_missing_items")
            result = run_dialogue(screen, CHAPTER_7_MISSING_ITEMS_ENDING, player_name, inventory,
                                  background=Room3_lit_background)
            return result

        if room_result == "mapped":
            result = run_dialogue(screen, [CHAPTER_7_DECISION[0]], player_name, inventory,
                                  background=Room3_lit_background)
            if result is not None:
                return result

            choice = run_choice_scene(
                screen, CHAPTER_7_DECISION[1], player_name,
                "Leave Map", "Map Room 3",
                background=Room3_lit_background, inventory=inventory,
            )

            if choice == "left":
                # unlock BEFORE returning
                achievements.unlock_ending("chapter_7_leave_map")
                result = run_dialogue(screen, CHAPTER_7_LEAVE_MAP_ENDING, player_name, inventory,
                                      background=Room3_lit_background)
                return result

            if choice == "right":
                # unlock BEFORE returning
                achievements.unlock_ending("chapter_7_money")
                result = run_dialogue(screen, CHAPTER_7_MONEY_ENDING, player_name, inventory,
                                      background=Room3_lit_background)
                return result

            return choice

        return room_result


def run_chapter_7_room(screen, inventory, room_state):
    """Room 3 exploration loop."""
    clock = pygame.time.Clock()
    last_click_name = None
    last_click_time = 0


    while True:
        mouse_position = pygame.mouse.get_pos()
        now = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                debug_scene = get_debug_scene(event)
                if debug_scene is not None:
                    return debug_scene
                if event.key == pygame.K_ESCAPE:
                    return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                flashlight_slot_rect = get_inventory_slot_rect_for_item(inventory, "flashlight")
                if (not room_state["revealed"]
                        and flashlight_slot_rect is not None
                        and flashlight_slot_rect.collidepoint(event.pos)):
                    is_double, last_click_name, last_click_time = check_double_click(
                        "flashlight", last_click_name, last_click_time, now
                    )
                    if is_double:
                        room_state["revealed"] = True
                        return "revealed"
                    continue

                if room_state["revealed"]:

                    if not room_state["skull_given"]:
                        skull_slot_rect = get_inventory_slot_rect_for_item(inventory, "skull")
                        if skull_slot_rect is not None and skull_slot_rect.collidepoint(event.pos):
                            is_double, last_click_name, last_click_time = check_double_click(
                                "skull", last_click_name, last_click_time, now
                            )
                            if is_double:
                                inventory.remove("skull")
                                room_state["skull_given"] = True
                                return "give_skull"
                            continue

                    if not room_state["bracelet_given"]:
                        bracelet_slot_rect = get_inventory_slot_rect_for_item(inventory, "bracelet")
                        if bracelet_slot_rect is not None and bracelet_slot_rect.collidepoint(event.pos):
                            is_double, last_click_name, last_click_time = check_double_click(
                                "bracelet", last_click_name, last_click_time, now
                            )
                            if is_double:
                                inventory.remove("bracelet")
                                room_state["bracelet_given"] = True
                                return "give_bracelet"
                            continue

                    map_slot_rect = get_inventory_slot_rect_for_item(inventory, "map")
                    if map_slot_rect is not None and map_slot_rect.collidepoint(event.pos):
                        is_double, last_click_name, last_click_time = check_double_click(
                            "map", last_click_name, last_click_time, now
                        )
                        if is_double:
                            # Room 3 only checks skull_given and bracelet_given --
                            # it has no stalactites or rocks logic.
                            if room_state["skull_given"] and room_state["bracelet_given"]:
                                return "mapped"
                            return "mapped_too_early"
                        continue

        background = Room3_lit_background if room_state["revealed"] else Room3_dark_background
        screen.blit(background, (0, 0))

        if room_state["revealed"]:
            skeleton_image = get_skeleton_image(
                room_state["skull_given"], room_state["bracelet_given"]
            )
            screen.blit(skeleton_image, ROOM3_SKELETON_RECT)
            if ROOM3_SKELETON_RECT.collidepoint(mouse_position):
                draw_simple_tooltip(screen, "Skeleton", mouse_position)

            # Spirit is always visible once the room is lit, as long as
            # both items have not yet been returned.
            # Hovering over it adds the "Spirit" tooltip on top.
            both_given = room_state["skull_given"] and room_state["bracelet_given"]
            if not both_given:
                screen.blit(Spirit_image, ROOM3_SPIRIT_RECT)
                if ROOM3_SPIRIT_RECT.collidepoint(mouse_position):
                    draw_simple_tooltip(screen, "Spirit", mouse_position)

        draw_inventory(screen, inventory)
        pygame.display.update()
        clock.tick(60)


# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# MAIN GAME
# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

def run_game(screen):
    current_scene = START_SCENE
    inventory = ["map"]

    if current_scene == "intro":
        player_name = get_player_name(screen)
        if player_name is None:
            return
        achievements.start_session(player_name)
    else:
        player_name = "Test Explorer"
        inventory.append("flashlight")
        if current_scene == "chapter_5":
            inventory.extend(["rocks", "bracelet"])
        if current_scene in ("chapter_6", "chapter_7"):
            inventory.extend(["bracelet", "skull"])

    while True:
        if current_scene == "intro":
            next_scene = run_intro(screen, player_name, inventory)
        elif current_scene == "chapter_2":
            next_scene = run_chapter_2(screen, player_name, inventory)
        elif current_scene == "chapter_3":
            next_scene = run_chapter_3(screen, player_name, inventory)
        elif current_scene == "chapter_4":
            next_scene = run_chapter_4(screen, player_name, inventory)
        elif current_scene == "chapter_5":
            next_scene = run_chapter_5(screen, player_name, inventory)
        elif current_scene == "chapter_6":
            next_scene = run_chapter_6(screen, player_name, inventory)
        elif current_scene == "chapter_7":
            next_scene = run_chapter_7(screen, player_name, inventory)
        else:
            return

        if next_scene is None or next_scene == "quit":
            return

        current_scene = next_scene