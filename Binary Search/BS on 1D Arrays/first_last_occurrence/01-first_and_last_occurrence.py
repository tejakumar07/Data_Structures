# Brute Force Approach
# Using Liner Search
# But O(n) Time Complexity


def first_and_last_occurence(nums, X):
    n = len(nums)
    first = -1
    second = -1

    for i in range(n):
        if nums[i] == X and first == -1:
            first = i
            second = i
        elif nums[i] == X and first != -1:
            second = i
    return [first, second]

if __name__ == "__main__":
    arr = [5,7,7,8,8,10]
    target = 8
    ans = first_and_last_occurence(arr, target)
    print(ans)
