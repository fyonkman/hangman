Requirements for Hangman app:

1. pip install Flask

To run:

1. Run app.py on the command line.
2. Open 127.0.0.1:5000 in a browser.

To play:

1. Choose difficulty on the home screen.
2. Guess single English letters in the textbox and click "Try Letter".
3. If the letter is contained in the randomly-generated word, that letter will
  be drawn in the appropriate blank(s).
4. If the letter is not in the word, part of the hangman will be drawn.
5. If 10 wrong letters are guessed, the user has lost the game.
6. If the user completes the word before the hangman is completely drawn,
  the user has won the game.
7. Wins and losses are tallied on the game board canvas. If the user clicks
  "Play Again", the wins and losses will be saved. Returning to the main menu
  clears wins and losses.

The class structure for Hangman is as follows:

1. app.py is a Python file which acts as the controller of the app.
  It links the views (game.html and index.html) to the model (model.py).
2. The model is model.py which deals with any logic required in keeping track
  of important information such as correct and incorrect letters, and
  any error messaging to help the user understand what they need to input.
3. The views of Hangman are index.html and game.html. index.html is the welcome
  screen and game.html creates and maintains the gameboard for hangman. These
  files are written in a combination of html/css and JavaScript.

Potential Additions/Improvements:

1. Refresh/back button leads to main menu(PRG architecture?)
2. Button for each letter
3. Streak
4. Sound effects
5. Removal of names from list of words
6. Timer
7. Be able to choose theme of words
8. List out the words that have guessed but are wrong at the bottom
9. Account system to track stats
10. Hints
11. Harder difficulty - multi words
12. Multi-player
