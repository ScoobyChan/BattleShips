import random
# from board import board                   Used for testing
class placeship():
    num = 0
    Position = True

    def placeship(self, user):
        # Set values to greater than 4 to make loops true
        #=============
        s1 = 5
        s2 = 5
        s3 = 5
        s4 = 5
        #=============

        if user == "P":         # This is the players ship placer
            while self.Position:
                hv = input("Enter h or v for ship placement horizontal or vertical: ")          # This is the input for HV selector
                hv = hv.title()         # Sets hv to capatial

                if hv == "H":
                    print("You have picked the across method")
                    print("Please have the across different and the down same")
                else:
                    print("You have picked the down method")
                    print("Please have the down different and the across same")
                # These loops makes sure the inputs are valid answers for the integers
                while s1 > 4:
                    s1 = input("Enter A number between 0 and 4 for starting across: ")
                    try:        # This checks s1 to see if it is a integer
                        s1 = int(s1)
                    except ValueError:      # If not integer it will give error message to user
                        print(s1, "Does not equal a number")
                        s1 = 5
                while s2 > 4:
                    s2 = input("Enter A number between 0 and 4 for starting down: ")
                    try:
                        s2 = int(s2)
                    except ValueError:
                        print(s2, "Does not equal a number")
                        s2 = 5    
                while s3 > 4:
                    s3 = input("Enter A number between 0 and 4 for ending  across: ")
                    try:
                        s3 = int(s3)
                    except ValueError:
                        print(s3, "Does not equal a number")
                        s3 = 5    
                while s4 > 4:
                    s4 = input("Enter A number between 0 and 4 for ending down: ")
                    try:
                        s4 = int(s4)
                    except ValueError:
                        print(s4, "Does not equal a number")
                        s4 = 5     
                
                if hv == "H":               # if hv equal to hv is equal to H then run program // Horizontal selector for player
                    leng = s3 - s1          # validates length
                    # print(leng) used for trouble shooting
                    if leng == 2:
                        self.Position = False
                        # print(self.Coord[s2]) used for trouble shooting

                        if self.Coord[s2] == "A":       # If list equal to A the run program
                            if "s" not in self.pA:      # This line checks to see if the list indexs are valid
                                for i in range(3):      # Loops 3 times
                                    self.pA[s1] = "s"   # sets List A for Player to s
                                    s1 = s1 + 1         # updates s1 by 1
                            else:
                                print("Spot in use")    # This prints out message to tell player the spot is taken
                                self.Position = True    # Sets position to True
                                
                        elif self.Coord[s2] == "B":
                            if "s" not in self.pB:
                                for i in range(3):
                                    self.pB[s1] = "s"
                                    s1 = s1 + 1
                            else:
                                print("Spot in use")
                                self.Position = True
                                
                        elif self.Coord[s2] == "C":
                            if "s" not in self.pC:
                                for i in range(3):
                                    self.pC[s1] = "s"
                                    s1 = s1 + 1
                            else:
                                print("Spot in use")
                                self.Position = True
                                
                        elif self.Coord[s2] == "D":
                            if "s" not in self.pD:
                                for i in range(3):
                                    self.pD[s1] = "s"
                                    s1 = s1 + 1
                            else:
                                print("Spot in use")
                                self.Position = True
                                
                        elif self.Coord[s2] == "E":
                            if "s" not in self.pE:
                                for i in range(3):
                                    self.pE[s1] = "s"
                                    s1 = s1 + 1
                            else:
                                print("Spot in use")
                                self.Position = True
                                
                                    
                else:
                    # This section is used for vertical ship placement
                    leng = s4 - s2
                    if leng == 2:
                        self.Position = False
                        if self.Coord[s2] == "A":           # if equal to A the run code
                            if "s" not in self.pC[s1] and  "s" not in self.pB[s1] and "s" not in self.pA[s1]:       # This line checks to see if the list indexs are valid
                                # Replaces the vertical position
                                #==================
                                self.pA[s1] = "s"
                                self.pB[s1] = "s"
                                self.pC[s1] = "s"
                                #==================
                            else:
                                print("Spot in use")
                                self.Position = True
                                
                        elif self.Coord[s2] == "B":
                            if "s" not in self.pC[s1] and  "s" not in self.pD[s1] and "s" not in self.pB[s1]:
                                self.pD[s1] = "s"
                                self.pB[s1] = "s"
                                self.pC[s1] = "s"
                            else:
                                print("Spot in use")
                                self.Position = True
                                
                        elif self.Coord[s2] == "C":
                            if "s" not in self.pC[s1] and  "s" not in self.pD[s1] and "s" not in self.pE[s1]:
                                self.pE[s1] = "s"
                                self.pD[s1] = "s"
                                self.pC[s1] = "s"
                            else:
                                print("Spot in use")
                                self.Position = True
                                
                        else:
                            self.Position = True
                        
                if self.Position == True:
                    print("Invalid placement try again")
                    # set all to 5 to make while loops vaild again
                    s1 = 5      
                    s2 = 5
                    s3 = 5
                    s4 = 5

            # set all to 5 to make while loops vaild again      
            s1 = 5
            s2 = 5
            s3 = 5
            s4 = 5
            self.Position = True        # set position to True
#======================================================            
        else:
            # The Ai Selector for ship placement
            hv = ["H","V"]              # List for H, V
            num = random.randint(0,1)   # random number 0 - 1 for H, V selector
            
            direction = hv[num]         # sets direction to the list index
            
            while self.Position: 
                #print("Check") Used for debugging
                #print(direction)
                if direction == "H":        # Used to select diection for AI
                    # Selects random numbers for vertical direction
                    #============================
                    s1 = random.randint(0,4)
                    s2 = random.randint(0,4)
                    s3 = random.randint(0,4)
                    #============================

                    leng = s3 - s1
                    # print(leng) used for trouble shooting
                    if leng == 2:
                        self.Position = False            # This is required so the to end the selector loop
                        # print(self.Coord[s2]) used for trouble shooting

                        if self.Coord[s2] == "A":           # If list equal to A the run program
                            if "s" not in self.cA:          # Checks if valid use
                                for i in range(3):          # loops 3 times
                                    self.cA[s1] = "s"       # sets list to s
                                    s1 = s1 + 1             # adds one to s1
                            else:
                                # print("Spot in use")           
                                self.Position = True            # This is called so that the player has to redo because of invalid move
                                 
                        elif self.Coord[s2] == "B":         # Explained already
                            if "s" not in self.cB:
                                for i in range(3):
                                    self.cB[s1] = "s"
                                    s1 = s1 + 1
                            else:
                                # print("Spot in use")
                                self.Position = True
                                    
                        elif self.Coord[s2] == "C":
                            if "s" not in self.cC:
                                for i in range(3):
                                    self.cC[s1] = "s"
                                    s1 = s1 + 1
                            else:
                                # print("Spot in use")
                                self.Position = True
                                    
                        elif self.Coord[s2] == "D":
                            if "s" not in self.cD:
                                for i in range(3):
                                    self.cD[s1] = "s"
                                    s1 = s1 + 1
                            else:
                                # print("Spot in use")
                                self.Position = True
                                    
                        elif self.Coord[s2] == "E":
                            if "s" not in self.cE:
                                for i in range(3):
                                    self.cE[s1] = "s"
                                    s1 = s1 + 1
                            else:
                                print("Spot in use")
                                self.Position = True
                                    
                     # Was an error on line 186/189 list index out of range                   
                else:
                    # Chooses a number for Vertical random numbers 
                    #==================================
                    s1 = random.randint(0,4) 
                    s2 = random.randint(0,3)
                    s4 = random.randint(0,4)
                    #==================================


                    leng = s4 - s2              # Makes sure the length valid
                    if leng == 2:               # Checks to make sure length is equal to the number where needed
                        self.Position = False
                        if self.Coord[s2] == "A":
                            if "s" not in self.cC[s1] and  "s" not in self.cB[s1] and "s" not in self.cA[s1]:           # Used to make sure a ship hasnt been placed on those coordanints
                                # this is used to replace coordanints downwards
                                #==================
                                self.cA[s1] = "s"   
                                self.cB[s1] = "s"
                                self.cC[s1] = "s"
                                #==================
                            else:
                                # print("Spot in use")          Used to make sure the spot valid works
                                self.Position = True
                        
                                   
                        elif self.Coord[s2] == "B":
                            if "s" not in self.cC[s1] and  "s" not in self.cD[s1] and "s" not in self.cB[s1]:
                                self.cD[s1] = "s"
                                self.cB[s1] = "s"
                                self.cC[s1] = "s"
                            else:
                                # print("Spot in use")        
                                self.Position = True
                                    
                        elif self.Coord[s2] == "C":
                            if "s" not in self.cC[s1] and  "s" not in self.cD[s1] and "s" not in self.cE[s1]:
                                self.cE[s1] = "s"
                                self.cD[s1] = "s"
                                self.cC[s1] = "s"
                            else:
                                # print("Spot in use")
                                self.Position = True
                                    
                        else:
                            self.Position = True
                            
                    
            self.Position = True            # This is required so the position can be called again next time but it has to be outside the while loop otherwise the loop will be called again

# This was used for testing
#================================
# p = placeship()
# p.placeship("C")
# p.displayBoard("C")
# p.placeship("C")
# p.displayBoard("C")
#================================
