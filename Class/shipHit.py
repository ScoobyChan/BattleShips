import random
class shipHit():
    def shipHit(self, p):
        v = 5
        h = 5
        s = ""
        notAccepted = True
        
        if p == "P":
            # Checks to make sure numbers are valid
            while notAccepted:
                while h > 4:
                    while v > 4:
                        v = input("Enter down number between 0 - 4: ")      # Takes input between 0 and 4
                        try:        # This checks value is a number
                            v = int(v)
                            if v > 4:
                                print("Number too high\n")
                            else:
                                print("Number is fine please enter next one\n")
                        except ValueError:      # If v cant be converted to integer than spit out error
                            print(v, "Is not a number")
                            v = 5
                            
                    h = input("Enter across number between 0 - 4: ")
                    try:
                        h = int(h)
                        if h > 4:
                            print("Number too high\n")
                        else:
                            print("Number is fine")
                    except ValueError:
                        print(h, "Is not a number")
                        h = 5
                        
                # makes h a string for joining
                integer = str(h)
                
                self.pCoord.append(self.vert[v])
                self.pCoord.append(integer)

                joined = s.join(self.pCoord)
                # used to make sure the coords have been joined correctly
                # print(joined)
                
                if joined in self.pCoords:
                    print("The coordanints have been accepted for the player")
                    notAccepted = False
                else:
                    print("the coordanints have been used already please try again\n")
                    v = 5
                    h = 5
                    self.pCoord = []
#============================================================================================================
        else:
            while notAccepted:
                v = random.randint(0,4)
                h = random.randint(0,4)

                # makes h a string for joining
                integer = str(h)
                
                self.cCoord.append(self.vert[v])
                self.cCoord.append(integer)

                joined = s.join(self.cCoord)
                # used to make sure the coords have been joined correctly
                # print(joined)
                
                if joined in self.pCoords:
                    print("The coordanints have been accepted for the computer")
                    notAccepted = False
                else:
                    # Used to make sure coord checker works but doesnt need to print for AI
                    # print("the coordanints have been used already please try again\n")
                    v = 5
                    h = 5
                    self.cCoord = []
        if p == "P":
            # Selects row
            if self.vert[v] == "A":
                co = self.cA[h]
            elif self.vert[v] == "B":
                co = self.cB[h]
            elif self.vert[v] == "C":
                co = self.cC[h]
            elif self.vert[v] == "D":
                co = self.cD[h]
            elif self.vert[v] == "E":   
                co = self.cE[h]
#============================================================================================================
        else:
            # Selects row
            if self.vert[v] == "A":
                co = self.pA[h]
            elif self.vert[v] == "B":
                co = self.pB[h]
            elif self.vert[v] == "C":
                co = self.pC[h]
            elif self.vert[v] == "D":
                co = self.pD[h]
            elif self.vert[v] == "E":   
                co = self.pE[h]
        # used to make sure right list is selected
        # print(co)

#============================================================================================================
        # used to replace hit or missed places
        if co == "s":
            print("Hit")
            self.replace(self.vert[v], h, "h", p)
        else:
            print("Miss")
            self.replace(self.vert[v], h, "m", p)
        
#============================================================================================================
        
        # used to remove used coords
        if p == "P":
            if joined in self.pCoords:
                self.pCoords.remove(joined)
                self.pCoord = []
        else:
            if joined in self.cCoords:                
                self.cCoords.remove(joined)
                self.cCoord = []
                
        # print(self.coords[1:9]) # used to check if coord is removed

#===========================================================================
