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
  #First step should be to compile a list of all possible guesses
  #Then remove all guesses that contain a card that you've seen
  #The above is one option, another would be to try to make a map of where all the cards are.  Then you can try to build guesses based off that map
  
  return [[0,0],[1,0],[2,1]]

def cleanMasterHistory(playernumber, masterhistoryobject):
  #needs to mask everything that playernumber should not have been able to see, censor it for that player
  cleanedhistory=masterhistoryobject[:]
  print(masterhistoryobject)
  x="x"
  cleanedhistory[0]=[[x,x],[x,x],[x,x]]
  allplayerscards=cleanedhistory[1]  
  cleanedhistory[1]=allplayerscards[playernumber]  #this needs to be changed to put x's in for other players cards to maintain data structure
  turnhistory=cleanedhistory[2]
  for turn in turnhistory:
    junk= turn[2]
    tempjunk = junk[:]
    #print(turn[0]%3)
    #print(playernumber)
    #print(turn[0]%3 == playernumber)
    #print(tempjunk[0])
    #print(playernumber)
    #print((tempjunk[0] == playernumber))
    #print((turn[0]%3 == playernumber) | (tempjunk[0] == playernumber))
    if((turn[0]%3 != playernumber) & (tempjunk[0] != playernumber)):
      #print("yup")
      response = turn[2]
      response[1]=[x,x]
      turn[2]=response[:]
  cleanedhistory[2]=turnhistory #I don't think I need this line since these two objects have the same memory location
  print(masterhistoryobject)
  return cleanedhistory
  
def evaluateGuess(playernumber, guess, masterhistory):
  #This takes the player number and the guess, and returns the player number disproving it and the disproving card
  #for now if the disproving player can disprove with 2 cards, the game will pick the first card to show.
  #In the future, however, you could have a strategy here that you call to decide which card to show.
  allplayerscards = masterhistory[1]
  respondingplayer = playernumber + 1
  while(respondingplayer != playernumber): 
    relevantcards=allplayerscards[respondingplayer]
    if(guess[0] in relevantcards):
      return [respondingplayer, guess[0]]
    if(guess[1] in relevantcards):
      return [respondingplayer, guess[1]]
    if(guess[2] in relevantcards):
      return [respondingplayer, guess[2]]
    respondingplayer = (respondingplayer+1)%3 #need a parameter for number of players, assuming 3 for now while building. 
  return ["x",["x","x"]] #no one can disprove the guess, i.e. the guess was correct.
      
  #return [1, [0, 0]]

def inputGuess():
  character = int(input("What character number was guessed?"))
  weapon = int(input("What weapon number was guessed?"))
  room = int(input("What room number was guessed?"))
  return [[0,character],[1,weapon], [2, room]]
  
def inputGuessResponse():
  tempjunk= input("Enter the player number that responded to the guess (leave blank if no one responded):")
  if(tempjunk is ""):
    playernumber = "x"
  else:
    playernumber = int(tempjunk)
  tempjunk = input("Enter 0 for a character, 1 for weapon, 2 for room (leave blank if you don't know):")
  if(tempjunk):
    card0 = int(tempjunk)
  else:
    card0 = "x"
  tempjunk = input("Enter 0 through n for which character/weapon/room it was (leave blank if you don't know):") #this isn't necessary-- it should look at the guess and if we know that the character card was replied with, we know the character as well since it was in the guess.
  if(tempjunk):
    card1 = int(tempjunk)
  else:
    card1 = "x"
  return [playernumber, [card0,card1]]