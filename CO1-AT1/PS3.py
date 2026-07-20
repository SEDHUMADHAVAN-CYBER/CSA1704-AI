N = 8
#Backtracking Search
#Constraint Satisfaction Problem (CSP)

#Backtracking
#Constraint Satisfaction Problem (CSP)
#State Space Search
board = [-1] * N

def safe(row, col):
    for i in range(col):
        if board[i] == row or abs(board[i]-row) == abs(i-col):
            return False
    return True

def solve(col):
    if col == N:
        return True

    for row in range(N):

        if safe(row, col):

            board[col] = row

            if solve(col+1):
                return True

            board[col] = -1

    return False

if solve(0):
    print("Solution:")
    for c in range(N):
        print("Column", c, "Row", board[c])
else:
    print("No Solution")