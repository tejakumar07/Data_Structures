# Brute Force Approach

def LeadersInArray(nums):
    members = []
    n = len(nums)

    for i in range(n):
        leader = True
        for j in range(i+1, n):
            if nums[i] < nums[j]:
                leader = False
                break
        
        if leader == True:
            members.append(nums[i])
    
    return members

if __name__ == "__main__":
    arr = [10,22,12,3,0,6]
    print(LeadersInArray(arr))