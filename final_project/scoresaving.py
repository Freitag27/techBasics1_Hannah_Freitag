import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATS_FILE_PATH = os.path.join(BASE_DIR, "trembling_tunnels_stats.txt")


def end_game_processing(name, time_used, ending):
    """Kept for backwards compatibility. The main game now calls
    achievements.unlock_ending() directly, but this function still works
    if called manually."""
    current_date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    save_record(name, current_date, time_used, ending)


def save_record(name, date_str, time_used, ending):
    try:
        with open(STATS_FILE_PATH, "a") as f:
            f.write(f"{name},{date_str},{time_used},{ending}\n")
    except Exception as e:
        print(f"Error writing to stats file: {e}")


def get_leaderboard_entries():
    """Returns all saved records as a list of [name, date, time, ending]
    lists, newest first. Returns an empty list if the file does not exist
    or cannot be read."""
    if not os.path.exists(STATS_FILE_PATH):
        return []
    entries = []
    try:
        with open(STATS_FILE_PATH, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                # Guard against blank lines or lines with the wrong number
                # of fields -- these would crash any screen trying to
                # display entries[i][0] etc.
                if len(parts) == 4 and any(p.strip() for p in parts):
                    entries.append(parts)
    except Exception as e:
        print(f"Error loading records: {e}")
    # Reverse so the most recent play appears at the top of any list.
    return list(reversed(entries))
    entries = []
    try:
        with open(STATS_FILE_PATH, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    entries.append(parts)
    except Exception as e:
        print(f"Error loading records: {e}")
    return entries