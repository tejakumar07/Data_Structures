# This is the Basic method for the Counting Digits
def count_digit(n):
    count=0
    while n > 0:
        digit = n % 10
        count += 1
        print(digit)
        n = int(n/10)
    print("The No.of Digits you entered is: ",count)

if __name__ == "__main__":
    number = int(input("Enter the Number: "))
    count_digit(number)