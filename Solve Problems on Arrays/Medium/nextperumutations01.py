def nextPermutation(nums):
    n = len(nums)
    
    # Step 1: Find the first decreasing element from the end
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    # Step 2: If found, find the number just larger and swap
    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    # Step 3: Reverse the part from i+1 to end
    nums[i + 1:] = reversed(nums[i +1:])

    return nums

if __name__ == "__main__":
    arr = [1,3,5,4,2]
    print(nextPermutation(arr))