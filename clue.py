class Game(object):
  #should all variables always be self.var ?
  
  def __init__(self, players): #for now the game assumes all manual players, just taking an int for the number of them)
    #I tried to define this outside of __init__ so they are global/constants for all games... not sure why but it didn't work.
    self.suspects = ["Miss Scarlet", "Professor Plum", "Mrs. Peacock", "Mr. Green", "Colonel Mustard", "Mrs. White"]
    self.weapons = ["Candlestick", "Knife", "Pipe", "Revolver", "Rope", "Wrench"]
    self.rooms = ["Ballroom", "Conservatory", "Billiard Room", "Library", "Study", "Hall", "Lounge", "Dining Room", "Kitchen"] 
    self.players = players #number of players in the game
    
    self.solution = Scene() #For automatic games, there should be a shuffling assigning cards to players and creating the actual scene.
      
  def play():
    self.startingPlayer = int(input("Enter the player number who starts first (player 0 through %d)" %(self.players-1)))
    
    
class Scene(Game):  #not sure if it should extend Game, but every scene lives within a game, right?  I'm doing it to get access to the suspects, weapons, and rooms
  
  def __init__(self):
    self. scene=[]
    print("Select, using 0 to %d, the Scene's suspect: " % (len(suspects)-1))
    for item in suspects:
      print(item)
    scene.append(int(input("> ")))
    
    print("Select, using 0 to %d, the Scene's weapon: " % (len(weapons)-1))
    for item in self.weapons:
      print(item)
    scene.append(int(input("> ")))
    
    print("Select, using 0 to %d, the Scene's room: " % (len(rooms)-1))
    for item in self.rooms:
      print(item)
    scene.append(int(input("> ")))
    
    print("You selected the following scene:")
    print(self.suspects[scene[0]])
    print(self.weapons[scene[1]])
    print(self.rooms[scene[2]])
    
    
test = Game(4)
print(test.players)