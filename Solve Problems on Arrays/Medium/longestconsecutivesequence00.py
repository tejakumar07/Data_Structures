# Brute Force Approach

def LongestConsecutiveSequence(nums):
    length = 1
    members = []
    for num in nums:
        count = 1
        members = [num]
        while LinearSearch(nums, num+1) == True:
            num += 1
            count += 1
            length = max(length, count)
            members.append(num)
    print(f"The Longest Consecutive Sequence Elements are: {members}")
    return length

def LinearSearch(a, target):
    for num in a:
        if num == target:
            return True
    return False

if __name__ == "__main__":
    arr = [102, 4, 100, 1, 101, 3, 2, 1, 1]
    print(f"The Longest Sequence length is: {LongestConsecutiveSequence(arr)}")