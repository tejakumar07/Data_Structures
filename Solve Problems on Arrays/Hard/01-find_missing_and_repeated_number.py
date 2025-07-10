# Brute Force Approach

def find_missing_and_repeated(nums, k):
    missing = -1
    repeated = -1
    for i in range(1, k + 1):
        count = 0
        for j in range(k):
            if i == nums[j]:
                count += 1
        if count > 1:
            repeated = i
        elif count == 0:
            missing = i

        if missing != -1 and repeated != -1:
            return [missing, repeated]
        return [-1, -1]


if __name__ == "__main__":
    arr = [4, 3, 6, 2, 1, 1]
    n = 6
    ans = find_missing_and_repeated(arr, n)
    print(ans)
