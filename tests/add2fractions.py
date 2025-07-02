# Problem Statement:
# Take two fractions as strings in the form "a/b" and "c/d" where a, b, c, and d are positive integers and b ≠ 0, d ≠ 0.
#
#
#
# Your task is to add the two fractions and print their sum in the simplest form as a string x/y.
#
# Examples:
# Input:
# 3/4
# 1/7
#
# Output:
#  25/28
#
# Explanation: 3/4 + 1/7 = (3×7 + 1×4)/(4×7) = 25/28
#
# Input:
# 5/2
# 1/2
#
# Output:
# 3/1
#
# Explanation: 5/2 + 1/2 = 6/2 = 3/1
#
# Constraints:
# The inputs frac1 and frac2 are valid strings in the form "a/b" where 1 ≤ a, b ≤ 104
# The final answer must be fully simplified

import math
A = input()
C = input()

a, b = A.split("/")
c, d = C.split("/")

a = int(a)
b = int(b)
c = int(c)
d = int(d)

num = ((a * d) + (b * c))
den = (b * d)

jonsnow = math.gcd(num, den)

num //= jonsnow
den //= jonsnow
print(f"{num}/{den}")