global N
N = int(input("N iin utgiig ogno uu: "))


res = []
board = [["."] * N for i in range(N) ]


def isSafe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == "Q":
            return False
 
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == "Q":
            return False
 
    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1),
                    range(col, -1, -1)):
        if board[i][j] == "Q":
            return False
 
    return True

def backtrack(board, col):
    if col >= N:
        copy = ["".join(row) for row in board]
        res.append(copy)
        return 

    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = "Q"
            
            backtrack(board, col + 1)

            board[i][col] = "."

backtrack(board, 0)
for row in res:
    print(row)