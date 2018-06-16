board=['','','','','','','','','','']
def display_board(board):
	print(" 	|	|	")
	print(f"    {board[7]}	|  {board[8]}	|  {board[9]}")
	print(" 	|	|	")
	print("   -------------------")
	print(" 	|	|	")
	print(f"    {board[4]}	|  {board[5]}	|  {board[6]}")
	print(" 	|	|	")
	print("   -------------------")
	print(" 	|	|	")
	print(f"    {board[1]}	|  {board[2]}	|  {board[3]}")
	print(" 	|	|	")

def player_input():
	Step=0
	eo=1
	Player1=input("Player1..Enter Marker X or O? 	")
	if Player1 == 'X':
		Player2='O'
	else:
		Player2='X'

	while Step != 9:

		if(eo%2==1):
			pos=int(input("Player1..Enter Position(1-9)	"))
			if board[pos] != '':
				pos=int(input("Invalid move..Enter again"))
			print('\n'*100)
			eo=0
			place_marker(board,Player1,pos)
			p=win_check(board,Player1)

		else:
			pos=int(input("Player2..Enter Position(1-9)	"))
			if board[pos] != '':
				pos=int(input("Invalid move..Enter again"))
			print('\n'*100)
			eo=1
			place_marker(board,Player2,pos)
			p=win_check(board,Player2)

		if p == 9:
			break
		else:
			Step+=1


def place_marker(board,marker,position):
	board[position]=marker
	display_board(board)

def win_check(board,marker):
	x=win(board,marker)
	if x == True:
		Step=9
		return Step	
	

def win(board,marker):
	b=True
	if board[1] == marker and board[2] == marker and board[3] == marker:
		print(marker + " WINS!! ")
	elif board[4] == marker and board[5] == marker and board[6] == marker:
		print(marker + " WINS!! ")
	elif board[7] == marker and board[8] == marker and board[9] == marker:
		print(marker + " WINS!! ")
	elif board[1] == marker and board[4] == marker and board[7] == marker:
		print(marker + " WINS!! ")
	elif board[2] == marker and board[5] == marker and board[8] == marker:
		print(marker + " WINS!! ")
	elif board[3] == marker and board[6] == marker and board[9] == marker:
		print(marker + " WINS!! ")
	elif board[1] == marker and board[5] == marker and board[9] == marker:
		print(marker + " WINS!! ")
	elif board[3] == marker and board[5] == marker and board[7] == marker:
		print(marker + " WINS!! ")
	else:
		b=False
	return b

ans='Yes'
while ans == 'Yes':
	player_input()
	ans=input("Do you want to replay..?	")
