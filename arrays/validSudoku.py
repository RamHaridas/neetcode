def isValidSudoku(board) -> bool:
    # validate rows
    for i in range(9):
        s = set()
        for j in range(9):
            if board[i][j] in s:
                return False
            elif board[i][j] != '.':
                s.add(board[i][j])
    
    # validate columns
    for i in range(9):
        s = set()
        for j in range(9):
            if board[j][i] in s:
                return False
            elif board[j][i] != '.':
                s.add(board[j][i])

    # validate boxes
    ranges = [(0,0),(0,3),(0,6),
              (3,0),(3,3),(3,6),
              (6,0),(6,3),(6,6)
              ]

    for i, j in ranges:
        s = set()
        for row in range(i, i+3):
            for col in range(j, j+3):
                if board[row][col] in s:
                    return False
                elif board[row][col] != '.':
                    s.add(board[row][col])
    return True



board1 = [["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]]

board2 = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]



isvalid = isValidSudoku(board1)
print(isvalid)