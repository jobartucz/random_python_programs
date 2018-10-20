
to_reverse = input("Enter string to reverse: ")

# for the advanced user, look up extended slice
print (to_reverse[::-1])

#create an empty string
reversed_string = ''
# add each character to the beginning of the existing string
for char in to_reverse:
    reversed_string = char + reversed_string

print (reversed_string)