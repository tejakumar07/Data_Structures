# Brute Force Approach to minimize the maximum distance between gas stations

def minimiseMaxDistance(arr, k):
    n = len(arr)
    
    # Track how many gas stations are added between each pair
    inBetween = [0] * (n - 1)
    
    # Add 'k' gas stations
    for gasStation in range(k):
        maxIndex = -1
        maxSection = -1

        # Find the section with the maximum current distance
        for i in range(n - 1):
            diff = arr[i + 1] - arr[i]
            currentSection = diff / (inBetween[i] + 1)
            
            if currentSection > maxSection:
                maxSection = currentSection
                maxIndex = i

        # Add a gas station to the section with max distance
        inBetween[maxIndex] += 1

    # After placing all stations, calculate the maximum distance between stations
    maxDistance = -1
    for i in range(n - 1):
        diff = arr[i + 1] - arr[i]
        currentSection = diff / (inBetween[i] + 1)
        maxDistance = max(maxDistance, currentSection)

    return maxDistance


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    k = 4
    ans = minimiseMaxDistance(arr, k)
    print(ans)
