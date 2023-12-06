boardSize=5

def transpose(arr):
	a=[]
	rows=len(arr)
	cols=len(arr[0])
	for c in range(cols):
		b=[]
		for r in range(rows):
			b.append(arr[r][c])
		a.append(b)
	return a

def line2ints(line, sep):
	return [int(x) for x in line.split(sep) if x!='']

def line2intsBoard(line, sep):
	return [[int(x),0] for x in line.split(sep) if x!='']

def readData(fname):
	boards=[]
	randomNums=[]
	with open(fname) as f:
		lines = f.readlines()
		randomNums=line2ints(lines[0],',')
		numBoards=int(len(lines[1:])/(boardSize+1))
		board=[]
		for l in lines[1:]:
			if len(l)>1:
				board.append(line2intsBoard(l,' '))
				if len(board)==boardSize:
					boards.append(board)
					board=[]

	return randomNums,boards

def markNumber(boards,number):
	for i in range(len(boards)):
		for row in range(boardSize):
			for col in range(boardSize):
				if boards[i][row][col][0]==number:
					boards[i][row][col][1]=1

def checkWin(board):
	for row in board:
		if sum([x[1] for x in row])==boardSize:
			return True
	boardT=transpose(board)
	for row in boardT:
		if sum([x[1] for x in row])==boardSize:
			return True
	return False

def calculateScore(board):
	n=0
	for row in board:
		for col in row:
			if col[1]==0:
				n+=col[0]
	return n

def playTheGame(randomNums,boards):
	scores=[]
	winBoards=[]
	for num in randomNums:
		markNumber(boards, num)
		#print(num, [checkWin(x) for x in boards])
		for b in range(len(boards)):
			if b not in winBoards:
				if checkWin(boards[b]):
					score=num*calculateScore(boards[b])
					scores.append(score)
					winBoards.append(b)
	return scores


randomNums,boards=readData('in.txt')
scores=playTheGame(randomNums, boards)
print(scores[0])
print(scores[-1])