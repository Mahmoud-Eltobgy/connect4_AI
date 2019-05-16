ROWS = 6   #ROWS

COLUMNS = 7 #COLUMNS 

PLAYER = 0

AI = 1

EMPTY = 0

PLAYER_PIECE = 1

AI_PIECE = 2

WINDOW_LENGTH = 4






def evaluate_window(window, piece):

	score = 0

	opp_piece = PLAYER_PIECE

	if piece == PLAYER_PIECE:

		opp_piece = AI_PIECE



	if window.count(piece) == 4:

		score += 100

	elif window.count(piece) == 3 and window.count(EMPTY) == 1:

		score += 5

	elif window.count(piece) == 2 and window.count(EMPTY) == 2:

		score += 2



	if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:

		score -= 4



	return score




def utility(board, piece):

	score = 0



	## Score center column

	center_array = [int(i) for i in list(board[:, COLUMNS//2])]

	center_count = center_array.count(piece)

	score += center_count * 3



	## Score Horizontal

	for r in range(ROWS):

		row_array = [int(i) for i in list(board[r,:])]

		for c in range(COLUMNS-3):

			window = row_array[c:c+WINDOW_LENGTH]

			score += evaluate_window(window, piece)



	## Score Vertical

	for c in range(COLUMNS):

		col_array = [int(i) for i in list(board[:,c])]

		for r in range(ROWS-3):

			window = col_array[r:r+WINDOW_LENGTH]

			score += evaluate_window(window, piece)



	## Score posiive sloped diagonal

	for r in range(ROWS-3):

		for c in range(COLUMNS-3):

			window = [board[r+i][c+i] for i in range(WINDOW_LENGTH)]

			score += evaluate_window(window, piece)



	for r in range(ROWS-3):

		for c in range(COLUMNS-3):

			window = [board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]

			score += evaluate_window(window, piece)



	return score
