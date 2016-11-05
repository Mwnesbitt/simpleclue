"""
master history format:
[answer, player's cards, turn history]

answer format:
[card0, card1, card2]

card format:
[cardtype, cardnumber]

player's cards format:
[player1 cards, player2 cards...]

turn history format:
[turn 1, turn 2, ...]

turn format
[guessing player, guess, [disprover, disproving card]]

guess format: 
[card0, card1, card2]
"""

def dontBeDumb(cleanedhistory):
  #this needs to take in only the facts, and then it makes a best guess given those facts
  
  return [[0,0],[1,0],[2,1]]

def cleanMasterHistory(playernumber, masterhistory):
  #needs to mask everything that playernumber should not have been able to see, censor it for that player
  return masterhistory
  
def evaluateGuess(playernumber, guess):
  #This takes the player number and the guess, and returns the player number disproving it and the disproving card
  #for now if the disproving player can disprove with 2 cards, the game will randomly pick which card (actually probably pick the first card).
  #In the future, however, you could have a strategy here that you call to decide which card to show.
  #Don't forget to code what happens if the guess is correct.  Maybe just pass back x's or something. 
  return [1, [0, 0]]