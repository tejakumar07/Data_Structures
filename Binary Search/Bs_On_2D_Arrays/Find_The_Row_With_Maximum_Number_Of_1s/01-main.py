def rowAndMaximumOnes(mat):
    n = len(mat)
    m = len(mat[0])
    maxRows = -1
    maxIndx = -1
    
    for i in range(n):
        currentRows = 0
        for j in range(m):
            currentRows += mat[i][j]
        if currentRows > maxRows:
            maxRows = currentRows
            maxIndx = i
    return [maxIndx, maxRows]
if __name__ == "__main__":
    mat = [[0,1], [1,0], [1, 1]]
    ans  = rowAndMaximumOnes(mat)
    print(ans)
    