from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        max_freq = max(freq.values())
        
        
        bucket = [[] for _ in range(max_freq + 1)]

        for ch, count in freq.items():
            bucket[count].append(ch)
        
    
        res = []
        for i in range(max_freq, 0, -1):
            for ch in bucket[i]:
                res.append(ch * i)

        return "".join(res)

if __name__ == "__main__":
    teja = Solution()
    s = "tree"
    print(teja.frequencySort(s))