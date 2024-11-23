# This will give you the factors or divisiors for the given number
# This problem is from code 360
# Problem Link: https://www.naukri.com/code360/problems/print-all-divisors-of-a-number_1164188?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_Arrayproblems&leftPanelTabValue=SUBMISSION
def divisiors(n):
    factors = []
    for i in range(1,n+1):
        if n % i == 0:
            factors.append(i)
    return factors

if __name__ == "__main__":
    num = int(input("What's N: "))
    print(divisiors(num))