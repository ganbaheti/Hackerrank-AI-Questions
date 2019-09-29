
def next_move(posr, posc, board):
    spots = []
    for i,row in enumerate(board):
        for j, col in enumerate(row):
            if col == 'd':
                spots.append((i,j))
    nxt = (posr, posc)
    while spots:
        board[nxt[0]][nxt[1]] = '-'
        nxt = min(spots, key=lambda i: abs(posr - i[0] ) + (abs(posc - i[1])))
        vert = posr - nxt[0]
        horiz = posc - nxt[1]
        ups,downs,lefts,rights = 0,0,0,0
      
        if vert > 0:
            ups = vert
        elif vert < 0: 
            downs = abs(vert)
        if horiz > 0: 
            lefts = horiz
        elif horiz < 0: 
            rights = abs(horiz)
        while ups:
            posr -= 1
            ups -= 1 
            print("UP")
        while downs:
            posr += 1
            downs -= 1 
            print("DOWN")
        while lefts:
            posc -= 1
            lefts -=1
            print("LEFT")
        while rights:
            posc += 1
            rights -=1 
            print("RIGHT")
        print("CLEAN")
        board[nxt[0]][nxt[1]] = 'b'
        for x in board:
            for y in x:
                print(y,end='')
            print('\n')
        spots.remove(nxt)


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
