
something = input("what would you like to write to the file? ")

# this will overwrite the entire file!!!
f = open("demofile.txt", "w")
f.write(something + '\n')

f.close()


something = input("what would you like to append at the end of the file? ")

# this will append to the end of the file
f = open("demofile.txt", "a")
f.write(something + '\n')

f.close()

something = input("Are you ready to read the file? ")

# this will read the file
f = open("demofile.txt", "r")
for currentline in f:
    print(currentline, end='')

f.close()