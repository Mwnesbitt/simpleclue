I started this project with a goal similar to that of the mastermind project.  I wanted to simulate the game clue.

The reason I wanted to do this was because I had recently played with friends and 
was terrible at the game-- I knew I wasn't taking advantage of half the information available to me, and I felt that
it was the type of problem perfectly suited to a computer-- remembering and applying a simple algorithm to data.

However, I ran into a serious stumbling block based on my lack of coding knowledge.  Like with the mastermind project,
I tried to record the history of the game with an ever increasingly complicated single variable that kept having things
added to it.  Terrible plan.  I tried to plow on, but what really did me in was that the variable was a list that contained
lists of lists.  When copying that variable to modify it to hide certain parts of it, I would end up copying pointers and
so modification of the copy also modified the variable itself.  That's when I threw in the towel and said I needed to
learn more python.

I started the learn_python_the_hard_way exercises, and got through 45 or so, when it came time that an exercise was to 
use an object-oriented structure to make a game, so I returned to Clue.  I'm pretty happy with how all that went-- I
learned a lot of python and I think I can actually make the game work.



Additional details on the project

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

Another implication fo the automated vs manual is that strategies for the manual side print out several good guesses,
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

I probably should document exactly how the game works.  My old readme file includes my notes, some of which I followed,
others of which I changed, so it would be good to have a documentation of how the whole thing works.