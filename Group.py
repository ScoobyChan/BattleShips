import time
from Game import Init
class Group(Init):
    # Variables required for the While loops
    start = True
    gameStart =True
    reset = True
    
    def start(self):            # The starting Function
        while self.reset:
            # This is used to set everything back to True for the reset
            self.start = True           
            self.gameStart = True
            #================================
            
            player = Init()      # creates the player 
            comp = Init()        # creates the computer

            # comp.displayBoard("C")    This was used for testing the comp place feature
            player.player()         # This accesses the player function
            
            #This prints the instructions for the game
            print("Welcome")
            print("Instructions\n")
            print("You will be asked for four numbers between 0 and 4\n")
            print("and you will be asked for h or v\n")
            print("These taskes will happen twice to place 2 ships")
            print("You will be playing against the AI")
            print("First one to take out all ships will win\n")
            print("Enjoy")

            time.sleep(3)
            # Comment out after testing
            # comp.placeship("C")       This was used to test the place ship function for the computer when it was bugged
            # comp.displayBoard("C")    This was used to test the display board function for the computer when it was bugged 

            # self.reset = False        This was used for testing
            while self.start:       # Start while loop
                # This section is for placing the ships
                print("Please select you ship placing")
                player.placeship("P")
                player.displayBoard("P")
                player.placeship("P")
                player.displayBoard("P")
                #================================

                player.playerBoard()        # This accesses the function playerBoard to save the players board
                
                i = input("Would like to see where you placed your ship? ")         # This input askes if the user wants to see its 
                i = i.title()       # this capitalises the the words

                if i == "Yes" or  i == "Y":             # takes the input of i
                    player.displayPlayerShips()         # this displayes the players ship
                
                time.sleep(0.5)
                print("The AI is choosing")             # Displays a message that the AI is choosing
                # AI Chooses twice
                comp.placeship("C")                     
                comp.placeship("C")
                #==========================
                print("Game is starting")           # Notifies the player that the game has begun
                time.sleep(1)           
                player.displayBoard("P")            # displays the players board
                # comp.displayBoard("C")              # Used for testing purposes
                
                while self.gameStart:               # gamestart loop
                    comp.blank()
                    player.shipHit("P")           # access place ship function 
                    comp.blank()
                    comp.displayBoard

                    comp.checkIfWon("C")        # the checking function for computer
                    player.checkIfWon("P")          # The checking function for the player
                    if self.gameStart == True:      # This checks to see if the player has won or not
                        print("Where the computer has gone incomparison to your pieces")
                        comp.shipHit("C")
                        player.displayBoard("P")
                        
                        comp.checkIfWon("C")        # the checking function for computer
                        player.checkIfWon("P")          # The checking function for the player
                        
                u = input("Would you like to play again? ")     # Asks if the user wants to play again
                u = u.title()                   # Capitalises the word

                if u == "Y" or u == "Yes":      # takes the input of u
                    self.start = False          # Sets the the start loop to 
                    print("Reseting game")      # Alerts the player that the game is reseting
                    time.sleep(1)
                else:
                    self.start = False          # Sets the start loop to False
                    self.reset = False          # Sets the reset loop to False
                    print("Thank you for playing",self.player)          # Thanks the player
                    time.sleep(1)
