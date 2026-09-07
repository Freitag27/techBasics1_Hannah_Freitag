import os
import datetime
import pygame

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATS_FILE_PATH = os.path.join(BASE_DIR, "trembling_tunnels_stats.txt")

# All six endings in display order.
ALL_ENDINGS = [
    ("intro_decision_no",       "Left before entering the cave"),
    ("chapter_3_critter",       "Picked up the poisonous worm"),
    ("chapter_5_no_rocks",      "Got stuck in the stalactites"),
    ("chapter_7_missing_items", "Fell asleep in the dark"),
    ("chapter_7_leave_map",     "Left the map with the skeleton"),
    ("chapter_7_money",         "Mapped the cave for Mr. McMoney"),
]

# Session state -- reset by start_session() at the start of every run.
_current_name = "Unknown"
_session_start = None
_unlocked_this_session = set()  # prevents double-writing within one run


def start_session(player_name):
    """Calls once when  player starts  new game,  after they type name. Resets  session  so nothing   previous run blocks."""
    global _current_name, _session_start, _unlocked_this_session
    _current_name = player_name
    _session_start = datetime.datetime.now()
    _unlocked_this_session = set()


def unlock_ending(ending_key):

    global _unlocked_this_session

    if ending_key in _unlocked_this_session:
        return

    if _session_start is None:
        time_used = "00:00"
    else:
        elapsed = datetime.datetime.now() - _session_start
        total_seconds = int(elapsed.total_seconds())
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        time_used = f"{minutes:02d}:{seconds:02d}"

    current_date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")

    try:
        with open(STATS_FILE_PATH, "a") as f:
            f.write(f"{_current_name},{current_date},{time_used},{ending_key}\n")
        _unlocked_this_session.add(ending_key)
    except Exception as e:
        print(f"Error saving ending: {e}")


def get_unlocked_endings():
    """Returns list of (key, description, date_or_None, name_or_None)
    for every ending in ALL_ENDINGS."""


    first_records = {}

    if os.path.exists(STATS_FILE_PATH):
        try:
            with open(STATS_FILE_PATH, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    # Each line: name,date,time,ending_key
                    if len(parts) == 4:
                        saved_name, saved_date, saved_time, saved_ending = parts
                        # Keep only the first record per ending key.
                        if saved_ending not in first_records:
                            first_records[saved_ending] = (saved_date, saved_name)
        except Exception as e:
            print(f"Error reading stats file: {e}")

    result = []
    for key, description in ALL_ENDINGS:
        if key in first_records:
            date, name = first_records[key]
            result.append((key, description, date, name))
        else:
            result.append((key, description, None, None))
    return result


def get_total_endings_count():

    unlocked_keys = set()

    if os.path.exists(STATS_FILE_PATH):
        try:
            with open(STATS_FILE_PATH, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 4:
                        saved_ending = parts[3]
                        unlocked_keys.add(saved_ending)
        except Exception as e:
            print(f"Error reading stats file: {e}")

    return len(unlocked_keys), len(ALL_ENDINGS)


#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# ACHIEVEMENTS SCREEN
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def show_achievements(screen):
    """Scene function: draws the achievements screen showing all six endings and whether they have been unlocked or 'quit' if the window is closed."""

    pygame.font.init()

    title_font = pygame.font.SysFont("Poor Richard", 42)
    entry_font = pygame.font.SysFont("Poor Richard", 26)
    small_font  = pygame.font.SysFont("Poor Richard", 20)

    BLACK        = (0,   0,   0)
    WHITE        = (255, 255, 255)
    GOLD         = (212, 175, 55)
    GREY         = (120, 120, 120)
    TEXTBOX_BG   = (20,  20,  20)
    TEXTBOX_BORDER = (200, 200, 200)

    BACK_BUTTON_RECT = pygame.Rect(30, SCREEN_HEIGHT - 60, 140, 40)

    clock = pygame.time.Clock()

    while True:


        entries = get_unlocked_endings()
        unlocked_count, total_count = get_total_endings_count()

        # --- Events ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return None
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if BACK_BUTTON_RECT.collidepoint(event.pos):
                    return None

        # --- Draw ---
        screen.fill(BLACK)

        # Title
        title_surface = title_font.render("Achievements", True, WHITE)
        screen.blit(title_surface, (
            SCREEN_WIDTH // 2 - title_surface.get_width() // 2, 30
        ))

        # Progress
        progress_text = small_font.render(
            f"{unlocked_count} / {total_count} endings unlocked", True, GREY
        )
        screen.blit(progress_text, (
            SCREEN_WIDTH // 2 - progress_text.get_width() // 2, 85
        ))

        pygame.draw.line(screen, TEXTBOX_BORDER,
                         (40, 110), (SCREEN_WIDTH - 40, 110), 1)

        y = 125
        ROW_HEIGHT = 68
        PADDING    = 14

        for key, description, date, name in entries:

            row_rect = pygame.Rect(40, y, SCREEN_WIDTH - 80, ROW_HEIGHT)
            pygame.draw.rect(screen, TEXTBOX_BG,     row_rect)
            pygame.draw.rect(screen, TEXTBOX_BORDER, row_rect, 1)

            if date is not None:
                # Unlocked: description in gold
                desc_surface = entry_font.render(description, True, GOLD)
                screen.blit(desc_surface, (
                    row_rect.left + PADDING,
                    row_rect.top  + PADDING
                ))

                # Date and name on the line below, e.g. '04.09.2022 16:30, "Anna"'
                detail_text = f'{date}, "{name}"'
                detail_surface = small_font.render(detail_text, True, GREY)
                screen.blit(detail_surface, (
                    row_rect.left + PADDING,
                    row_rect.top  + PADDING + entry_font.get_height() + 4
                ))
            else:
                # Locked: question marks
                locked_surface = entry_font.render("???", True, GREY)
                screen.blit(locked_surface, (
                    row_rect.left + PADDING,
                    row_rect.top  + (ROW_HEIGHT - entry_font.get_height()) // 2
                ))

            y += ROW_HEIGHT + 6

        # Back button
        mouse_pos  = pygame.mouse.get_pos()
        back_hover = BACK_BUTTON_RECT.collidepoint(mouse_pos)
        pygame.draw.rect(
            screen,
            (120, 120, 120) if back_hover else (70, 70, 70),
            BACK_BUTTON_RECT
        )
        pygame.draw.rect(screen, WHITE, BACK_BUTTON_RECT, 2)
        back_text = entry_font.render("Back", True, WHITE)
        screen.blit(back_text, (
            BACK_BUTTON_RECT.centerx - back_text.get_width() // 2,
            BACK_BUTTON_RECT.centery - back_text.get_height() // 2
        ))

        pygame.display.update()
        clock.tick(60)