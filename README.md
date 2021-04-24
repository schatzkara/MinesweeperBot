# MinesweeperBot

This project was developed to run with Python 3.9.1

How to Run:
	1. Type "python Driver.py" in the command line using your appropriate python command
	2. You will be prompted to answer the following questions:
		a. "What number of rows and columns would you like?" 
		Type an integer into the command line to continue. 
		Note: We recommend a number less than 7 to be able to see the whole board in the GUI, though our agent can still play on larger boards.
		b. "How many mines would you like out of the _ tiles?" 
		Type an integer into the command line to continue.
		c. "Would you like to use the knowledge-based agent or the random bot? (type "random" or "kba")"
		As stated in the prompt, you must type "random" to use the random bot or "kba" to use our knowledge-based agent.
	3. When the GUI appears, simply click the "Start Game" button to watch the agent play!
	4. When the game is over, a window will pop up stating if the agent won or lost.
	5. Close the GUI window and repeat from step 1.

Description of each File:
	- Board.py: Contains a class representing the game board.
	- Constants.py: Contains a series of constant values that are used througout the whole project. 
	- Driver.py: Contains the main method that runs the entire project together.
	- Graphics.py: Contains everything related to the GUI, including the method that runs the game loop.
	- KBA.py: Contains everything related to the KBA, including the KB setup and maintenance, the inference method, and the method to choose actions.
	- Predicates.py: Contains an enum, which lists the allowable predicates in our lexicon.
	- Rando_Bot.py: Contains the random agent.
	- Rule.py: Contains a class representing a logical rule with an antecendent (lhs) and consequent (rhs).
	- Tile.py: Contains a class representing a tile on the board.
