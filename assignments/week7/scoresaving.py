# scoresaving.py
import datetime
import os

#seeing where game is
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATS_FILE_PATH = os.path.join(BASE_DIR, "trembling_tunnels_stats.txt")


def end_game_processing(name, time_used, ending):
#playing time
    current_date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")

    #saving
    save_record(name, current_date, time_used, ending)

  #leaderboard
    display_leaderboard()


def save_record(name, date_str, time_used, ending):
    try:
        with open(STATS_FILE_PATH, "a") as f:
            f.write(f"{name},{date_str},{time_used},{ending}\n")
    except Exception as e:
        print(f"Error occurred while writing records to database: {e}")


def display_leaderboard():
    print("      TREMBLING TUNNELS - LEADERBOARD        ")

    try:
        if not os.path.exists(STATS_FILE_PATH):
            print("No existing records database found.")
            print("Creating a brand new file registry with current result...")
            return

        with open(STATS_FILE_PATH, "r") as f:
            entries = []
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    entries.append(parts)

            if not entries:
                print("Database is currently empty.")
                return

            # Display records nicely
            print(f"{'Rank':<5} {'Name':<12} {'Date/Time':<17} {'Duration':<10} {'Ending achieved':<20}")
            print("-" * 70)
            for idx, entry in enumerate(entries, start=1):
                print(f"{idx:<5} {entry[0]:<12} {entry[1]:<17} {entry[2]}s{'' :<6} {entry[3]:<20}")

    except FileNotFoundError:
        print("Record file registry missing or deleted.")
    except Exception as e:
        print(f"Error loading leaderboard components: {e}")
    print("=============================================\n")