class Solution:
    def integerToRoman(self, num: str):
        values = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]
        roman = ""
        
        for rom, val in reversed(values):
            if num // val:
                count = num // val
                roman += (rom * count)
                num %= val
        
        return roman

if __name__ == "__main__":
    nums = 3749
    teja = Solution()
    print(teja.integerToRoman(nums))