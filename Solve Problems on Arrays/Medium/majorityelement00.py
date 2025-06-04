# Brute Force Approach

def MajorityElement(nums):
    n = len(nums) // 2

    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                count += 1
        if count > n:
            return nums[i]
    return -1


if __name__ == "__main__":
    arr = [2, 2, 3, 3, 1, 2, 2]
    print(MajorityElement(arr))