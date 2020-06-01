from Class import checkIfWon, board, group
class test(checkIfWon.checkIfWon, board.board, group.group):
    pass


c = test()
c.checkIfWon("C")
c.checkIfWon("P")

print(c.gameStart)
