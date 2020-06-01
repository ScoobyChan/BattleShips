# Using board class for testing purposes
# Take out when merging all

class board():
    vert = ["A","B","C","D","E"]
    pCoord = []
    cCoord = []
    
    pA = ["o","o","o","o","o"]
    pB = ["o","o","o","o","o"]
    pC = ["o","o","o","o","o"]
    pD = ["o","o","o","o","o"]
    pE = ["o","o","o","o","o"]

    cA = ["o","o","o","o","o"]
    cB = ["o","o","o","o","o"]
    cC = ["o","o","o","o","o"]
    cD = ["o","o","o","o","o"]
    cE = ["o","o","o","o","o"]

    pCoords = ["A0","A1","A2","A3","A4","B0","B1","B2","B3","B4",]
    cCoords = ["A0","A1","A2","A3","A4","B0","B1","B2","B3","B4",]


    def displayBoard(self, p):
        if p =="P":
            print("Player Board")
            print(*self.pA, sep=' ')
            print(*self.pB, sep=' ')
            print(*self.pC, sep=' ')
            print(*self.pD, sep=' ')
            print(*self.pE, sep=' ')
        else:
            print("Computer Board")
            print(*self.cA, sep=' ')
            print(*self.cB, sep=' ')
            print(*self.cC, sep=' ')
            print(*self.cD, sep=' ')
            print(*self.cE, sep=' ')

    # need to add to board for replacer
    def replace(self, v, h, l, q):
        # used to make sure values for function matches
        # replace(self.vert[v], h, l)
        # Used to check values
        # print(v)
        # print(h)
        if q =="C":
            if v == "A":
                self.pA[h] = l
            elif v == "B":
                self.pB[h] = l
            elif v == "C":
                self.pC[h] = l
            elif v == "D":
                self.pD[h] = l
            elif v == "E":
                self.pE[h] = l
        else:
            if v == "A":
                self.cA[h] = l
            elif v == "B":
                self.cB[h] = l
            elif v == "C":
                self.cC[h] = l
            elif v == "D":
                self.cD[h] = l
            elif v == "E":
                self.cE[h] = l


#===========================================================================
        
# Ship class
# from board import board
class ship(board):
    ship = "s"
    A = ["","","","",""]
    B = ["","","","",""]
    C = ["","","","",""]
    D = ["","","","",""]
    E = ["","","","",""]
    num = 0

    # This function is used to reset the saved player board
    def resetPlayerBoard(self):
        for i in range(0,5):
            self.A[self.num] = "o"
            # Used to check that saving player  board worked
            # print(self.pA[self.num])
            self.num = self.num + 1
        self.num = 0
        
        for i in range(0,5):
            self.B[self.num] = "o"
            self.num = self.num + 1
        self.num = 0

        for i in range(0,5):
            self.C[self.num] = "o"
            self.num = self.num + 1
        self.num = 0

        for i in range(0,5):
            self.D[self.num] = "o"
            self.um = self.num + 1
        self.num = 0

        for i in range(0,5):
            self.E[self.num] = "o"
            self.num = self.num + 1
        self.num = 0

        print("Player Board Reset")

    # This is used to save the player board
    def playerBoard(self):
        for i in range(0,5):
            self.A[self.num] = self.pA[self.num]
            # print(self.pA[self.num])
            self.num = self.num + 1
        self.num = 0
    
        for i in range(0,5):
            self.B[self.num] = self.pB[self.num]
            self.num = self.num + 1
        self.num = 0

        for i in range(0,5):
            self.C[self.num] = self.pC[self.num]
            self.num = self.num + 1
        self.num = 0

        for i in range(0,5):
            self.D[self.num] = self.pD[self.num]
            self.num = self.num + 1
        self.num = 0

        for i in range(0,5):
            self.E[self.num] = self.pE[self.num]
            self.num = self.num + 1
        self.num = 0

        # used to save players board
        print("Player Board Saved")

    # Used to display saved player board
    def displayPlayerShips(self):
        print(*self.A, sep=' ')
        print(*self.B, sep=' ')
        print(*self.C, sep=' ')
        print(*self.D, sep=' ')
        print(*self.E, sep=' ')

    # Used to test that the rows show for the players board
    def test(self):
        print(*self.A, sep=' ')
        


#===========================================================================
        
# Shiphit class
# from board import board
import random
class shipHit(board):
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
                        v = int(input("Enter vertical number between 0,4: "))
                        if v > 4:
                            print("Number too high\n")
                        else:
                            print("Number is fine please enter next one\n")
                        
                    h = int(input("Enter horizontal number between 0,4: "))
                    if h > 4:
                        print("Number too high\n")
                    else:
                        print("Number is fine")
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
                co = self.pA[h]
            elif self.vert[v] == "B":
                co = self.pB[h]
            elif self.vert[v] == "C":
                co = self.pC[h]
            elif self.vert[v] == "D":
                co = self.pD[h]
            elif self.vert[v] == "E":   
                co = self.pE[h]
#============================================================================================================
        else:
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

#============================================================================================================


users = ship()
player = shipHit()
comp = shipHit()

# Loop shiphit()
for i in range(1,6):
    comp.shipHit("C")
    player.displayBoard("P")
    
    player.shipHit("P")
    comp.displayBoard("C")

#users.playerBoard()
#users.displayPlayerShips()





