# Optimal Approach

def LeadersInArray(nums):
    n = len(nums)
    maxi = float("-inf")
    members = []
    i = n - 1

    while i >= 0:
        if nums[i] < maxi:
            i-=1
        else:
            members.append(nums[i])
            maxi = max(maxi, nums[i])
            i-=1
    return members

if __name__ == "__main__":
    arr = [10,22,12,3,0,6]
    print(LeadersInArray(arr))