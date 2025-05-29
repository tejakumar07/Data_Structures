def MissingNumber(nums, k):
    hash = [0] * (k+1)
    for num in nums:
        if 1 <= num <= k:
            hash[num] = 1
    for i in range(1, k+1):
        if hash[i] == 0:
            return i

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    d = 10
    print(MissingNumber(arr, d))

