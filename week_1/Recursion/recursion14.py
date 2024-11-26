# This code is about Fibonacci Number
# It's a LeetCode Problem
# link : https://leetcode.com/problems/fibonacci-number/description/
def function(n):
    if n == 0:
        return 0
    if n < 2:
        return 1
    return function(n-1)+function(n-2)

if __name__ == "__main__":
    n = int(input("What's N: "))
    print(function(n))