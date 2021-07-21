import random #For randomized choice
import timeit #For timer 
import math #For rounding to nearest number 

#Records time of execution
start = timeit.default_timer() 

#Tracks total amount of rounds played throughout duration of program
totalRounds = 0 

#Loops until the user refuses to play again
while True: 

    #Both score trackers stay within the loop to track how many wins in a Bo3 there are
    playerWins = 0 
    computerWins = 0

    #Continues the Bo3 until either the player wins or computer wins by getting to 2 first 
    while(playerWins < 2 and computerWins < 2): 
        possibleMoves = ["R", "P", "S"]
        computer = random.choice(possibleMoves) #Computer randomly selects an option from possibleMoves

        #True until correct input is given
        while True: 
            print("SELECT ACTION BELOW:")
            player = input("(R) ROCK | (P) PAPER | (S) SCISSORS: ")
            player = player.upper() #Capitalize user input
            print("")
            if(player not in possibleMoves): #Test if input is within database 
                print("INVALID INPUT: SELECT R, P, OR S")
                print("")
            else:
                break #Exit loop

        print("YOUR CHOICE: " + player)
        print("THE COMPUTER'S CHOICE: " + computer)

        #Determines a winner through conditional statements
        if(player == computer): 
            print("DRAW")
        elif(player == "R"): 
            if(computer == "S"): 
                print("ROCK > SCISSORS. YOU WIN.")
                playerWins = playerWins + 1
            else: 
                print("PAPER > ROCK. THE COMPUTER WINS.")
                computerWins = computerWins + 1
        elif(player == "P"): 
            if(computer == "R"): 
                print("PAPER > ROCK. YOU WIN.")
                playerWins = playerWins + 1
            else: 
                print("SCISSORS > PAPER. THE COMPUTER WINS.")
                computerWins = computerWins + 1
        elif(player == "S"): 
            if(computer == "P"): 
                print("SCISSORS > PAPER. YOU WIN.")
                playerWins = playerWins + 1
            else: 
                print("ROCK > SCISSORS. THE COMPUTER WINS.")
                computerWins = computerWins + 1
        
        #Increments by 1 after every completed round
        totalRounds = totalRounds + 1

        print("")
        print("YOUR WINS: ", playerWins)
        print("COMPUTER WINS: ", computerWins)

        #If player or computer reaches two, display message and exit game
        if(playerWins == 2):
            print("YOU HAVE BEATEN THE COMPUTER.")
        elif(computerWins ==2):
            print("THE COMPUTER HAS BEATEN YOU.")
        
        print("")
        
    #Asks user to play again
    runAgain = input("PLAY AGAIN? (Y/N): ")
    runAgain = runAgain.upper()
    if(runAgain != "Y"):
        print("TOTAL ROUNDS PLAYED: ", totalRounds) #Displays total rounds throughout the entire duration
        break #Exit program


stop = timeit.default_timer() #Records the time when the program concluded.
print("[ Approximate Execution Time (Seconds): ", math.trunc(stop - start), " ]") #Subtract start from stop, round to nearest second
                                                                                    

 
