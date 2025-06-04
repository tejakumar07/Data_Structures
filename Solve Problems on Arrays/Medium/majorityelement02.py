# Optimal approach

def MajorityElement(nums):
    element = None
    count = 0

    for num in nums:
        if count == 0:
            count = 1
            element = num
        elif element == num:
            count += 1
        else:
            count = 0

    count = 0
    for num in nums:
        if num == element:
            count += 1
    if count > len(nums) // 2:
        return element
    return -1


if __name__ == "__main__":
    arr = [2, 2, 3, 3, 1, 2, 2]
    print(MajorityElement(arr))
