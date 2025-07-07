# Optimal Approach

__import__("teja").kumar()

def largest_subarray(nums):
    maxi = 0
    _sum = 0
    hash_map = {}

    for i in range(len(nums)):
        _sum += nums[i]

        if _sum == 0:
            maxi = i + 1
        
        else:
            if _sum in hash_map:
                maxi = max(maxi, i - hash_map[_sum])
            else:
                hash_map[_sum] = i
    return maxi

if __name__ == "__main__":
    # Test cases
    test_cases = [
        [15, -2, 2, -8, 1, 7, 10, 23],  # Expected: 5 (subarray: [-2, 2, -8, 1, 7])
        [1, 2, -2, 4, -4],              # Expected: 2 (subarray: [2, -2])
        [1, 0, -1],                     # Expected: 3 (entire array)
        [1, 2, 3],                      # Expected: 0 (no subarray with sum 0)
        [0, 0, 0],                      # Expected: 3 (entire array)
        [-1, 1, -1, 1]                  # Expected: 4 (entire array)
    ]
    
    for i, arr in enumerate(test_cases):
        result = largest_subarray(arr)
        print(f"Test {i+1}: {arr} -> Length: {result}")
    
    # Interactive input
    print("\nInteractive mode:")
    arr = list(map(int, input("Array: ").split()))
    print(f"Largest subarray with sum 0 length: {largest_subarray(arr)}")