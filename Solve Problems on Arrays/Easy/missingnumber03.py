# Optimal Solution - I

def MissingNumber(nums, k):
    total_sum = k * (k+1) // 2
    array_sum = sum(nums)
    return total_sum - array_sum


if __name__ == "__main__":
    arr =[1,2,3,4,5,6,7,8,9]
    d = 10
    print(MissingNumber(arr, d))
