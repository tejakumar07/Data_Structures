# Brute Force Approach

from typing import List
def mySqrt(x : int) -> int:
    ans = 1
    for i in range(1, x + 1):
        if i * i <= x:
            ans = i
        else:
            break
    return ans

if __name__ == "__main__":
    print(mySqrt(25))
    print(mySqrt(39))
    print(mySqrt(2147395599))