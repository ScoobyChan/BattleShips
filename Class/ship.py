# Used print to help diagnose class problem
class ship():
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

        print(self.Player,"Board Reset")

    # This is used to save the player board
    def playerBoard(self):
        for i in range(0,5):
            self.A[self.num] = self.pA[self.num]        # Makes copy of list pA
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
        print(self.Player,"Board Saved")

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
