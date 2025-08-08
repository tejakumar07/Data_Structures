class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        count = 0
        n = len(s)

        for i in range(n - 1):
            if values[s[i]] < values[s[i + 1]]:
                count -= values[s[i]]
            else:
                count += values[s[i]]

        # add the last value
        count += values[s[-1]]
        return count

if __name__ == "__main__":
    s = "MCMXCIV"
    teja = Solution()
    print(teja.romanToInt(s))