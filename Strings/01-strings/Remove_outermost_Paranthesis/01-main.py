def removeOuterParentheses(s):
    result = []
    count = 0  # balance counter

    for char in s:
        if char == '(':
            if count > 0:
                result.append(char)
            count += 1
        else:  # char == ')'
            count -= 1
            if count > 0:
                result.append(char)

    return ''.join(result)

if __name__ == "__main__":
    s = "(()())(())"
    print(removeOuterParentheses(s))