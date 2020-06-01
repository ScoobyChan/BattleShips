from Class import ship, shipHit, board, checkIfWon, player, placeship, blank, replace       # Imports the classes from class folder

class Init(ship.ship, shipHit.shipHit, board.board, checkIfWon.checkIfWon, player.player, placeship.placeship, blank.blank, replace.replace):
    pass        # The pass function allows the class to have nothing in it and come up with no errors
                # This line passes through all classes in the class folder which allows this class and the classes in the folder to access all the information


