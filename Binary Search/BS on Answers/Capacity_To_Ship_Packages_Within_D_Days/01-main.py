# Brute Force Approach

def calculateDays(weights, capacity):
    n = len(weights)
    load  = 0 
    day = 1
    
    for i in range(n):
        if load + weights[i] > capacity:
            day += 1
            load = weights[i]
        else:
            load += weights[i]
    return day

def shipWithinDays(weights, days):
    n = len(weights)
    maxi = max(weights)
    total_sum = sum(weights)
    
    for i in range(maxi, total_sum + 1):
        ans = calculateDays(weights, i)
        if ans <= days:
            return i
    return -1
if __name__ == "__main__":
    weights = [1,2,3,4,5,6,7,8,9,10]
    days = 5
    print(shipWithinDays(weights, days))