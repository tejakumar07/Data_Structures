# This Problem solves GCD and HCF
# Problem Link: https://www.naukri.com/code360/problems/gcd_6557?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_Arrayproblems&leftPanelTabValue=SUBMISSION
n1 = 4
n2 = 12
n1_list = []
n2_list = []

for i in range(1,n1+1):
    if n1%i == 0:
        n1_list.append(i)
print(n1_list)

for i in range(1,n2+1):
    if n2 % i == 0:
        n2_list.append(i)
print(n2_list)

common_elements = list(set(n1_list) & set(n2_list))
print((common_elements))

if common_elements:
    gcd = max(common_elements)
    
print(gcd)
