# Brute Force Approach
def LongestSubArray(arr, k):
    length = 0
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            total_sum = 0
            for l in range(i, j+1):
                total_sum += arr[l]
            if total_sum == k:
                length = max(length, j-i+1)
    return length


if __name__ == "__main__":
    arr = [1,2,3,1,1,1,1,4,2,3]
    k = 3
    print(LongestSubArray(arr, k))
