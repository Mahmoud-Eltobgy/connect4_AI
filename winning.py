def winning (board,userid):
    win = False
    if (userid==1):

        #Horizontal
        for y in range(6):
            for x in range(4):
                if (board[y][x]==1):
                    
                    if (board[y][x]==board[y][x+1]==board[y][x+2]==board[y][x+3]):
                        win= True
                        return win 

        #Vertical
        for x in range(7):
            for y in range(3):
                if (board[y][x]==1):
                    
                    if (board[y][x]==board[y+1][x]==board[y+2][x]==board[y+3][x]):
                        win= True
                        return win
        #Diagonally
        for x in range (5,0,-1):
            for y in range(6,0,-1):

                if (board[x][y] == board[x-1][y-1] == board[x-2][y-2] == board[x-3][y-3]== 1):
                    win= True
                    return win

        for x in range(5,0,-1):
            for y in range(4):
                if (board[x][y]==board[x-1][y+1]== board[x-2][y+2] == board[x-3][y+3]==1):
                    win= True
                    return win

    elif (userid==2):

        #Horizontal
        for y in range(6):
            for x in range(4):
                if (board[y][x]==2):
                    
                    if (board[y][x]==board[y][x+1]==board[y][x+2]==board[y][x+3]):
                        win= True
                        return win 

        #Vertical
        for x in range(7):
            for y in range(3):
                if (board[y][x]==2):
                    
                    if (board[y][x]==board[y+1][x]==board[y+2][x]==board[y+3][x]):
                        win= True
                        return win
        #Diagonally
        for x in range (5,0,-1):
            for y in range(6,0,-1):

                if (board[x][y] == board[x-1][y-1] == board[x-2][y-2] == board[x-3][y-3]== 2):
                    win= True
                    return win

        for x in range(5,0,-1):
            for y in range(4):
                if (board[x][y]==board[x-1][y+1]== board[x-2][y+2] == board[x-3][y+3]==2):
                    win= True
                    return win
