# Brute Force Approach

def findPeakElement(matrix):
    n = len(matrix)
    m = len(matrix[0])
    first = float("-inf")
    ii = jj = -1

    for i in range(n):
        for j in range(m):
            if matrix[i][j] > first:
                first = matrix[i][j]
                ii = i
                jj = j
    return (ii, jj)

if __name__ == "__main__":
    mat = [[1,4],[3,2]]
    print(findPeakElement(mat))