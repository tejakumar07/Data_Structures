# Better Solution

def MissingNumber(nums, k):
    freq = {}
    for num in nums:
        freq[num] = 1
    for i in range(1, k+1):
        if i not in freq:
            return i
if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    d = 10
    print(MissingNumber(arr, d))
