# Using Binary Search

def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    
    n = len(matrix)
    m = len(matrix[0])
    
    low = 0
    high = n * m - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        row, col = mid // m , mid % m
        
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return False

if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 30
    ans = searchMatrix(matrix, target)
    print(ans)