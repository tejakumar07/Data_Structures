# Optimal Solution
# Using Binary Search Method

from typing import List
def mySqrt(x: int) -> int:
    ans = 0
    low = 1
    high = x

    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= x:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

if __name__ == "__main__":
    print(mySqrt(25))
    print(mySqrt(543))