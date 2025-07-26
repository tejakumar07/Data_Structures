# Optimal Solution
# Using Binary Search

def calculateDays(weights, capacity):
    days = 1
    load = 0
    
    for weight in weights:
        if load + weight > capacity:
            days += 1
            load = weight
        else:
            load += weight
    return days

def shipWithinDays(weights, days):
    n = len(weights)
    maxi = max(weights)
    total_weight = sum(weights)
    low = maxi
    high = total_weight
    
    while low <= high:
        mid = (low + high) // 2
        
        ans = calculateDays(weights, mid)
        
        if ans <= days:
            high = mid - 1
        else:
            low = mid + 1
    
    return low
        
if __name__ == "__main__":
    weights = [1,2,3,4,5,6,7,8,9,10]
    days = 5
    print(shipWithinDays(weights, days))