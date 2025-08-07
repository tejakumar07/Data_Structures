from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        freq = sorted(freq.items(), key = lambda x:x[1], reverse = True)
        return "".join(ch * count for ch, count in freq)

if __name__ == "__main__":
    teja = Solution()
    s = "tree"
    print(teja.frequencySort(s))