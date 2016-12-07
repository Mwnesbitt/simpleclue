THIS PROJECT IS ON HOLD UNTIL I COMPLETE MORE PYTHON TUTORIALS.

The goal of this project is similar to that of the mastermind project.  I want to simulate the game clue.

For this project, however, I do not already have a good Clue strategy.  I played recently with friends and 
was terrible-- I knew I wasn't taking advantage of half the information available to me, and I felt that
looking at it algorithmically might help.

For this project, I'm simplifying Clue to where there's no gameboard or pieces.  The game just assumes that
the players go around in a circle making their guesses.  The reason for that is because the game gets a lot
harder if you can observe what rooms your opponents choose and eschew.  There's an element of bluffing and 
reading a bluff there that I don't want to get into here.  (There's also an element of bluffing and reading 
a bluff when it comes to the guesses they make.  I'll have to see how that goes-- I might have to ignore that 
source of information too.)

The repository structure will be similar to mastermind: there will be a runGame.py file and a strat.py file.  
Clue is more complicated than mastermind and keeping track of the game state will be tricky as far as the 
data structures go.  We'll see how it goes.



Notes on the current state 12/5
These notes wereinspired by reading the https://learnpythonthehardway.org/book/ex43.html  Jotting down some really rough notes—will return to this later to clean them up. 

A turn is an class that handles most of the activity.  Turns must have an index. 
A game is an class with a method play() that has a while loop that keeps iterating through turns.   Before starting a game though it has to know the number of players and I guess it also has to set the scene cards (How do you play if you want to use this file to actually play in real life where shuffling is what actually decides the scene.)
Is a card an object?  Or should they just be variables in a game?   (I think yes, because those are constant throughout the game.  We don’t need to create them at will).  Do lists: suspects, weapons, rooms.  
What about a scene?  Should that be an object?  (I think yes, because they need to be constantly created)  have a scene.accuse() The game object will check that this method does not return “correct” as a result.  If not correct, it returns the person and possibly the card used to disprove it.   NOW I THINK NO—the accusation can just be a variable in a turn.  

What about players and strategies?  (Players may not be necessary.  The turn should handle that—it just says “What was the guess?”  As for strategies, for now I think there just needs to be a way to type in that it’s all manual and worry about how to automate a game a little later.

Read online about strategies if you want.

So it starts by:
Instantiate a game.  The Game class has the cards (suspects, weapons, rooms) defined as global variables. The __init__ function of the game asks for the number of players.  Make a comment that this can also ask for whether the players are manual or employing a strategy.  When non-all-manual is implemented, (command line param or asked by the init function?), the init function will also ask about the strategies being employed and will also randomly select an element from each of the suspects, weapons, and rooms lists to create the scene.  The init function also records the players names and asks who goes first as variables in the game.  There’s also a counter in the game that keeps track of state by having a counter variable.
Then game.play() is called.  The play() function looks at the counter variable which counts the turns starting from 0.  Has a while loop that increments the turn at the end.  A Turn class gets instantiated.  The Turn class can be stored in variable “turn_”+counter .  The turn class __init__ first checks to see whether the turn is being skipped.  Then it has self.accusation variable that gets set equal to 3 cards.  (in non 100% manual versions this can be done by a strategy.  How does the strategy keep track of the state of the game?  It has to review all previous turns, right?  So turns need to be available to strategies somehow)   There also needs to be an ruling (accusation_ruling, result?) or some variable that says the player that responded to the accusation and the card they used?  (Need to think about global knowledge of the state of the game versus local knowledge.  How do you juggle these?)   Turn needs a “set_accusation()” function that modifies the accusation variable (will always be manually entered) and a “set_ruling()” function that is either set manually or can be set automatically in automatically run games.
So this gives us a situation where all the turns keep stacking up with predictable names that should be easy to iterate through.  Actually they should probably be stored in a list of “turns” and that way their index is their turn number. 
Game needs to have a variable with the actual scene stored in automatic games.  In manual games this variable is set to null or ignored
Game needs to have a variable that stores the player’s actual cards.  This gets entered in for manual games but is set automatically in automatic games.  
So the game is looping through turns, and each turn that comes up the user types in the set() for each of the turns.  You need to consider 2 things here: what happens if there’s a typo on entering this shit in, and how do you print out the state of the game and the turn history so that the player can make intelligent guesses?  The loop keeps checking that the value for the previous turn’s ruling variable is not set to “no ruling” or whatever you’ll put when no one responded.  Then the game stops and reports the person who made that guess and declares that person the winner.  

Do you want to try to build this with composition and or inheritance? 


Email the guy who wrote learn_python_the_hard_way after this to see what he thinks of your game. 
In gorgons, a scene has a method called enter that does all the work and then returns the result of being in the scene—either death, the next scene name, or finished




Notes on the current state:
11/17: 
This is horrific spaghetti code.  Pretty embarassing.  But I think I'm going to push on to see
if I can get something to work.  If I can get things to run, I might go back and clean things up
a bit, have fewer hardcoded things and just make the flow more elegant.  I recognize that's pretty
bad practice though, and that I probably won't have the appetite to do it.
It'll be important to make it usable, where the state of the game is readable and where if I mistype
something on the 20th turn of a long game, I'm not totally fucked cause my program quits. 
One thing to change is to make sure the program is consistent that n keeps track of which player's turn 
it is, not the turn number.  The turns can be counted by seeing how many of them there are, counter not needed. 
I think I'm running into issues with pointers in my data structure.  Since it's so many different lists,
I think I've got pointers all over the place and I'm editing subsections of the list when I don't mean to be. 
Kind of embarassing because I think it shows just what a noob I am, but I'm pretty sure I need to create classes
for all the components of a clue game.  A "turn" could be a class, for instance.  A "card" is a class.  A "scene" 
could be a class with 3 cards, one of each type.  This would involve completely breaking down the code to start over,
which happened in the mastermind project, but 1) it really needs to happen and 2) I'm kind of curious to learn
how to properly use classes.  I think after this project I need to finish the google code school, then that other
"learn python the hard way" exercises, and then I'll have a better basis for stuff, maybe the crypto puzzles e.g.

Should there be an object called a game?  And every instance of a game has a state, which includes its history?  Then there should be a way of viewing a game where a player can only see a subset of all the information stored in a game.  Does that mean that a player needs to be a class?  And each player has a variable called a strategy that gets employed?  

A game gets created.  It has some constructor parameters, like how the cards are dealt, how many players, what their strategies are.  At the same time the Player object needs to be instantiated with cards for each player and a strategy for that player.  Other classes that need to exist to make the game work: cards, turns, and scenes (combo of 3 types of cards representing a murder).  
To run a game, turns have to be looped through.  Each turn should get saved within an instantiated game somewhere, maybe in a list of turns.  This would be the game history.  
The game should also contain the filtering mechanism for each player.  That way the game can provide players with the filtered game history during their turns.   The game would only need to clean the turnhistory for each player—they submit a request for a turnhistory and their player number (actually, that level of trust should not be on the client side.  The game should know who’s asking and act accordingly) and then the game returns the turnhistory for that player. 
What about responses?  Should there be accusations (which would extend scenes) and responses (that would extend cards)? 
Should strategies be classes? 
Will need functions for inputting a guess/scene/accusation and evaluating it, either via computer or by input from the command line.  

How would you use this play an actual game of Clue in real life though?  You need a subset of what you’re doing, since in real life you only ever see the filtered version.   Your strategy should rank best options, so in case you have other factors that you want to use to overrule your strategy you can look at what’s #2 or #3 best option according to the strategy.  
It might be that a param when instantiating the game class would be to set what kind of game it is-- computer managed or 
done IRL as a player.  I'm not sure how that would work, though, since the game has variables for the solution and 
for all player's cards.  Maybe when instantiating the game, those variables just aren't set?  