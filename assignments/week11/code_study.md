### Suspended sentence code reading excersise

#### 1. Where did you find the code and why did you choose it? (Provide the link)

I used: https://github.com/CTPUG/suspended_sentence/tree/master

It is an old entry to Pyweek. I know we weren't supposed to use code that is too old BUT it was the only game that I found that was close to what I want to do for my final assigment.  
Also, I tried the game and it works well still.

#### 2. What does the program do? What's the general structure of the program?

It's a point and click game called "suspended sentence" where one is a prisoner in a space station being the only survivor of a disaster and having to fix the ship. 
In the game, one has to click on items to pick them up, and combine them if other items or the surrounding area. For example, you can pick up a fish-bowl and combine it with duct tape to get a makeshift astronaut helmet.
Structure of program: Firstly, there is  a start screen with settings. Secondly there is a map letting you navigate through the different rooms of the spaceship, which are drawn pictures. 
the items are overlayed on top of the sceneries and there is an inventory that stays the same throughout the different rooms. There is also a progress saving mechanism, however I have not tried it. It features many different codes, which I had not the change to look at all of, to be honest, but I made sure to get a general overview.
 The code itself is structured into many different folders. 
---

#### 3. Function analysis: pick one function and analyze it in detail:
It's a function inside a class called jimpanel. 

    From: gamelib/scenes/bridge.py
    
    def interact_with_machete(self, item): 
    ai_status = self.state.get_jim_state()
    if ai_status == 'online':
        return self.interact_default(item) 
    elif self.scene.get_data('ai panel') == 'closed': 
        self.scene.set_data('ai panel', 'open')
        self.set_interact()
        return Result(_("Using the machete, you lever the panel off."))
    elif self.scene.get_data('ai panel') == 'open':
        self.scene.set_data('ai panel', 'broken')
        self.state.break_ai()
        self.set_interact()
        return Result(_("You smash various delicate components with the machete.")) 
    
The code defines what happens when the player uses the item "machete" on the "Ai panel (or jim panel)" in the game. If the Ai panel is already open, you destroy the insides with the machete, if not, you open the Ai panel.
Before that part, its defined what happens if you touch the panel and after, there is a function naming a general happenstance if the panel is touched with any other object. 
I've learned more about the dot notation (e.g. self.state.get_jim_state()), that it 'reads it like an adress from left to right to find a specific function.'
Later in the code, the on-screen-pictures are defined with coordinates of where they are, to the change is visual as well. Depending on whether the panel is open or closed, it will change the png.

    class JimPanel(Thing):
        "The panel to JIM's internals'"
    
        NAME = "jim_panel"
    
        INTERACTS = {
                'closed': InteractNoImage(506, 430, 137, 47),
                'open': InteractImage(500, 427, 'jim_panel_open.png'),
                'broken': InteractImage(488, 412, 'jim_panel_destroyed.png'),
                }
    
        INITIAL = 'closed'



##### What does this function do?
-  It defines the consequences of an action in the game. You can open the 'Ai panel' with a machete, but if it's already open and you click on it again, you break it.
- 
- ##### How does it work (step by step)?
      -   From: gamelib/scenes/bridge.py
        
          def interact_with_machete(self, item): #a function is defined ("interact_with_machete), and parts of it are "self" and the item used (item)
          ai_status = self.state.get_jim_state() #we call on the global game state to see whether the AI in the game is online or offline
          if ai_status == 'online':#if the AI string is exactly equal to the string "online", the default reaction is triggered (an electric shock in the game)
              return self.interact_default(item) #
          elif self.scene.get_data('ai panel') == 'closed': #if the Ai is NOT online, and you interact with it, the panel will be opened
              self.scene.set_data('ai panel', 'open') #changes ai panel status from closed to open 
              self.set_interact() #code looks up the changed ai panel status. 
              return Result(_("Using the machete, you lever the panel off.")) # description is printed of what is happening in the game
          elif self.scene.get_data('ai panel') == 'open': #if the Ai panel is already open and you use the machete on it again, it's status is updated from open to broken
              self.scene.set_data('ai panel', 'broken')
              self.state.break_ai() 
              self.set_interact()#info of broken panel is updated  
              return Result(_("You smash various delicate components with the machete.")) #result with description  

---

4. #### Takeaways: are there any things you can learn from the code? (How to structure your code, a clean solution for some function you might also need...)
   1. I didn't understand the "self.[...]" logic as much before, but thanks to this code i've gotten more comfortable with it
   2. Docs: There is a 'artists how to' that specifies the canvas and item size, which I found very helpful, as I can use a similar size for my project. Additionally there is a walkthrough file, explaining what one must do to complete the game. I think it will be very helful for me to make a similar file for planning my project.
   3. I like how they strucutred their code in different folders, so its easier to get specific info, when looking for it. 
   4. I also better understand their method of defining functions and using methods inside classes, I think this logic will be valuable for my final project


5. #### What parts of the code were confusing or difficult at the beginning to understand?
    It took some time to navigate through the different folders, as well as understanding how the code changes the pictures and finding the code snippet that does. 

6. #### Were you able to understand what it is doing after your own research?
    I definitely know more than I did before, but I didn't have time to go through the whole code yet.

7. #### Extra notes
The makers of this game also made a library for point and click adventure games called pyntclick, which for my project I'll look at next
