def reverse_word(word):
    chars = list(word)
    i, j = 0, len(chars) - 1
    while i < j:
        chars[i], chars[j] = chars[j], chars[i]
        i += 1
        j -= 1
    return ''.join(chars)

if __name__ == "__main__":
    
    s = "Let's code DSA"
    words = s.split()
    rev = [reverse_word(w) for w in words]
    result = " ".join(rev)
    print(result)
