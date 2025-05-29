num = [2, 32, 12, 343, 765, 75, 24, 674, 24, 24, 45]

target = int(input("What is the target: "))

length = len(num)

i = 0

while i < length:

    if num[i] == target:
        print("found")
        break
    i+=1

else:
    print("Not Found")

"""
Here’s how the control flow works:

If the while loop runs to completion (i.e., i reaches length in your case), and the loop wasn't interrupted by a break, the else block will run.
If the loop is interrupted by a break (which happens when the target is found), the else block will not execute.
"""
