from tkinter import *
master = Tk()

print ("I will paint everything with a 0 in light yellow, 1 in dark green and missing info will be light pink")

# we need to get the width and height to know how to print it out
width = int(input("how many squares WIDE is your picture? "))
if (width <= 0):
    raise ValueError('invald width!')

height = int(input("how many squares TALL is your picture? "))
if (width <= 0):
    raise ValueError('invald height!')

# this is where we get the user's 0's and 1's
string_input = input("please enter your code, separated by commas: ")
binary_input = string_input.split(",")

if (height * width != len(binary_input)):
    print ("uhoh! The length times the width does not equal the number of characters your entered! I'll do my best :/")

# check to make sure the data is valid
for i in range (len(binary_input)):
    if (str(binary_input[i]).strip() != '0' and str(binary_input[i]).strip() != '1'):
        print ("There is an error in your data, I'm setting this value to '1'")
        binary_input[i] = '1'
        
# first, print out the matrix as a test to check it
for i in range (len(binary_input)):
    # print a newline at the end of every line
    if (i > 0 and i % width == 0):
        print("")
    print (str(binary_input[i]) + " ", end='')

# here is where we make the graphic
# make the window about 600 pixels high or wide at the maximum
multiplier = int(600 / max([width, height]))
canvas_width = width * multiplier
canvas_height = height * multiplier

# create a window with a canvas
w = Canvas(master, 
           width=canvas_width,
           height=canvas_height)
w.pack()

for i in range (height):
    for j in range (width):
        cur_num = i * width + j

        # draw the squares
        if (cur_num >= len(binary_input)): #red
            w.create_rectangle(j * multiplier, i * multiplier, (j + 1) * multiplier, (i + 1) * multiplier, fill="#ffaaaa")
        elif (int(binary_input[cur_num]) == 0): # yellow 
            w.create_rectangle(j * multiplier, i * multiplier, (j + 1) * multiplier, (i + 1) * multiplier, fill="#ffff88")
        else: #green
            w.create_rectangle(j * multiplier, i * multiplier, (j + 1) * multiplier, (i + 1) * multiplier, fill="#476042")


mainloop()

