class blank():
    bA = ["o","o","o","o","o"]
    bB = ["o","o","o","o","o"]
    bC = ["o","o","o","o","o"]
    bD = ["o","o","o","o","o"]
    bE = ["o","o","o","o","o"]
    def blank(self):
        print("Players placement board")
        print("  | 0 1 2 3 4")
        print("--+-----------")
        print("0 |", *self.bA, sep=' ')
        print("1 |", *self.bB, sep=' ')
        print("2 |", *self.bC, sep=' ')
        print("3 |", *self.bD, sep=' ')
        print("4 |", *self.bE, sep=' ')

# Used for testing
# t = blank()
# t.blank()
