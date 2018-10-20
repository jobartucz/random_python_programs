
mynum = int(input("Enter any integer > 1: "))

# for mynum in range(2, 9999999999999999):
    
print ("trying: " + str(mynum))

while mynum != 1:
    
        if (mynum % 2 == 0):
            mynum = mynum // 2
        else:
            mynum = mynum * 3 + 1
        
        print ("success: " + str(mynum))
    
