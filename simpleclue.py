#Work on usability by printing relevant things that are formatted in an easy to read way.  Number all the lists that the user sees and selects from.

#need to figure out how to prevent a typo from breaking the entire game.  
#read online to get good strategies

import sys

class Game(object):
  #should all variables always be self.var ?
  suspects = ["Miss Scarlet", "Professor Plum", "Mrs. Peacock", "Mr. Green", "Colonel Mustard", "Mrs. White"]
  weapons = ["Candlestick", "Knife", "Pipe", "Revolver", "Rope", "Wrench"]
  rooms = ["Ballroom", "Conservatory", "Billiard Room", "Library", "Study", "Hall", "Lounge", "Dining Room", "Kitchen"]
  turnHistory = []
    
  def __init__(self, players): #for now the game assumes all manual players, just taking an int for the number of them.  Need a way to shuffle and deal the cards for an automatic game.
    #I tried to define this outside of __init__ so they are global/constants for all games... not sure why but it didn't work.     
    self.players = players #number of players in the game    
    self.solution = Scene() #Manually entered for now.
    self.startingPlayer = int(input("Enter the player number who starts first (player 0 through %d)\n" %(self.players-1)))
    self.userPlayerNumber = int(input("Enter your player number (player 0 through %d)\n" %(self.players-1)))
    self.userStrategy = Strategy(self) #this can be where the user selects which Strategy to use.
  
  #def addYourCards is used in manual games for the user to type in what cards they have.  This again makes me think cards should be a class.
  
  def play(self):
    self.gameOver = False
    while(not self.gameOver):    
      self.turnHistory.append(Turn(self))
      self.gameOver = self.turnHistory[-1].accusationCorrect
      
class Scene(Game):  #not sure if it should extend Game, but every scene lives within a game, right?  I'm doing it to get access to the suspects, weapons, and rooms
  
  def __init__(self):
    self.scene=[]
    print("Select, using 0 to %d, the Scene's suspect: " % (len(self.suspects)-1))
    for item in self.suspects:
      print(item)
    self.scene.append(int(input("> ")))
    
    print("Select, using 0 to %d, the Scene's weapon: " % (len(self.weapons)-1))
    for item in self.weapons:
      print(item)
    self.scene.append(int(input("> ")))
    
    print("Select, using 0 to %d, the Scene's room: " % (len(self.rooms)-1))
    for item in self.rooms:
      print(item)
    self.scene.append(int(input("> ")))
    
    print("You selected the following scene:")
    self.printScene()

  def printScene(self):
    print(self.suspects[self.scene[0]])
    print(self.weapons[self.scene[1]])
    print(self.rooms[self.scene[2]])

class Turn(Game): #not sure if it should extend Game, but a turn lives inside a game and I may need access to the suspects, weapons, and rooms.
  
  def __init__(self,gameName):
    self.number = len(self.turnHistory)
    self.player = (gameName.startingPlayer + self.number)%gameName.players
    #good practice?  Declare all the variables that a turn needs right here and now and set them to nothing and then start modifying them.
    print("Ok!  Let's begin turn number %d" % self.number)
    print("This is player %d's turn.  You are player %d" %(self.player,gameName.userPlayerNumber))
    if(self.player==gameName.userPlayerNumber):
      gameName.userStrategy.printTopThree(gameName)
    self.accusationMade = input("Was there an accusation made? (y/n)\n")
    self.accusationCorrect = False
    if(self.accusationMade == 'y'):
      #self.accusationCorrect = False
      self.accusation = Scene() #will need to pass parameter for manual once manual/automatic distinction is created
      self.respondingPlayer = input("Type the player number who answered (press ENTER if no one answered)\n")
      if(self.respondingPlayer):
        # this section seems waaaay too cumbersome.  There should be a way to improve this.  Card object?
        self.temp1Response = input("Type the type used to disprove the accusation (suspect, weapon, room) (press ENTER if you didn't see it)\n")
        if('suspect' in self.temp1Response):
          print("Which Suspect?")
          for suspect in gameName.suspects:
            print(suspect)
          self.tempjunk = int(input("Enter the number: ")) # can this be combined with the next line?
          self.respondingCard = gameName.suspects[self.tempjunk]
        elif('weapon' in self.temp1Response):
          print("Which Weapon?")
          for weapon in gameName.weapons:
            print(weapon)
          self.tempjunk = int(input("Enter the number: "))
          self.respondingCard = gameName.weapons[self.tempjunk]
        elif('room' in self.temp1Response):
          print("Which Room?")
          for room in gameName.rooms:
            print(room)
          self.tempjunk = int(input("Enter the number: "))
          self.respondingCard = gameName.rooms[self.tempjunk]
        else:
          print("Ok, you didn't see it.")
          self.respondingCard = ''
        self.respondingPlayer = int(self.respondingPlayer)
      else:
        print("The accusation was correct.  Game Over!")
        self.accusation.printScene()
        self.accusationCorrect=True
    else:
      self.respondingPlayer = None
      #self.accusationCorrect = False
      
  def printTurn(self, gameName):
    print("\nHistory for Turn Number: %d" %self.number)
    print("Player Number: %d" %self.player)
    print("An accusation was made: %s" %self.accusationMade)
    print("Responding player: %r" %self.respondingPlayer)
    print("Responding card: %r" %self.respondingCard)

class Strategy(Game):
  def __init__(self, gameName):
    pass
  def printTopThree(self, gameName):
    print("Here's the turn history\n")
    for turnItem in gameName.turnHistory:
      turnItem.printTurn(gameName)
    print("Here are your top 3 guesses according to this algorithm")
    print("Mustard, Knife, Ballroom")
    print("Mustard, Knife, Ballroom")
    print("Mustard, Knife, Ballroom")

players = int(input("How many players?\n"))
test = Game(players)
test.play()