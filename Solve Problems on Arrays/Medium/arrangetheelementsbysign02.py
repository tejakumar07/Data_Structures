# Type - II
# Code Studio Model
# If the elements are not equal assign the remaining values as same without
# alterating the order

def ArrangingTheElementsBySign(nums):
    pos = []
    neg = []
    
    for num in nums:
        if num > 0:
            pos.append(num)
        else:
            neg.append(num)
    
    p, n = len(pos), len(neg)
    
    min_length = min(p, n)
    
    i = 0
    
    for j in range(min_length):
        nums[i] = pos[j]
        i+=2
    
    for j in range(min_length, p):
        nums[i] = pos[j]
        i+=1
    for j in range(min_length, n):
        nums[i] = neg[j]
        i+=1
    return nums

if __name__ == "__main__":
    nums = [1, -1, 2, -2, 3, -3, 4]
    print(ArrangingTheElementsBySign(nums))