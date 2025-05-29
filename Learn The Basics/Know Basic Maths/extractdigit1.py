n = int(input("What's N: "))

digits = []
count = 0

while n > 0:

    temp_digit = n % 10
    n = int(n/10)
    count += 1
    digits.append(temp_digit)

digits.reverse()

for digit in digits:
    print(digit,end=" ")
print("")
print("The No.of Digits are: ",count)