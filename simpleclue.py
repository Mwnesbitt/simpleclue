import sys
import simplecluestrat

def runGame(gameStyle, list):
  #masterhistory is the absolute state of the game, but is selectively revealed to players on their turn.  
  #A strategy can choose to make use of as much or as little of that info as it wants to.
  masterhistory = [list[0],[list[1],list[2],list[3]],[]] #assuming only 3 players for now.  
  n = 0
  gameOver = False
  while not gameOver:
    tempjunk = input("Enter the player number:")
    if(tempjunk is "x"):
      break
    if(int(tempjunk)>n):
      n=int(tempjunk)
    cleanedhistory = simplecluestrat.cleanMasterHistory(n%3,masterhistory) #for player n, hide all the things that player n would not have seen
    if(gameStyle ==1):
      guess = simplecluestrat.inputGuess()
      guessresponse = simplecluestrat.inputGuessResponse()
    else:
      guess = simplecluestrat.dontBeDumb(cleanedhistory) #player n makes a guess based on his/her strategy, currently hardcoded to dontBeDumb.  Should make this a param.
      guessresponse = simplecluestrat.evaluateGuess(n, guess, masterhistory) #the player and the card that respond to the guess
    masterhistory[2].append([n,guess,guessresponse]) #update master history with that information
    n=n+1
    print(guessresponse)
    print(guessresponse == ['x',['x','x']])
    if(guessresponse == ['x',['x','x']]):
      gameOver=True
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
  #assuming only 3 players for now to keep things simple
  player0 = [[0,1],[1,1],[2,1]]
  player1 = [[0,1],[1,1],[2,2]]
  player2 = [[0,1],[1,1],[2,2]]
  gameStyle = int(input("1 for manual, 2 for computer-run:")) #Note: not planning on building out option #2.  The bones are all there to do it, though.
  if(gameStyle==1):
    x="x"
    answer=[[x,x],[x,x],[x,x]]
  else:
    answer = [[0,0],[1,0],[2,0]]
  #The player to the left of the person using the program is player 0.
  runGame(gameStyle, [answer, player0, player1, player2])

#NOTE: would love to have this data structure reviewed by an experienced code.  There has GOT to be a better way of doing this.
#NOTE: need to have a way where if you mistype, it doesn't wreck the code.
if __name__ == '__main__':
  main()