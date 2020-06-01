# This class checks the board to see if the player or computer has won
class checkIfWon():
    # This function takes in self and user as parameters
    def close(self):        # Used to end pick function
        self.gameStart = False
        
    def checkIfWon(self,user):
        # This choses between the player checker and computer checker
        if user == "P":
            # Computer checker
            # It checks computers board to see if player has won
            if "s" not in self.cA and  "s" not in self.cB and  "s" not in self.cC and  "s" not in self.cD and  "s" not in self.cE:
                print(self.Player,"has won")
                # self.gameStart = False
                self.close()
                
        else:   
            # Player checker
            if "s" not in self.pA and  "s" not in self.pB and  "s" not in self.pC and  "s" not in self.pD and  "s" not in self.pE:      # Looks to check the players grid for any ships left
                print("The Computer has won")     # This alerts the player they have won
                self.gameStart = False          # This ends one of the while loops
