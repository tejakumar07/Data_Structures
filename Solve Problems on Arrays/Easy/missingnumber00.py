# Brute Force Approach

def MissingNumber(nums, k):
    for i in range(1, k+1):
        if i not in nums:
            return i

if __name__ == "__main__":
    arr =[1,2,3,4,5,6,7,8,9]
    d = 10
    print(MissingNumber(arr, d))
