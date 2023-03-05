"""
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them,
print out a message of congratulations to the winner,
and ask if the players want to start a new game)

Remember the rules:

    *Rock beats scissors
    *Scissors beats paper
    *Paper beats rock
"""
import random
def rpsChecker(string1,string2):
    player1 = 'Player 1 wins.'
    player2 = 'Player 2 wins.'
    if string1 == string2:
        return 'It\'s a draw.'
    elif string1 == 'rock' and string2 == 'paper':
        return player2
    elif string1 == 'rock' and string2 == 'scissors':
        return player1
    elif string1 == 'paper' and string2 == 'rock':
        return player1
    elif string1 == 'paper' and string2 == 'scissors':
        return player2
    elif string1 == 'scissors' and string2 == 'paper':
        return player1
    elif string1 == 'scissors' and string2 == 'rock':
        return player1
while True:
    print('Note: Press ENTER to end the game.')
    player1 = input('Player 1, enter your play: ')
    if player1 == '':
        break
    player2 = input('Player 2, enter your play: ')
    if player2 == '':
        break
    print(rpsChecker(player1,player2))
    
    
