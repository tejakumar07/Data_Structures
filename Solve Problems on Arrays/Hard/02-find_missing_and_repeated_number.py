def find_missing_and_repeated(nums):
    n = len(nums)
    hash_freq = [0] * (n + 1)
    for i in range(n):
        hash_freq[nums[i]] += 1
    missing, repeated = -1, -1
    for i in range(1, n + 1):
        if hash_freq[i] == 0:
            missing = i
        elif hash_freq[i] == 2:
            repeated = i

        if missing != -1 and repeated != -1:
            print(missing)
            print(repeated)
            break


if __name__ == "__main__":
    a = [3, 1, 2, 5, 4, 6, 7, 5]
    find_missing_and_repeated(a)
