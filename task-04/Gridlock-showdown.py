def checkRows(matrix):
    for i in range (0,3):
        if (matrix[i][0]==matrix[i][1]==matrix[i][2] and matrix[i][0]!='.'):
            return matrix[i][0]
    return 0

def checkCols(matrix):
    for i in range(0,3):
        if (matrix[0][i]==matrix[1][i]==matrix[2][i] and matrix[0][i]!='.'):
            return matrix[0][i]
    return 0

def checkDiagonals(matrix):
    for i in range(0,3):
        if (matrix[0][0]==matrix[1][1]==matrix[2][2] and matrix[0][0]!='.'):
            return matrix[0][0]
        elif (matrix[0][2]==matrix[1][1]==matrix[2][0] and matrix[0][2]!='.'):
            return matrix[0][2]
    return 0


x=int(input())
lst = []

for i in range(0,x):
    matrix=[]
    for j in range(0,3):
        str=input()
        lst = list(str)
        matrix.append(lst)
    if (checkRows(matrix)):
        print(checkRows(matrix))
    elif (checkCols(matrix)):
        print(checkCols(matrix))
    elif (checkDiagonals(matrix)):
        print(checkDiagonals(matrix))
    else:
        print("DRAW")