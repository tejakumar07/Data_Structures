def SetMatrixToZeros(matrix):
    n = len(martix)
    
    if n == 0:
        return
    
    m = len(martix[0])
    
    row = [0] * n
    col = [0] * m
    
    for i in range(n):
        for j in range(m):
            if martix[i][j] == 0:
                row[i] = 1
                col[j] = 1
    
    for i in range(n):
        for j in range(m):
            if row[i] or col[j]:
                martix[i][j] = 0
    
    return matrix

if __name__ == "__main__":
    martix = [
        [1, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [1, 0, 0, 1]
    ]
    SetMatrixToZeros(martix)
    
    for row in martix:
        print(row)