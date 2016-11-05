import sys
import simplecluestrat

def runGame(list):
  #masterhistory is the absolute state of the game, but is selectively revealed to players on their turn.  
  #A strategy can choose to make use of as much or as little of that info as it wants to.
  masterhistory = [list[0],[list[1],list[2],list[3]],[]]
  n = 0
  gameOver = False
  while not gameOver:
    cleanedhistory = simplecluestrat.cleanMasterHistory(n,masterhistory) #for player n, hide all the things that player n would not have seen
    guess = simplecluestrat.dontBeDumb(cleanedhistory) #player n makes a guess based on his/her strategy, currently hardcoded to dontBeDumb.  Should make this a param.
    guessresult = simplecluestrat.evaluateGuess(n, guess) #the player and the card that respond to the guess
    masterhistory[2].append([n,guess,guessresult]) #update master history with that information
    n=n+1
    #check to see if the last guess was correct.  If it was, then change gameOver to true. 
    if(n==3): 
      gameOver = True
  for item in masterhistory:
    print(item)

def main():
  #future ideas: allow user to choose the cards for the whodunnit for experimentation purposes, have args 
  #that define the strategy of each of the players.   
  if (len(sys.argv) !=2):
    print("pre-screen")
    print("To run the program, please enter these args:")
    print("simpleclue.py numberOfPlayers")
    for item in sys.argv:
      print(item)
    sys.exit(0)  
  #outcome = runGame(sys.argv)
  #Shuffle and deal the cards now.  Use runGame for the mechanics. 
  answer = [[0,0],[1,0],[2,0]]
  #assuming only 3 players for now to keep things simple
  player0 = [[0,1],[1,1],[2,1]]
  player1 = [[0,1],[1,1],[2,1]]
  player2 = [[0,1],[1,1],[2,1]]
  runGame([answer, player0, player1, player2])

#NOTE: need a quick and easy way to build up the game history so that you can actually use this to play clue. 
#NOTE: you may not end up finishing runGame because you really only want to use this to play a game of Clue. 
if __name__ == '__main__':
  main()