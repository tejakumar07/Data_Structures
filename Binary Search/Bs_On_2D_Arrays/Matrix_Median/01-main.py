# Brute Force Approach

def findMatrixMedian(matrix):
    
    arr = [col for row in matrix for col in row]
    arr.sort()
    n = len(arr)
    
    return arr[n // 2]


if __name__ == "__main__":
    matrix = [[ 1, 5, 7, 9, 11 ],
      [ 2, 3, 4, 8, 9 ],
      [ 4, 11, 14, 19, 20 ],
      [ 6, 10, 22, 99, 100 ],
      [ 7, 15, 17, 24, 28 ]]
    
    ans = findMatrixMedian(matrix)
    print(ans)