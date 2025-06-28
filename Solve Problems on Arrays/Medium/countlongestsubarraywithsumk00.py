# Brute Force Approach

def sub_array(nums, target):
    count = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sum = 0
            for k in range(i, j+1):
                sum += nums[k]
            if sum == target:
                count += 1
    return count


if __name__ == "__main__":
    arr = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
    print(sub_array(arr, 3))
