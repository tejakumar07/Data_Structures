# Pascal Triangle
# [
#   [1],
#   [1, 1],
#   [1, 2, 1],
#   [1, 3, 3, 1],
#   [1, 4, 6, 4, 1],
#   [1, 5, 10, 10, 5, 1]
# ]

# 3 - Type of Solutions for the Pascals Triangle

# Type - I Problem

class PascalTriangle:
    def nCr(self, n, r):
        if n < 0 or r < 0:
            return "N and R must be +ve"
        if r > n:
            return 0
        
        result = 1
        for i in range(r):
            result = result * (n - i)
            result = result // (i + 1)
        return result
if __name__ == "__main__":
    teja = PascalTriangle()
    print(teja.nCr(5, 0))
    print(teja.nCr(6, 8))
    print(teja.nCr(12, 5))
    print(teja.nCr(2, 0))
    print(teja.nCr(5, 6))
    print(teja.nCr(8, 9))
    print(teja.nCr(5, 5))
