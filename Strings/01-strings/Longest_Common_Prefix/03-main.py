from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]

                if prefix == "":
                    return ""
        return prefix

if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    teja = Solution()
    ans = teja.longestCommonPrefix(strs)
    print(ans)