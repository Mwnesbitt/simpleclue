# TO DO #

#MPV Items:
#  Push forward on the strategy: producing the ranking of each of the card types.

#Update readme to reflect refined scope.  
#  Project isn't to simulate a game of clue-- it's to assist someone playing it by giving them their best guesses.  Consdering new name: clueAssistant
#  Thus, all parts of the code that were meant to be flexible or allow for automatic play of the game have been removed
#  MVP reached -- still a bit fragile but it can be used now.  See Beyond MVP section for the list of things that should be done.
#  Need better way of handling cards.  Dict?
#  Make a note about how you're assuming a single strategy (MapRefinement) but how things could change if there were several available.
#  Make a note about how the code doesn't do any checking on whether user entries make sense/are possible. (also if a weapon stopped an accusation the user shouldn't have to type it in)

#Beyond MVP
#  Asking the user to confirm is cloogy inside of a turn-- you have to confirm the scene twice-- if you reject the second one the whole turn gets restarted.  You need to go through the process-- when a turn is confirmed it should be a) improved for when there was no accusation and b) if the user does not confirm the player that responded the user should not be asked to input the scene again.  
#  Do an audit-- go through a mock game to make sure there aren't bugs, come up with some scenarios to test the logic.
#  Use learn-python-the-hard-way to review best practices and make sure the code follows these.  (init function not overloaded?) 
#  Look for duplicated code (printing lists, some noted in the comments, spend some time looking through to think about how you can simplify and group/condense things into their proper logical groups.
#  Additional strategy improvements.  Right now the strategy isn't super sophisticated-- it uses 1/2 dozen basic things to refine the map and may not be determining as much as it could.  Think hard to make sure the strategy is capturing everything-- come up with scenarios where information is learned and make sure the strategy grabs that info. Read online to get good strategies.  Think about making a while loop that performs internal checks on the map-- what can it learn from itself?  Once you've done the "matrix" work, go back through turnByTurn (maybe beef the method itself up), Loop through the turns and see what else you learn from the turn now that the map has been updated.  terminate the while loop if the map after the while loop is the same as the map before it.
#  Allow the game to print out its state to a file and to load a state from a properly formatted file.  Then you can put game.play() inside a try-catch that prints to the file if an exception is encountered.  Then you can go edit the file (if necessary) and start a new game and point it to that file so you don't lose all your progress.  Probably storing all Game variables would be enough.

import sys

class Game(object):
  def __init__(self): 
    #space at the end of each card is my bad way of making printing turns look good
    self.cards = [
    "Miss Scarlet    ", 
    "Professor Plum  ", 
    "Mrs. Peacock    ", 
    "Mr. Green       ", 
    "Colonel Mustard ", 
    "Mrs. White      ",
    "Candlestick     ",
    "Knife           ", 
    "Pipe            ", 
    "Revolver        ", 
    "Rope            ", 
    "Wrench          ",
    "Ballroom        ", 
    "Conservatory    ", 
    "Billiard Room   ", 
    "Library         ", 
    "Study           ", 
    "Hall            ", 
    "Lounge          ", 
    "Dining Room     ", 
    "Kitchen         "]
    self.suspectsList = [self.cards[0], self.cards[1], self.cards[2], self.cards[3], self.cards[4], self.cards[5]]
    self.weaponsList = [self.cards[6], self.cards[7], self.cards[8], self.cards[9], self.cards[10], self.cards[11]]
    self.roomsList = [self.cards[12], self.cards[13], self.cards[14], self.cards[15], self.cards[16], self.cards[17], self.cards[18], self.cards[19], self.cards[20]]
    
    self.turnHistory = []
    self.players = int(input("\nHow many players?\n"))
    self.startingPlayer = int(input("\nEnter the player number who starts first (player 0 through %d)\n" %(self.players-1)))
    self.user = Player(self)
      
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
      return self.cards
    
  def printCards(self, cardType): #this code is somewhat redudant with the code in setScene in the class Scene
    for item in self.cards:
      print(self.cards.index(item), item)
  
class Scene(object):
  
  def __init__(self,gameName):
    self.suspect=""
    self.weapon=""
    self.room=""
    
    while True:
      self.setScene(gameName)
      print("\nThe following scene was entered:")
      self.printScene()
      repeat = input("\nPress ENTER to confirm the scene")
      if(not repeat):
        break
    
  def setScene(self, gameName):
    print("\nSelect, using 0 to %d, the Scene's suspect: " % (len(gameName.suspectsList)-1))
    for item in gameName.suspectsList:
      print(gameName.suspectsList.index(item), item)
    self.suspect = gameName.suspectsList[int(input("> "))]  #stored as pointer to the suspect's string, correct?
  
    print("\nSelect, using 0 to %d, the Scene's weapon: " % (len(gameName.weaponsList)-1))
    for item in gameName.weaponsList:
      print(gameName.weaponsList.index(item), item)
    self.weapon = gameName.weaponsList[int(input("> "))]
    
    print("\nSelect, using 0 to %d, the Scene's room: " % (len(gameName.roomsList)-1))
    for item in gameName.roomsList:
      print(gameName.roomsList.index(item), item)
    self.room = gameName.roomsList[int(input("> "))]      
      
  def printScene(self):
    print(self.suspect, self.weapon, self.room, end = "")

    
class Turn(object):
  
  def __init__(self,gameName):
    self.number = len(gameName.turnHistory)
    self.player = (gameName.startingPlayer + self.number)%gameName.players
    self.accusationMade = ""
    self.accusation = None
    self.accusationCorrect = False
    self.respondingPlayer = None
    self.respondingCard = None
    
    print("\n","-"*20)
    print("TURN NUMBER: %d" % self.number)
    print("Player %d's turn.  (You are player %d)\n" %(self.player,gameName.user.number))
  
    if(self.player==gameName.user.number):
      gameName.user.implementStrategy(gameName)
    
    while True:
      self.accusationMade = input("Was there an accusation made? (y/n)\n")  
      if(self.accusationMade == 'y'):
        self.manageAccusation(gameName)
      
      print("Player %r answered and the card was %r" %(self.respondingPlayer, self.respondingCard))      
      repeat = input("\nPress ENTER to confirm this turn")
      if(not repeat):
        break
    
  def manageAccusation(self,gameName):
    self.accusation = Scene(gameName) 
    self.respondingPlayer = input("\nType the player number who answered.  Player %d made the accusation. (press ENTER if no one answered)\n" % self.player)
    if(self.respondingPlayer):
      for item in gameName.cards:
        print(gameName.cards.index(item), item) #Seems like redundant code-- condense this type of card presentation into one code area?
      self.tempjunk = input("\nEnter the number of the card.  (press ENTER if you didn't see it)\n")
      if(self.tempjunk):
        self.respondingCard = gameName.cards[int(self.tempjunk)]
      else:
        print("Ok, you didn't see it.")
      self.respondingPlayer = int(self.respondingPlayer)
    else:
      print("The accusation was correct.  Game Over!\n")
      self.accusation.printScene()
      self.accusationCorrect=True
      
  def printTurn(self, gameName): #can the branching be eliminated?  If self.accusation is None and .printScene is called, what happens?  error, right?
    if(self.accusationMade == 'y'):
      print("Turn %d " %self.number, "Player %d " %self.player, end = "")
      self.accusation.printScene()
      print(" Responding player: %r, " %self.respondingPlayer, self.respondingCard)
    else:
      print("Turn %d " %self.number, "Player %d " %self.player)

class MapRefinement(object):

  def __init__(self,gameName):
    self.myMap = {}
    for item in gameName.cards:
      self.myMap[item] = Maplet(gameName)
      
  def executeStrategy(self,gameName):
    print("EXECUTE STRATEGY")
    self.userCards(gameName)
    self.viewedCards(gameName)
    self.unheldCards(gameName)    
    self.turnByTurn(gameName) 
    #The map has completed all it's 'known' information.  Now we move on to inferred information
    self.convertToInferred(gameName)
    
    #inferred information: 
    self.dingAccusations(gameName)
    self.cardStopping(gameName)
    
    #Ranking: Best card to guess would be one where you see lots of people don't have the card.  Also one where there is a lot of negative weights.
    #for card in gameName.cards:

    self.printTurnHistory(gameName)    
    print("\n\nMap at end of strategy execution")
    self.printMap(gameName)
    print("-"*20)
    print("\nHere are the rankings for each card Type:")
    print("RANKING HERE")
    print("-"*20)
  
  def cardStopping(self,gameName): #someone stops a card. (gives a boost).  More than once gives something like adding the triangular number of the times a card is stopped to the weighting?
    for card in gameName.cards:
      if(not self.myMap[card].locationDetermined):
        tempMaplet = self.myMap[card]
        counterMaplet = Maplet(gameName)
        for item in counterMaplet.contents:
          counterMaplet.contents[counterMaplet.contents.index(item)]=0
        for turnItem in gameName.turnHistory:
          if(turnItem.accusationMade == "y"):
            if(turnItem.accusation.suspect == card or (turnItem.accusation.weapon == card or turnItem.accusation.room == card)):
              #count the number of times a particular player has stopped a scene with the card in it
              counterMaplet.contents[turnItem.respondingPlayer] +=1 #number of times each player has stopped the card.
        for position in counterMaplet.contents:
          print(int((position*(position+1))/2))
          tempMaplet.contents[counterMaplet.contents.index(position)]+= int((position*(position+1))/2)
  
  def dingAccusations(self,gameName):
    for turnItem in gameName.turnHistory:
      if(turnItem.accusationMade == "y"):
        tempMaplet = self.myMap[turnItem.accusation.suspect]
        tempMaplet.contents[turnItem.player]-=1
        tempMaplet = self.myMap[turnItem.accusation.weapon]
        tempMaplet.contents[turnItem.player]-=1
        tempMaplet = self.myMap[turnItem.accusation.room]
        tempMaplet.contents[turnItem.player]-=1
  
  def convertToInferred(self, gameName):
    print("convertToInferred called")
    for card in gameName.cards:
      tempMaplet = self.myMap[card]
      for position in tempMaplet.contents:
        #print("interior loop")
        if(position == None):
          #print("interior branch")
          tempMaplet.contents[tempMaplet.contents.index(position)] = 0
  
  def printMap(self,gameName):
    for item in gameName.cards:
      print(item, end = "")
      self.myMap[item].printMaplet()
      print()

  def userCards(self,gameName):
    for card in gameName.user.cards:
      tempMaplet = self.myMap[card]
      tempMaplet.setTrue(gameName.user.number)    
    
  def viewedCards(self, gameName):
    for turnItem in gameName.turnHistory:
      #print(turnItem.respondingCard)
      if(turnItem.respondingCard):
        tempMaplet = self.myMap[turnItem.respondingCard]
        tempMaplet.setTrue(turnItem.respondingPlayer)
  
  def unheldCards(self, gameName):
    for turnItem in gameName.turnHistory:
      if(turnItem.accusationMade == "y"):
        tempjunk = (turnItem.player + 1) % gameName.players
        while tempjunk != turnItem.respondingPlayer: #This next block could definitely be more efficient
          #player with number of tempjunk doesn't have any of the cards in the scene
          tempscene = turnItem.accusation
          
          tempsuspect = tempscene.suspect
          tempMaplet = self.myMap[tempsuspect]
          if(tempMaplet.contents[tempjunk] == True):
            print("ERROR IN UNHELDCARDS, suspect")
            sys.exit(1)
          tempMaplet.contents[tempjunk] = False
          
          tempweapon = tempscene.weapon
          tempMaplet = self.myMap[tempweapon]
          if(tempMaplet.contents[tempjunk] == True):
            print("ERROR IN UNHELDCARDS, weapon")
            sys.exit(1)
          tempMaplet.contents[tempjunk] = False
          
          temproom = tempscene.room
          tempMaplet = self.myMap[temproom]
          if(tempMaplet.contents[tempjunk] == True):
            print("ERROR IN UNHELDCARDS, room")
            sys.exit(1)
          tempMaplet.contents[tempjunk] = False
          
          tempjunk= (tempjunk + 1) % gameName.players

  def turnByTurn(self, gameName): #can probably get more information into the map in this method.  Also this code is very inefficient.
    for turnItem in gameName.turnHistory:
      if(turnItem.accusationMade == "y"):
        #get the 3 cards from the accusation in the turn
        #check to see their status for the player that disproved the accusation.  If any pair are False, then set the 3rd to be true.  
      
        suspectMaplet = self.myMap[turnItem.accusation.suspect]
        weaponMaplet = self.myMap[turnItem.accusation.weapon]
        roomMaplet = self.myMap[turnItem.accusation.room]
        if((suspectMaplet.contents[turnItem.respondingPlayer] == False) and (weaponMaplet.contents[turnItem.respondingPlayer] == False)):
          roomMaplet.setTrue(turnItem.respondingPlayer)
        elif((weaponMaplet.contents[turnItem.respondingPlayer] == False) and (roomMaplet.contents[turnItem.respondingPlayer] == False)):
          suspectMaplet.setTrue(turnItem.respondingPlayer)
        elif((roomMaplet.contents[turnItem.respondingPlayer] == False) and (suspectMaplet.contents[turnItem.respondingPlayer] == False)):
          weaponMaplet.setTrue(turnItem.respondingPlayer)
        else:
          pass
  
  def printTurnHistory(self, gameName):
    print("\n","-"*20,"\nHere's the turn history\n")
    for turnItem in gameName.turnHistory:
      turnItem.printTurn(gameName)
    print("-"*20)
    
    
class Maplet(object):  #Nothing except for MapRefinement will interact with Maplets
  def __init__(self,gameName):
    self.contents = []
    self.locationDetermined = False
    i=0
    while i < gameName.players:
      self.contents.append(None)
      i+=1
    """
    for x in range(gameName.players - 1):
      self.contents.append(None)
    """
  
  def setTrue(self, player):
    
    for item in self.contents:
      self.contents[self.contents.index(item)] = False
    """
    i = 0
    while i < len(self.contents):
      self.contents[i] = False
      i+=1
    """
    self.contents[player] = True
    self.locationDetermined = True
  
  def getMaplet(self):
    return self.contents
  
  def printMaplet(self):
    for item in self.contents:
      print(item, end = "")
      
class Player(object):
  def __init__(self, gameName):
    
    while True:
      self.number = int(input("\nEnter your player number (player 0 through %d)\n" %(gameName.players-1)))
    
      self.cards = []    
      print("\nStart entering your cards:")
      for item in gameName.cards:
        print(gameName.cards.index(item), item) #Seems like redundant code-- condense this type of card presentation into one code area?
      while True:  
        self.tempCard = input("\nEnter the number of the card.  (press ENTER if done)\n")
        if(not self.tempCard):
          break
        else:
          self.cards.append(gameName.cards[int(self.tempCard)])
      print("You are player %d\n" %self.number)
      print("Your cards are: ")   
      self.printCards(gameName)
      repeat = input("\nPress ENTER to confirm that these are your cards:")
      if(not repeat):
        break
  
  def implementStrategy(self, gameName):
    self.myStrategy = MapRefinement(gameName)
    self.myStrategy.executeStrategy(gameName)
  
  def printCards(self,gameName):
    for item in self.cards:
      print(item)
      
test = Game()
test.play()