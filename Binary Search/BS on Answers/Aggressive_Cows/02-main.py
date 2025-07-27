# Optimal Solution
# Using Binary Search

# Helper function to check if we can place 'cows' in the stalls
# such that the minimum distance between any two cows is at least 'distance'
def canWePlace(stalls, distance, cows):
    n = len(stalls)
    noCows = 1                # Place the first cow in the first stall
    last = stalls[0]          # Track the position of the last placed cow

    # Try placing the rest of the cows
    for i in range(1, n):
        # If the current stall is at least 'distance' away from the last placed cow
        if stalls[i] - last >= distance:
            noCows += 1       # Place another cow
            last = stalls[i]  # Update the position of the last placed cow

        # If we have already placed all cows, return True
        if noCows >= cows:
            return True

    return False              # Could not place all cows with at least 'distance' gap

# Main function to find the largest minimum distance between any two cows
def aggressiveCows(stalls, k):
    n = len(stalls)

    # Sort the stall positions to enable binary search logic
    stalls.sort()

    # Minimum possible distance between cows is 1
    # Maximum possible distance is between the first and last stall
    low = 1
    high = stalls[n - 1] - stalls[0]

    # Binary search to find the largest minimum distance
    while low <= high:
        mid = (low + high) // 2  # Try placing cows with this minimum distance

        # If it's possible to place all cows with at least 'mid' distance
        if canWePlace(stalls, mid, k):
            low = mid + 1        # Try for a bigger minimum distance (move right)
        else:
            high = mid - 1       # Try for a smaller distance (move left)

    # After the loop, 'high' will store the largest minimum distance
    return high


if __name__ == "__main__":
    stalls = [0, 3, 4, 7, 10, 9]
    k = 4
    ans = aggressiveCows(stalls, k)
    print("The maximum possible minimum distance is:", ans)