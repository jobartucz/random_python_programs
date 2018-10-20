# get the input from the user
input_string = input("Please enter a list of numbers, separated only by spaces: ")

# make a list of the numbers by splitting it up on every space
input_string_list = input_string.split(" ")
print(input_string_list)

# the problem is that they still are not integers
# so we'll make a new list by going through the numbers one at a time and converting them
integer_list = [] # creates an empty list
for string_num in input_string_list: # go through input_string_list one at a time
    integer_list.append(int(string_num)) # convert the number to an integer and add it to integer_list
    
print(integer_list)

# I will grade this out of 10:
# up to 7 points for effort (still have to submit something)
# 8 points: print out all the numbers that are multiples of 7, or print "no multiples of 7" if there are none. You can use the "modulus" operator
# 9 points: print out the biggest even number and the smallest odd number (you can assume all numbers are between 1-1000)
# 10 points: sort the list (assume the numbers are integers between -1000000 and +1000000). I will test with MANY numbers

#### write your code below this line ###


