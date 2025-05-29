# This Program is about the Prime Number or Not
# The Problem Link: https://www.naukri.com/code360/problems/check-prime_624674?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_Arrayproblems&leftPanelTabValue=SUBMISSION
import math
def check_prime(num):
    count = 0
    
    for i in range(1,int(math.sqrt(num)+1)):
        if num % i ==0:
            count+=1
            if (num//i != i ):
                count+=1
    
    if count ==2:
        return True
    else: return False

if __name__ == "__main__":
    num = int(input("What's N: "))
    print(check_prime(num))