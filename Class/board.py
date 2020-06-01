class board():
    # Used for replace the list letters with h or m
    vert = ["A","B","C","D","E"]

    # These are used for shipPlacement is valid, for usable coords
    pCoord = []
    cCoord = []
    
    # Lists for Player
    #============================
    pA = ["o","o","o","o","o"]
    pB = ["o","o","o","o","o"]
    pC = ["o","o","o","o","o"]
    pD = ["o","o","o","o","o"]
    pE = ["o","o","o","o","o"]
    #============================

    # Lists for computer
    #============================
    cA = ["o","o","o","o","o"]
    cB = ["o","o","o","o","o"]
    cC = ["o","o","o","o","o"]
    cD = ["o","o","o","o","o"]
    cE = ["o","o","o","o","o"]
    #============================

    #  Useable Coords
    pCoords = ["A0","A1","A2","A3","A4","B0","B1","B2","B3","B4","C0","C1","C2","C3","C4","D0","D1","D2","D3","D4","E0","E1","E2","E3","E4"]
    cCoords = ["A0","A1","A2","A3","A4","B0","B1","B2","B3","B4","C0","C1","C2","C3","C4","D0","D1","D2","D3","D4","E0","E1","E2","E3","E4"]

    # Used in place ship
    Coord = ["A","B","C","D","E"]


    # This Displays the board
    def displayBoard(self, p):      # Takes in the parameters of self and p
        if p =="P":                 # Used to display Players board
            print("Players Board")
            print(*self.pA, sep=' ')        # This displays the list self.pA and separates the indexs with a space
            print(*self.pB, sep=' ')
            print(*self.pC, sep=' ')
            print(*self.pD, sep=' ')
            print(*self.pE, sep=' ')
        else:                       # Used to display Computers board
            print("Computer Board")
            print(*self.cA, sep=' ')
            print(*self.cB, sep=' ')
            print(*self.cC, sep=' ')
            print(*self.cD, sep=' ')
            print(*self.cE, sep=' ')

