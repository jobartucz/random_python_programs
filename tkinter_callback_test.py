# I'm using a graphical button instead of a real one
from tkinter import *
from time import sleep
from random import uniform

# keep track of the score
player1_wins = 0
player2_wins = 0

def pressed():
    
    # get the values of "can_click" and "wins" from the global program - don't make a new one!
    global can_click
    global player1_wins
    global player2_wins
    
    if (can_click == True):
        print ("player 1 wins!")
        player1_wins += 1
        can_click = False
    else:
        print ("too slow!")


# don't let someone click when they're not supposed to
can_click = False
print("Are you ready?") # LED goes on (or make a three-LED countdown)
print("3....")
sleep(uniform(1,3))
print("2....")
sleep(uniform(1,3))
print("1....")
sleep(uniform(1,3))
print("Go!")            # LED turns off
can_click = True
        
        
# this code just assigns the function about to the button
b = Button(text="click me", command=pressed)
b.pack()

mainloop()
