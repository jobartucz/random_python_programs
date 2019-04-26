class Roller:

    # it's easier storing some local variables
    # rather than passing them around the methods
    mSides = 0
    mPoints = 0
    mPointRolls = 0
    mTotalRolls = 0

    def roll(self, rollsleft, side, total):

        
        # print ("rollsleft: " + str(rollsleft) + " side: " + str(side))

        if (rollsleft == 0): # we've rolled all the dice
            # print (" total: " + str(total))
            self.mTotalRolls += 1 # add one to the total times we've rolled all the dice
            if (total >= self.mPoints):
                self.mPointRolls += 1 # if the points add up to more than the threshold, add one to the pointRolls
            
            return
        

        # recursively roll the dice        
        for side in range(1, self.mSides + 1):
            self.roll(rollsleft - 1, side, total + side)
        
    


    def rolldice(self, rolls, sides, points):

        # initialize the properties
        self.mSides = sides;
        self.mPoints = points;

        # start rolling
        self.roll(rolls, 0, 0);

        print (self.mPointRolls)
        print (self.mTotalRolls)

        # probability is number of rolls that were > points divided by total number of rolls
        return (float(self.mPointRolls) / float(self.mTotalRolls))

    


# You don't need to change anything below here
# execute only if run as a script
if __name__ == "__main__":
  
  numRolls = 10
  numSides = 6
  desiredPoints = 20
  
  tester = Roller()
  prob = tester.rolldice(numRolls, numSides, desiredPoints)

  print("Probability of getting at least " + str(desiredPoints) + " from " + str(numRolls) + " rolls " + " on a " + str(numSides) + "-sided die is " + str(prob))

