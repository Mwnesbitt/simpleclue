# TO DO:
"""
Get strategy working with known guesses and implement ways of weighting inferred facts
change readme and scope of project to be clueAssistant
Improvements to code: Change subclassing make a note about how strategy might 

#Go through the best practices section of learn python the hard way and edit the code to reflect best practices.  Look for duplicated code (printing lists).  init function does too much
#You've got lots of duplicated code-- spend some time looking through to think about how you can simplify things and despaghetti this.  It's not
#so bad right now but you can definitely do better.

#Once the code is clean and tight, you need to figure out how to prevent a typo from breaking the entire game.  (Basically every input chunk of code that takes
#user input needs to be inside some block of code that reruns if the user doesn't confirm after the code prints what they entered and asks for confirmation)

#Find a way to improve your strategy  Read online to get good strategies.  Think about how to make strategies that filter out guesses so that you can 
#choose the rooms

Need better way of handling cards.  Dict?
"""

import sys

class Game(object):
  #should all variables always be self.var ?
  #space at the end of each card is my bad way of making printing turns look good
  suspectsList = ["Miss Scarlet    ", "Professor Plum  ", "Mrs. Peacock    ", "Mr. Green       ", "Colonel Mustard ", "Mrs. White      "]
  weaponsList = ["Candlestick ", "Knife       ", "Pipe        ", "Revolver    ", "Rope        ", "Wrench      "]
  roomsList = ["Ballroom      ", "Conservatory  ", "Billiard Room ", "Library       ", "Study         ", "Hall          ", "Lounge        ", "Dining Room   ", "Kitchen       "]
  turnHistory = []
  cards = {
  "Miss Scarlet    " : "suspect", 
  "Professor Plum  " : "suspect", 
  "Mrs. Peacock    " : "suspect", 
  "Mr. Green       " : "suspect", 
  "Colonel Mustard " : "suspect", 
  "Mrs. White      " : "suspect",
  "Candlestick " : "weapon",
  "Knife       " : "weapon", 
  "Pipe        " : "weapon", 
  "Revolver    " : "weapon", 
  "Rope        " : "weapon", 
  "Wrench      " : "weapon",
  "Ballroom      " : "room", 
  "Conservatory  " : "room", 
  "Billiard Room " : "room", 
  "Library       " : "room", 
  "Study         " : "room", 
  "Hall          " : "room", 
  "Lounge        " : "room", 
  "Dining Room   " : "room", 
  "Kitchen       " : "room"}
     
  def __init__(self): #for now the game assumes all manual players, just taking an int for the number of them.  Need a way to shuffle and deal the cards for an automatic game.
    #I tried to define this outside of __init__ so they are global/constants for all games... not sure why but it didn't work.         
    self.players = int(input("\nHow many players?\n"))
    #self.solution = Scene() #Manually entered for now.
    self.startingPlayer = int(input("\nEnter the player number who starts first (player 0 through %d)\n" %(self.players-1)))
    self.userPlayerNumber = int(input("\nEnter your player number (player 0 through %d)\n" %(self.players-1))) #this should probably be stored in the player object.
    user = Player(self)
    user.inputCards(self)
    self.userStrategy = Strategy(self) #this can be where the user selects which Strategy to use. 
    self.userStrategy.userCards(self,user)
    self.userStrategy.viewedCards(self)
      
  def play(self):
    self.gameOver = False
    while(not self.gameOver):    
      self.turnHistory.append(Turn(self))
      self.gameOver = self.turnHistory[-1].accusationCorrect
  
  def getCards(self, cardType):
    result = []
    if("suspect" in cardType):
      return self.suspectsList
    elif("weapon" in cardType):
      return self.weaponsList
    elif("room" in cardType):
      return self.roomsList
    else:
      return list(self.cards.keys())
    
  def printCards(self, cardType):
    print()
    for item in self.getCards(cardType):
      print(self.getCards(cardType).index(item), item)
  
class Scene():
  
  def __init__(self,gameName):
    self.suspect=""
    self.weapon=""
    self.room=""
    
    self.suspectsList = gameName.getCards("suspect")
    self.weaponsList = gameName.getCards("weapon")
    self.roomsList = gameName.getCards("room")
    
    print("\nSelect, using 0 to %d, the Scene's suspect: " % (len(gameName.suspectsList)-1))
    for item in gameName.suspectsList:
      print(gameName.suspectsList.index(item), item)
    self.suspect = gameName.suspectsList[int(input("> "))]  #store as int or as pointer to the suspects string?
    #print(self.suspect)
    
    print("\nSelect, using 0 to %d, the Scene's weapon: " % (len(gameName.weaponsList)-1))
    for item in gameName.weaponsList:
      print(gameName.weaponsList.index(item), item)
    self.weapon = gameName.weaponsList[int(input("> "))]
    
    print("\nSelect, using 0 to %d, the Scene's room: " % (len(gameName.roomsList)-1))
    for item in gameName.roomsList:
      print(gameName.roomsList.index(item), item)
    self.room = gameName.roomsList[int(input("> "))]
    
    print("\nYou selected the following scene:")
    self.printScene()

  def printScene(self):
    print(self.suspect, self.weapon, self.room, end = "")
    
  def printSceneLine(self):
    print(self.suspect, self.weapon, self.room, end = "")

    
class Turn(): #not sure if it should extend Game, but a turn lives inside a game and I may need access to the suspects, weapons, and rooms.
  
  def __init__(self,gameName):
    self.number = len(gameName.turnHistory)
    self.player = (gameName.startingPlayer + self.number)%gameName.players
    #good practice?  Declare all the variables that a turn needs right here and now and set them to nothing and then start modifying them.
    print("\n","-"*20)
    print("TURN NUMBER: %d" % self.number)
    print("Player %d's turn.  (You are player %d)" %(self.player,gameName.userPlayerNumber))
    if(self.player==gameName.userPlayerNumber):
      gameName.userStrategy.printTurnHistory(gameName)
    self.accusationMade = input("\nWas there an accusation made? (y/n)\n")
    self.accusationCorrect = False
    self.respondingCard = None
    if(self.accusationMade == 'y'):
      #self.accusationCorrect = False
      self.accusation = Scene(gameName) #will need to pass parameter for manual once manual/automatic distinction is created
      self.respondingPlayer = input("\nType the player number who answered.  Player %d made the accusation. (press ENTER if no one answered)\n" % self.player)
      if(self.respondingPlayer):
        # this section seems waaaay too cumbersome.  There should be a way to improve this.  Card object?
        self.temp1Response = input("\nType the type used to disprove the accusation (suspect, weapon, room) (press ENTER if you didn't see it)\n")
        if('suspect' in self.temp1Response):
          print("\nWhich Suspect?")
          for suspect in gameName.suspectsList:
            print(gameName.suspectsList.index(suspect), suspect)
          self.tempjunk = int(input("\nEnter the number: ")) # can this be combined with the next line?
          self.respondingCard = gameName.suspectsList[self.tempjunk]
        elif('weapon' in self.temp1Response):
          print("\nWhich Weapon?")
          for weapon in gameName.weaponsList:
            print(gameName.weaponsList.index(weapon), weapon)
          self.tempjunk = int(input("\nEnter the number: "))
          self.respondingCard = gameName.weaponsList[self.tempjunk]
        elif('room' in self.temp1Response):
          print("\nWhich Room?")
          for room in gameName.roomsList:
            print(gameName.roomsList.index(room), room)
          self.tempjunk = int(input("\nEnter the number: "))
          self.respondingCard = gameName.roomsList[self.tempjunk]
        else:
          print("Ok, you didn't see it.")
        self.respondingPlayer = int(self.respondingPlayer)
      else:
        print("The accusation was correct.  Game Over!")
        self.accusation.printScene()
        self.accusationCorrect=True
    else:
      self.respondingPlayer = None
      
  def printTurn(self, gameName):
    #print("\nHistory for Turn Number: %d" %self.number)
    print("Turn %d " %self.number, end = "")
    print("Player %d " %self.player, end = "")
    #print("An accusation was made: %s" %self.accusationMade)
    #print("The accusing scene was: ")# NEED TO PRINT THE SCENE
    if(self.accusationMade == 'y'):
      self.accusation.printSceneLine()
      print(" Responding player: %r, " %self.respondingPlayer, end = "")
      print(self.respondingCard)
    else:
      print()

class Strategy(Game):
 
  def __init__(self,gameName):
    #create a dict with the key as the card string and the value as the maplet
    self.myMap = {}
    for item in list(gameName.cards.keys()):
      self.myMap[item] = Maplet(gameName)
  
  def printMap(self,gameName):
    for item in list(self.myMap.keys()):
      print(item, end = "")
      self.myMap[item].printMaplet()
      print()

  def userCards(self,gameName,userName):
    for card in userName.cards:
      #print(self.myMap)
      tempMaplet = self.myMap[card]
      print(tempMaplet)
      tempMaplet.setTrue(gameName.userPlayerNumber)    
    self.printMap(gameName)
    
  def viewedCards(self, gameName):
    print("ViewedCards called")
    for turnItem in gameName.turnHistory:
      print(gameName.respondingCard)
      if(gameName.respondingCard):
        tempMaplet = self.myMap[gameName.respondingCard]
        tempMaplet.setTrue(turnItem.player)
    
  def printTurnHistory(self, gameName):
    print("\n","-"*20,"\nHere's the turn history\n")
    for turnItem in gameName.turnHistory:
      turnItem.printTurn(gameName)
    print("-"*20)
    
    print("\nHere is the Map:")
    self.printMap(gameName)
    print("\nHere are the rankings for each card Type:")    
    
class Maplet(Game):
  #Nothing except for Map will interact with Maplets
  def __init__(self,gameName):
    self.contents = []
    i=0
    while i < gameName.players:
      self.contents.append(0)
      i+=1
  
  def setTrue(self, player):
    """
    for item in self.contents:
      item = False
    """
    i = 0
    while i < len(self.contents):
      self.contents[i] = False
      i+=1
    self.contents[player] = True
    
  def getMaplet(self):
    return self.contents
  
  def printMaplet(self):
    for item in self.contents:
      print(item, end = "")
      
  
class Player(Game):
  def __init__(self, gameName):
    self.cards = []
  def inputCards(self, gameName):
    print("\nStart entering your cards:")
    while True:  
      self.cardType = input("Suspect, Weapon, or Room (ENTER if done)\n\n")
      if(not self.cardType):
        break
      else:
        gameName.printCards(self.cardType)
        self.cardNumber = int(input("\nEnter Card Number:\n"))
        temp = gameName.getCards(self.cardType) #will throw an error due to changing how cards are being stored
        self.cards.append(temp[self.cardNumber])
        #print(self.cardType, self.cardNumber)
    print("Your cards are: ")
    self.printCards(gameName)
    print()
    
  def printCards(self,gameName):
    for item in self.cards:
      print(item)
      
test = Game()
#print(list(test.cards.keys()))
test.play()