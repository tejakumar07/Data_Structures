# Optimal Solution
# Using Binary Search
# Same Method for finding Median

from typing import List

def kthElement(a: List, n: int, b: List, m: int, k: int) -> int:
    if n > m:
        return kthElement(b, m, a, n, k)
    low = max(0, k - m)
    high = min(k, n)
    
    while low <= high:
        mid1 = (low + high) // 2
        mid2 = k - mid1
        
        l1 = float("-inf") if mid1 == 0 else a[mid1 - 1]
        r1 = float("inf") if mid1 == n else a[mid1]

        l2 = float("-inf") if mid2 == 0 else b[mid2 - 1]
        r2 = float("inf") if mid2 == m else b[mid2]

        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        elif l1 > r2:
            high = mid1 - 1
        else:
            low = mid1 + 1

if __name__ == "__main__":
    arr1 = [2, 3, 45]
    arr2 = [4, 6, 7, 8]
    k = 4
    n = len(arr1)
    m = len(arr2)
    ans = kthElement(arr1, n, arr2, m, k)
    print(ans)