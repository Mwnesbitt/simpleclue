SUMMARY
This project is meant to assist a person who is playing a game of clue.  It allows the user to type in the action in the game,
and plays back the action and organizes facts about the game during the user's turn to allow the user to make intelligent actions.

CODE IMPROVEMENTS/ISSUES
The current state is an MVP.  The code should run with no errors provided that the user doesn't input out of bounds values,
although I haven't tested it as extensively as I would like.  It also doesn't provide quite the level of sophistication in
its support for the user as I initially hoped, but I didn't want to get bogged down with sophisticated strategies before
I had a soup to nuts working code.  I've outlined the most important improvements below:

1. The MapRefinement class can be improved.  I'm concerned that I'm leaving information on the table both in the creation of 
   the "known" map and especially in the creation of the "inferrred" map.  Come up with some scenarios where outside of the program
   you know that certain information can be concluded and check that the program is capturing those deductions. Read online to 
   get good strategies.  Think about making a while loop that performs internal checks on the map-- what can it learn from itself?
   Once you've done the "matrix" work, go back through turnByTurn (maybe beef the method itself up), Loop through the turns and 
   see what else you learn from the turn now that the map has been updated.  Terminate the while loop if the map after the while 
   loop is the same as the map before it.  You could also consider different strategies-- right now only MapRefinement exists, but 
   if there are other high-level strategies (not just approaches within MapRefinement, but a strategy that doesn't rely on attempting
   to create a map of where all the cards are) then you may want to create a class Strategy with some functions and have MapRefinement
   and any other high-level strategies inherit from Strategy.
2. Ranking cards.  Right now the MVP only provides the user with a Map of where known cards are and inferences on where cards 
   might be.  The code should translate this into a print out of each of the 3 types of  cards and the user's best guess for each.
   This would rely on ideas such as a card with a high weight on being in a certain location is assumed to be in that location and 
   is deprioritized.
3. Confirming user input.  The implementation of this is cloogy, especially inside of a turn.  The user has to confirm the scene 
   twice-- if the user rejects the second confirmation the whole turn gets restarted.  The whole process needs a review-- when a 
   turn is confirmed it should be a) improved for when there was no accusation and b) if the user does not confirm the player that 
   responded the user should not be asked to input the scene again.  
4. Code review.  I don't think the code has any runtime bugs but I'm not as sure as I should be.  I'd like to feel like the code
   isn't fragile, but I don't feel that way just yet.  I also need to look for duplicated code (printing lists, some noted in 
   the comments, spend some time looking through to think about how you can simplify and group/condense things into their proper 
   logical groups.
5. Best practices:  I'm sure I had a bunch of poor practices.  I'd like to get a better sense of how a professional developer
   would have written this.  For example, I don't think the way cards are handled is a best practice.  It was cumbersome and 
   inelegant when writing the code.   This is a similar to-do item to #4. 
6. OPTIONAL: Have the game to print out its state to a file and  load a state from a properly formatted file.  This would allow 
   putting the entire code in a try-catch that prints to the file if an exception is encountered so you can more easily detect
   issues.  You could also correct the bad data inside the file and reload the game from that file to resume play.  (Storing all
   variables in class Game should probably be sufficient)
7. OPTIONAL: Guide the user better in inputting.  Reprompt when the user inputs something out of bounds?  (E.g., When an accusation 
   is disproven, once the user says what card type disproved it, then the game should know what the actual card was and not prompt 
   the user to type in the card name.
8. OPTIONAL: Running this not through the command line.


BACKGROUND
I did this project to practice with classes in python.  I originally didn't know about classes and ran into serious trouble,
so I put it on the back burner while I went through the learn python the hard way online exercise set, until I encountered ex45,
which required the student to make a game with classes.  I realized it was the perfect way to return to the project and do it properly.

My original goal was similar to that of the mastermind project-- to simulate a game, in this case, clue.  However, I later refined
the scope to be what would better be termed a "clue assistant" that a player in a game of clue can use to help track the
game and make optimal guesses.  I decided not to rename the project so that I wouldn't have two directories running around 
on github, confusing my page.

I had the idea for the project when I  played clue with friends and 
was terrible at the game-- I knew I wasn't taking advantage of half the information available to me, and I felt that
it was the type of problem perfectly suited to a computer-- remembering and applying a simple algorithm to data.

However, I confused that goal with the goal of the mastermind project-- to simulate a game.  So when I initially started,
I was trying to juggle two goals at the same time, which resulted in a far more complex project, especially because I 
hadn't really realized that I was attempting to pursue  two goals.  Once I realized this, I removed all parts of the 
oode that were meant to support the actual running of a game.  I also initally ran into a serious stumbling block based 
on my lack of coding knowledge.  Like with the mastermind project,
I tried to record the history of the game with an ever increasingly complicated single variable that kept having things
added to it.  Terrible plan.  I tried to plow on, but what really did me in was that the variable was a list that contained
lists of lists.  When copying that variable to modify it, I would end up copying pointers and
so modification of the copy also modified the variable itself.  That's when I threw in the towel and said I needed to
learn more python.  So I backburnered the project while going through the learn python the hard way exercises, and returned
to it to complete ex45.

I'm pretty happy with how all that went-- I learned a lot of python and I think I've actually made a decent clue assistant.



Old descriptions of the project:

I simplified Clue to where there's no gameboard or pieces.  The game just assumes that
the players go around in a circle making their guesses, but does allow for a player to skip their guess.  This 
makes the program useful to use when playing an actual game, so if a person doesn't enter into a room on that turn,
it doesn't break the program.  The reason for this simplification is because the game gets a lot
harder if you can observe what rooms your opponents choose and eschew.  There's an element of bluffing and 
reading a bluff there that I don't want to get into here.  (There's also an element of bluffing and reading 
a bluff when it comes to the guesses they make.  I'll have to see how that goes-- I might make simple use of that 
information (thus, in a way that might be gamed), but I'm not sure. 

I envisioned this repository being structured similarly to the mastermind repository, but I had to revamp the project's
structure when I realized I needed objects.  

Automated vs manual game.  Goal is to design it so I can use it while playing (includes an imperative to allow
the user to make typos.)  Thus, I haven't worked on the automated side, where strategies feed guesses directly
to the game engine and I could run 1000 games of clue just like with mastermind.py.  That might be an interesting 
way to develop the code further.  A part of this automated vs manual game is what uncovered my original string 
pointer issue-- the need for there to be a central game with full information that then selectively reveals that
information as a way of keeping track of what each player knows.  I've kind of sidestepped that issue with the new 
implementation because I focused on the manual track.  I think the structure would make automating the game 
possible without any kind of major code restructuring, but that was outside of the scope that I was really trying
to accomplish, so I'm not totally sure.  (This issue is often described as "global" vs "local" knowledge in your notes,
and also as "cleaning" this history in the old implementation.)

Another implication of the automated vs manual is that strategies for the manual side print out several good guesses,
ranked in an order. This way the user can type them in, and the user can also overrule a guess if he/she has a hunch
about what's right or wrong (see above about bluffing.)

I'm also sure there are better ways to implement things.  I think my class structure is pretty decent-- it maps
to the logical elements of the game well and it gets the job done, but I'm sure there are changes I could make,
including adding additional classes and changing inheritance and other things.  (For example, I have Turns, Scenes, and Strategies
extending the class Game.  These do not have a is-a relationship with Game, so I don't think it's a best practice inheritance, but I
needed access to variables in the Game class to reference with Turns, Scenes, and Strategies, so I went ahead and did it.  I think
there could also be improvements to how cards are handled-- maybe a class with some methods to access card data.  Take a
look at the section of the code where the user has to type in a card-- there's repeated code there and it takes
waay too long to get user input on something so simple.  So I think there's definitely room for improvement there.)