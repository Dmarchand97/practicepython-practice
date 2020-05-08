#Rock paper scissors
#Make a two-player Rock-Paper-Scissors game
#Rock beats scissors
#Scissors beats paper
#Paper beats rock

player1 = input("rock, paper, or scissors?... ")
player2 = input("rock, paper, or scissors?... ")

def winner(u1, u2):
    if u1 == u2:
        return("Its a tie! Try again!")
    elif u1 == "rock":
        if u2 == 'scissors':
            return("Rock Wins! Play Again...?")
        else:
            return("Paper Wins! Play Again...?")
    elif u1 == "scissors":
        if u2 == 'paper':
            return("scissors Wins! Play Again...?")
        else:
            return("rock Wins! Play Again...?")
    elif u1 == "paper":
        if u2 == 'rock':
            return("paper Wins! Play Again...?")
        else:
            return("scissors Wins! Play Again...?")
    else:
        return("NO! WRONG! INVALID! ONLY ROCK, PAPER, SCISSORS!!!")

print(winner(player1, player2))