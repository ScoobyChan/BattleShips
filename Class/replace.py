class replace():
    def replace(self, v, h, l, q):
        # used to make sure values for function matches
        # replace(self.vert[v], h, l, q)
        # Used to check values
        # print(v)
        # print(h)
        if q =="P":                 # Used for player replacer
            if v == "A":
                self.cA[h] = l      # cA[h](computers list which has c at the start)
                self.bA[h] = l
            elif v == "B":
                self.cB[h] = l
                self.bB[h] = l
            elif v == "C":
                self.cC[h] = l
                self.bC[h] = l
            elif v == "D":
                self.cD[h] = l
                self.bD[h] = l
            elif v == "E":
                self.cE[h] = l
                self.bE[h] = l
        else:                       # Used for computer replacer
            if v == "A":            # if v is equal to A then run command
                self.pA[h] = l      # Sets the pA[h](players list which has p at the start) value to the value of l // h is the value is the index number
                
            elif v == "B":
                self.pB[h] = l
                    
            elif v == "C":
                self.pC[h] = l
                
            elif v == "D":
                self.pD[h] = l
                
            elif v == "E":
                self.pE[h] = l
