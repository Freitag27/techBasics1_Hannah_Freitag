#Hello! This is a little simulation, where you need to make the choice of Studying or spending time with friends;
# a decision just like a lot of students have to make in real life! About AI usage:
# I used ChatAIs QWEN to help me understand the process of refractoring, by having it guide me step by step.
#then I tried to apply what the AI did to my own code, without copying the AI code. In this way, I think I could
#achieve the best result and learn something for myself:)
import time

#------CONSTANTS THAT ALWAYS STAY THE SAME------

INTRO = "Welcome to 'Work-life balance, the simulator!!'"
NAME_REQUEST = "What's your name?"
# Scenario
SCENARIO = '''You are on you way home on a sunny afternoon. You meet one of your friends on the way!
How exiting! Will you
 1. Say Hi and continue to go home.
 or will you
 2. ask your friend to do something fun-
since the weather is so nice?'''
ANSWER_REQUEST = "What do you do, answer with 1 or 2!"
CHOICES = ["1", "2", "3"]
#Path one Constants
DECISION_ONE = "You decide to head home despite meeting your friend. You've got so much homework already, it would be irresponsible, to not use your free time to finish it today"
CONSTANT_CHOICE_ONE = "You chose to not see your friend and work. You seem to be very hardworking. Don't forget to chill."
#Path two Constants
DECISION_TWO = "A little time spent with friends is so much more valuable than sitting in front of your laptop and being bored, right? You and your friend decide to go to Penny and pick up some snacks. You have a makeshift picnic on Mensawiese."
CONSTANT_CHOICE_TWO = "You chose to not do your work and chill with your friends.Having fun with your friends is super important! But make sure to not neclect uni work."

#Path three Constants
DECISION_THREE = "You found the secret option! You and your friend decide to study together outside. You enjoy the sunny day AND still get work done. Good for you !!"
CONSTANT_CHOICE_THREE = "You found the secret perfect option!You found the secret perfect option! You either think outside the box or you just tried to stop my programm from working. In any case, good job!"

# Wrong answers constants
DECISION_WRONG = """please choose option 1 or option 2 (or secret option 3) by choosing '1' or '2' (or '3') respectively."""
EXPERIENCE_WRONG = "That wasn't a valid statement and you know it!"

#Asking about experience
EXPERIENCE_REQUEST = "How happy are you with your choice on a scale of 1-10?"
BAD_EXPERIENCE = "Don't be too hard on yourself. You can always start the game again. AND you can always try again tomorrow in real life as well!"
GOOD_EXPERIENCE = "Finding a work-life balance is tough. You're doing amazing, although you could use some relaxation :)"
FINAL_MESSAGE = "Thank you for playing!"

#------functions-----
def get_user_choice(prompt, valid_options):
# from CHATAI
    while True:
        choice = input(prompt).strip()
        if choice in valid_options:
            return choice
        else:
            print(f"Please choose one of: {', '.join(valid_options)}")

def show_feedback(experience, decision):
    if experience in ["6", "7", "8", "9", "10"]:
        print(GOOD_EXPERIENCE)
    else:
        print(BAD_EXPERIENCE)
    if decision == "1":
        print(CONSTANT_CHOICE_ONE)
    elif decision == "2":
        print(CONSTANT_CHOICE_TWO)
    elif decision == "3":
        print(CONSTANT_CHOICE_THREE)

def main():
    print(INTRO)
    #time.sleep(2)
    name = input (NAME_REQUEST)
    print (f"Welcome, {name}! Like all students, you have a lot going on academically! But what about your social life? Practice making work-life balance decisions with the following scenario:")


    # time.sleep(7)
    print (SCENARIO)
    decision = get_user_choice(ANSWER_REQUEST, CHOICES)
    if decision == "1":
        print (DECISION_ONE)
    elif decision == "2":
        print (DECISION_TWO)
    elif decision == "3":
        print (DECISION_THREE)

    time.sleep (7)
    experience = get_user_choice(EXPERIENCE_REQUEST, ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
    show_feedback(experience,decision)
    #sleep (5)
    #end game
    print(FINAL_MESSAGE)

if __name__ == "__main__":
    main()

input("Press Enter to exit...")