def LongestSubArray(nums, k):
    from collections import defaultdict

    hash_map = defaultdict(int)
    hash_map[0] = 1   # empty prefix sum
    curr_sum = 0
    count = 0

    for num in nums:
        curr_sum += num

        if (curr_sum - k) in hash_map:
            count += hash_map[curr_sum - k]

        hash_map[curr_sum] += 1

    return count

if __name__== "__main__":
    arr = [1, 2, 1, 2, 1]
    k = 3
    print(LongestSubArray(arr, k))