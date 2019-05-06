# I'm using a graphical button instead of a real one
from tkinter import *

# keep track of whether the game is over
game_over = False

def pressed():
    
    # get the value of "game_over" from the global program - don't make a new one!
    global game_over
    
    if (game_over == False):
        print ("clicked!")
        game_over = True
    else:
        print ("too slow!")
        game_over = True

# this code just assigns the function about to the button
b = Button(text="click me", command=pressed)
b.pack()

mainloop()
