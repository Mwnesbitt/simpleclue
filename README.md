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