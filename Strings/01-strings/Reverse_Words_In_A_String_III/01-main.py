def ReverseWords(str):
    words = str.split()
    words = [word[::-1] for word in words]
    str = " ".join(words)
    
    return str

if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    ans = ReverseWords(s)
    print(ans)