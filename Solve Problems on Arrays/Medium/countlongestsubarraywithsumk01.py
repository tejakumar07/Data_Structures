# Better Solution

def sub_array(nums, target):
    count = 0
    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            if sum == target:
                count += 1
    return count


if __name__ == "__main__":
    arr = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
    print(sub_array(arr, 3))
