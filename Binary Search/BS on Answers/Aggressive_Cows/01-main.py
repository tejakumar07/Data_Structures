# Brute Force Approach
# Using Linear Search to find the maximum minimum distance between cows

# Helper function to check if we can place all cows with at least 'dist' distance apart
def canWePlace(stalls, dist, cows):
    n = len(stalls)
    cntCow = 1               # Place the first cow in the first stall
    last = stalls[0]         # Position of the last placed cow

    for i in range(1, n):
        if stalls[i] - last >= dist:  # If stall is far enough from last cow
            cntCow += 1               # Place another cow
            last = stalls[i]          # Update last placed position

        if cntCow >= cows:            # If all cows are placed
            return True

    return False  # Not all cows could be placed with at least 'dist' apart

# Main function to compute the maximum minimum distance between cows
def aggressiveCows(stalls, k):
    n = len(stalls)
    stalls.sort()  # Sort stall positions for greedy placement

    limit = stalls[n - 1] - stalls[0]  # Max possible distance (range of stalls)

    # Try all possible distances from 1 to 'limit'
    for i in range(1, limit + 1):
        if not canWePlace(stalls, i, k):  # If cows can't be placed with distance i
            return i - 1  # Return the last successful distance

    return limit  # If all distances work, return the max one

# Only run this block when the script is executed directly (not when imported)
if __name__ == "__main__":
    # Input stall positions and number of cows
    stalls = [0, 3, 4, 7, 10, 9]
    k = 4

    # Function call to find answer
    ans = aggressiveCows(stalls, k)

    # Output the result
    print("The maximum possible minimum distance is:", ans)
