import time
#intro
print("Welcome to 'Work-life balance, the simulator!!'")
time.sleep(2)
name = input("What's your name?")
print("Welcome",name,"like all students,you have a lot going on academically! But what about your social life? Practice making work-life balance decisions with the following scenario:")
time.sleep(10)
#scenario choice making
print("""

You are on you way home on a sunny afternoon. You meet one of your friends on the way!
How exiting! Will you
 1. Say Hi and continue to go home.
 or will you
 2. ask your friend to do something fun-
since the weather is so nice?

""")
time.sleep(7)
Decision = input("What do you do, answer with 1 or 2!")


while Decision not in ["1", "2", "3"]:
    print("""please choose option 1 or option 2 (or secret option 3) by choosing '1' or '2' (or '3') respectively.""")
    Decision = input("What do you do, answer with 1 or 2!")

if Decision == "1":
    print("""

    You decide to head home despite meeting your friend. You've got so much homework already,
it would be irresponsible, to not use your free time to finish it today

""")
elif Decision == "2":
    print("""

    A little time spent with friends is so much more valuable than sitting in front
of your laptop and being bored, right? You and your friend decide to go to Penny and pick up some snacks. You have a makeshift picnic on Mensawiese.

""")
elif Decision == "3":
    print("""
          You found the secret option! You and your friend decide to study together outside. You enjoy the sunny day AND still get work done. Good for you !!"

          """)
time.sleep(7)

#asking about experience 
Experience = input("How happy are you with your choice on a scale of 1-10?""")

while Experience not in ["1", "2", "3","4","5","6","7","8","9","10"]:
    print("That wasn't a valid statement and you know it!")
    Experience = input("How happy are you with your choice on a scale of 1-10?""")
if Experience in ["6","7","8","9","10"]:
    print("Awesome! Finding a work-life balance is tough. You're doing amazing :)")
    if Decision == "1":
        print("You chose to not see your friend and work. You seem to be very hardworking. Don't forget to chill.")
    elif Decision == "2":
        print("You chose to not do your work and chill with your friends. Having fun with your friends is super important! But make sure to not neclect uni work.")
    elif Decision == "3":
        print("You found the secret perfect option! You either think outside the box or you just tried to stop my programm from working. In any case, good job!")
elif Experience in ["1", "2", "3","4","5"]:
    print ("""Don't be too hard on yourself. You can always start the game again. AND you can always try again tomorrow in real life as well!""")
    if Decision == "1":
        print("You chose to not see your friend and work. You seem to be very hardworking. Don't forget to chill.")
    elif Decision == "2":
        print(" You chose to not do your work and chill with your friends. Having fun with your friends is super important! But make sure to not neclect uni work.")
    elif Decision == "3":
        print("You found the secret perfect option! You either think outside the box or you just tried to stop my programm from working. In any case, good job!")



