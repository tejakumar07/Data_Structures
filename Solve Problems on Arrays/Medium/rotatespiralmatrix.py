def rotate_spiral(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    if n == 0:
        return []
    
    left, top = 0, 0
    right, bottom = m - 1, n - 1
    ans = []

    while left <= right and top <= bottom:
        # Left to Right
        for i in range(left, right + 1):
            ans.append(matrix[top][i])
        top += 1

        # Top to Bottom
        for i in range(top, bottom + 1):
            ans.append(matrix[i][right])
        right -= 1

        # Right to Left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                ans.append(matrix[bottom][i])
            bottom -= 1

        # Bottom to Top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1

    return ans

if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4, 5, 6],
        [20, 21, 22, 23, 24, 7],
        [19, 32, 33, 34, 25, 8],
        [18, 31, 36, 35, 26, 9],
        [17, 30, 29, 28, 27, 10],
        [16, 15, 14, 13, 12, 11]
    ]

    result = rotate_spiral(matrix)
    print("Spiral order:")
    
    print(result)
