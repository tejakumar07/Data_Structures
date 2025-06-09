# Better Solution

def LongestConsecutiveSequence(nums):
    if len(nums) == 0:
        return
    
    nums.sort()
    last_smaller = nums[0]
    count = 1
    length = 1

    for i in range(1, len(nums)):
        if nums[i] == last_smaller:
            continue
        elif nums[i] - 1 == last_smaller:
            count += 1
        else:
            count = 1
       
        length = max(length , count)
        last_smaller = nums[i]
    
    return length
if __name__ == "__main__":
    arr = [100, 102, 100, 101, 101, 4, 3, 2, 3, 2, 1, 1, 1, 2]
    print(LongestConsecutiveSequence(arr))
