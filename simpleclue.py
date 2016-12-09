#Go through the best practices section of learn python the hard way and edit the code to reflect best practices.  Look for duplicated code (printing lists).  init function does too much
#You've got lots of duplicated code-- spend some time looking through to think about how you can simplify things and despaghetti this.  It's not
#so bad right now but you can definitely do better.

#Once the code is clean and tight, you need to figure out how to prevent a typo from breaking the entire game.  (Basically every input chunk of code that takes
#user input needs to be inside some block of code that reruns if the user doesn't confirm after the code prints what they entered and asks for confirmation)

#Actually make a strategy that helps you.  Read online to get good strategies.  Think about how to make strategies that filter out guesses so that you can 
#choose the rooms

import sys

class Game(object):
  #should all variables always be self.var ?
  suspects = ["Miss Scarlet", "Professor Plum", "Mrs. Peacock", "Mr. Green", "Colonel Mustard", "Mrs. White"]
  weapons = ["Candlestick", "Knife", "Pipe", "Revolver", "Rope", "Wrench"]
  rooms = ["Ballroom", "Conservatory", "Billiard Room", "Library", "Study", "Hall", "Lounge", "Dining Room", "Kitchen"]
  turnHistory = []
    
  def __init__(self): #for now the game assumes all manual players, just taking an int for the number of them.  Need a way to shuffle and deal the cards for an automatic game.
    #I tried to define this outside of __init__ so they are global/constants for all games... not sure why but it didn't work.         
    self.players = int(input("\nHow many players?\n"))
    self.solution = Scene() #Manually entered for now.
    self.startingPlayer = int(input("\nEnter the player number who starts first (player 0 through %d)\n" %(self.players-1)))
    self.userPlayerNumber = int(input("\nEnter your player number (player 0 through %d)\n" %(self.players-1)))
    self.userStrategy = Strategy(self) #this can be where the user selects which Strategy to use.
    user = Player(self)
    user.inputCards(self)
      
  def play(self):
    self.gameOver = False
    while(not self.gameOver):    
      self.turnHistory.append(Turn(self))
      self.gameOver = self.turnHistory[-1].accusationCorrect
  
  def listGameCards(self, cardType): #this whole method can be more efficiently written (less code) and also is duplicated elsewhere in this file
    if("suspect" in cardType):
      for item in self.suspects:
        print(self.suspects.index(item), item)
    elif("weapon" in cardType):
      for item in self.weapons:
        print(self.weapons.index(item), item)
    elif("room" in cardType):
      for item in self.rooms:
        print(self.rooms.index(item), item)
    else:
      self.listGameCards("suspect")
      print()
      self.listGameCards("weapon")
      print()
      self.listGameCards("room")
      print()
  
  def getCards(self, cardType):
    if("suspect" in cardType):
      return self.suspects
    elif("weapon" in cardType):
      return self.weapons
    elif("room" in cardType):
      return self.rooms
    else:
      print("ERROR in getCards")
  
class Scene(Game):  #not sure if it should extend Game, but every scene lives within a game, right?  I'm doing it to get access to the suspects, weapons, and rooms
  
  def __init__(self):
    self.scene=[]
    print("\nSelect, using 0 to %d, the Scene's suspect: " % (len(self.suspects)-1))
    for item in self.suspects:
      print(self.suspects.index(item), item)
    self.scene.append(int(input("> ")))
    
    print("\nSelect, using 0 to %d, the Scene's weapon: " % (len(self.weapons)-1))
    for item in self.weapons:
      print(self.weapons.index(item), item)
    self.scene.append(int(input("> ")))
    
    print("\nSelect, using 0 to %d, the Scene's room: " % (len(self.rooms)-1))
    for item in self.rooms:
      print(self.rooms.index(item), item)
    self.scene.append(int(input("> ")))
    
    print("\nYou selected the following scene:")
    self.printScene()

  def printScene(self):
    print(self.scene[0], self.suspects[self.scene[0]])
    print(self.scene[1], self.weapons[self.scene[1]])
    print(self.scene[2], self.rooms[self.scene[2]])

class Turn(Game): #not sure if it should extend Game, but a turn lives inside a game and I may need access to the suspects, weapons, and rooms.
  
  def __init__(self,gameName):
    self.number = len(self.turnHistory)
    self.player = (gameName.startingPlayer + self.number)%gameName.players
    #good practice?  Declare all the variables that a turn needs right here and now and set them to nothing and then start modifying them.
    print("\n","-"*20)
    print("TURN NUMBER: %d" % self.number)
    print("Player %d's turn.  (You are player %d)" %(self.player,gameName.userPlayerNumber))
    if(self.player==gameName.userPlayerNumber):
      gameName.userStrategy.printTopThree(gameName)
    self.accusationMade = input("\nWas there an accusation made? (y/n)\n")
    self.accusationCorrect = False
    self.respondingCard = None
    if(self.accusationMade == 'y'):
      #self.accusationCorrect = False
      self.accusation = Scene() #will need to pass parameter for manual once manual/automatic distinction is created
      self.respondingPlayer = input("\nType the player number who answered.  Player %d made the accusation. (press ENTER if no one answered)\n" % self.player)
      if(self.respondingPlayer):
        # this section seems waaaay too cumbersome.  There should be a way to improve this.  Card object?
        self.temp1Response = input("\nType the type used to disprove the accusation (suspect, weapon, room) (press ENTER if you didn't see it)\n")
        if('suspect' in self.temp1Response):
          print("\nWhich Suspect?")
          for suspect in gameName.suspects:
            print(gameName.suspects.index(suspect), suspect)
          self.tempjunk = int(input("\nEnter the number: ")) # can this be combined with the next line?
          self.respondingCard = gameName.suspects[self.tempjunk]
        elif('weapon' in self.temp1Response):
          print("\nWhich Weapon?")
          for weapon in gameName.weapons:
            print(gameName.weapons.index(weapon), weapon)
          self.tempjunk = int(input("\nEnter the number: "))
          self.respondingCard = gameName.weapons[self.tempjunk]
        elif('room' in self.temp1Response):
          print("\nWhich Room?")
          for room in gameName.rooms:
            print(gameName.rooms.index(room), room)
          self.tempjunk = int(input("\nEnter the number: "))
          self.respondingCard = gameName.rooms[self.tempjunk]
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
    print("\nHistory for Turn Number: %d" %self.number)
    print("Player Number: %d" %self.player)
    print("An accusation was made: %s" %self.accusationMade)
    print("The accusing scene was: ")# NEED TO PRINT THE SCENE
    print("Responding player: %r" %self.respondingPlayer)
    print("Responding card: %r" %self.respondingCard)

class Strategy(Game):
  def __init__(self, gameName):
    pass
  def printTopThree(self, gameName):
    print("\n","-"*20,"\nHere's the turn history\n")
    for turnItem in gameName.turnHistory:
      turnItem.printTurn(gameName)
    print("-"*20)
    print("\nHere are your top 3 guesses according to this algorithm")
    print("Mustard, Knife, Ballroom")
    print("Mustard, Knife, Ballroom")
    print("Mustard, Knife, Ballroom")

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
        gameName.listGameCards(self.cardType)
        self.cardNumber = int(input("\nEnter Card Number:\n"))
        temp = gameName.getCards(self.cardType)
        self.cards.append(temp[self.cardNumber])
        print(self.cardType, self.cardNumber)
    self.printCards(gameName)
    
  def printCards(self,gameName):
    for item in self.cards:
      print(item)
      
test = Game()
test.play()