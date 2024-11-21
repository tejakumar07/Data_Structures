def digitExctraction(n):
    digits = []
    while n > 0:

        temp_digits = n % 10
        digits.append(temp_digits)
        n = int(n/10)
    
    digits.reverse()

    for digit in digits:
        print(digit,end=" ")



if __name__ == "__main__":
    number = int(input("What's the Number: "))
    digitExctraction(number)
