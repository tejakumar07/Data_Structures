class Solution:
    def checkingBackSpace(self, str, index):
        backSpace = 0

        while index >= 0:

            if str[index] == "#":
                backSpace += 1
            
            elif backSpace > 0:
                backSpace -= 1
            
            else:
                break

            index -= 1
        return index

    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1

        while i >= 0 or j >= 0:
            i = self.checkingBackSpace(s, i)
            j = self.checkingBackSpace(t, j)

            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
                
            elif i >= 0 or j >= 0:
                return False
                
            i -= 1
            j -= 1
        
        return True


if __name__ == "__main__":
    s = "ab#c"
    t = "ad#c"
    teja = Solution()
    print(teja.backspaceCompare(s, t))