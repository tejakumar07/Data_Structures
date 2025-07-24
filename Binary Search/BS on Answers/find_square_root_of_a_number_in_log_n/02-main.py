# Brute Force Approach

from typing import List


import math
def mySqrt(x: int) -> int:
    x = int(math.sqrt(x))
    return x

if __name__ == "__main__":
    print(mySqrt(25))
    print(mySqrt(36))
    print(mySqrt(29))