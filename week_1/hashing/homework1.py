'''
Problem statement: Given an array, we have found the number of occurrences of each element in the array.

Examples:

Example 1:
Input: arr[] = {10,5,10,15,10,5};
Output: 10  3
	 5  2
        15  1
Explanation: 10 occurs 3 times in the array
	      5 occurs 2 times in the array
              15 occurs 1 time in the array

Example2: 
Input: arr[] = {2,2,3,4,4,2};
Output: 2  3
	3  1
        4  2
Explanation: 2 occurs 3 times in the array
	     3 occurs 1 time in the array
             4 occurs 2 time in the array
'''

# Same Question

# Method - II

def prestoring_fetching(query):
    memory = {}
    for num in array:
        if num in memory:
            memory[num] += 1
        else:
            memory[num] = 1
    
    for q in query:
        print(memory.get(q,0))
    
if __name__ == "__main__":
    array = [10, 5, 10, 15, 10, 5]
    target = list(map(int,input("Target List: ").split()))
    prestoring_fetching(target)