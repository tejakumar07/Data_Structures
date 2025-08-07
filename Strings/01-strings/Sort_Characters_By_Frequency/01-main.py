class Solution:
    def frequencySort(self, s: str) -> str:
        mpp = {}

        for ch in s:
            mpp[ch] = mpp.get(ch, 0) + 1
        ans = sorted(mpp.items(), key = lambda x:x[1], reverse = True)

        result = []
        for ch, freq in ans:
            result.append(ch * freq)
        result = "".join(result)

        return result

if __name__ == "__main__":
    teja = Solution()
    s = "tree"
    print(teja.frequencySort(s))