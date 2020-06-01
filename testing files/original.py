from Game import gameInit

# game = gameInit()
# game.test() -- Used for testing

player = gameInit()
comp = gameInit()

player.player()

# Add ship placement
player.playerBoard()

# Loop shiphit()

comp.shipHit("C")
player.displayBoard("P")
    
    	
player.shipHit("P")
comp.displayBoard("C")

player.displayPlayerShips()


