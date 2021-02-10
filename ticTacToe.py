grid = [['_', '_', '_'],
	[' ', ' ', ' '],
	['¯', '¯', '¯']]
global currentPlayer, currentPiece, gameRunning
gameRunning = True
currentPlayer = ""
currentPiece = ""
player1 = ""
player2 = ""

def clearGrid():
	grid[0] = ['_', '_', '_']
	grid[1] = [' ', ' ', ' ']
	grid[2] = ['¯', '¯', '¯']

def displayGrid():
	print("\n   1   2   3 ")
	currentRow = grid[0]
	print("1 _" + currentRow[0] + "_|_" + currentRow[1] +"_|_" + currentRow[2] + "_")
	currentRow = grid[1]
	print("2  " + currentRow[0] + " | " + currentRow[1] + " | " + currentRow[2] + " ")
	currentRow = grid[2]
	print("3 ¯" + currentRow[0] + "¯|¯" + currentRow[1] + "¯|¯" + currentRow[2] + "¯\n")

def initGame():
	clearGrid()
	global player1, player2, currentPlayer, currentPiece
	player1 = input("Enter Player 1's name: ")
	player2 = input("Enter Player 2's name: ")
	currentPlayer = player1
	currentPiece = 'x'

def gamestateCheck():
	#row check
	for row in grid:
		if row[0] == row[1] and row[1] == row[2] and (row[0] == 'x' or row[0] == 'o'):
			gameEnd(False)
	#column check
	for i in range(len(grid[0])):
		if grid[0][i] == grid[1][i] and grid[1][i] == grid[2][i] and (grid[0][i] == 'x' or grid[0][i] == 'o'):
			gameEnd(False)

	#Diagonal Check
	if (grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]) or (grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0]) and (grid[1][1] == 'x' or grid[1][1] == 'o'):
		gameEnd(False)
	
	stillEmptySpace = False
	for row in grid:
		for i in row:
			if i != 'o' and i != 'x':
				stillEmptySpace = True
	if stillEmptySpace == False:
		gameEnd(True)


def gameEnd(isTie):
	displayGrid()

	if isTie:
		print("The Game Resulted in a Tie! No one won")
	else:
		print(currentPlayer + " Won!")
	global gameRunning
	if str(input("Would you like to play again? Y/N: ")).lower() == 'y':
		clearGrid()
		gameRunning = True
		#playerTurn()
	else:
		print("Thanks for playing!")
		gameRunning = False


initGame()

while gameRunning:
	displayGrid()

	print(currentPlayer + "'s turn (" + currentPiece + ")")

	x = int(input("Enter X coordinate: ")) - 1
	y = int(input("Enter Y coordinate: ")) - 1
	if ((x < 3 and y < 3) and (grid[y][x] != 'x' and grid[y][x] != 'o')):
		grid[y][x] = currentPiece
	else:
		while (x >= 3 or y >= 3) or (x <= 0 or y <= 0) or (grid[y][x] == 'x' or grid[y][x] == 'o'):
			displayGrid()
			print("Invalid Input! Try Again")
			x = int(input("Enter X coordinate: ")) - 1
			y = int(input("Enter Y coordinate: ")) - 1
		grid[y][x] = currentPiece
	
	gamestateCheck()
	currentPlayer = (player1, player2)[currentPlayer == player1]
	currentPiece = ('o', 'x')[currentPlayer == player1]
	