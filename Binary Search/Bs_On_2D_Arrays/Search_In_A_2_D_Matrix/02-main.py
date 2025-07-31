# Optimal Solution
# Using Binary Search

def binarySearch(nums, target, n):
    low = 0
    high = n - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return False

def searchMatrix(nums, target):
    n = len(matrix)
    m = len(matrix[0])
    
    for i in range(n):
        if matrix[i][0] <= target and target <=matrix[i][m - 1]:
            return binarySearch(matrix[i], target, m)

if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 30
    ans = searchMatrix(matrix, target)
    print(ans)