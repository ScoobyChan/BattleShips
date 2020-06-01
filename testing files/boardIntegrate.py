class Board:
    num = 0
    
    
    A = ["o","o","o","o","o"]
    B = ["o","o","o","o","o"]
    C = ["o","o","o","o","o"]
    D = ["o","o","o","o","o"]
    E = ["o","o","o","o","o"]


    def displayBoard(self):
        print(*self.A, sep=' ')
        print(*self.B, sep=' ')
        print(*self.C, sep=' ')
        print(*self.D, sep=' ')
        print(*self.E, sep=' ')

board = Board()
board.displayBoard()
