def remove_duplicates(nums):
    n = len(nums)
    indx = 2

    for i in range(2, n):
        if nums[i] != nums[indx - 2]:
            nums[indx] = nums[i]
            indx += 1
    return indx

if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    print(remove_duplicates(nums))