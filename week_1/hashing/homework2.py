'''
Find the highest/lowest frequency element


Problem Statement: Given an array of size N. Find the highest and lowest frequency element.

Pre-requisite: Hashing Theory and  Counting frequencies of array elements

Examples:

Example 1:
Input: array[] = {10,5,10,15,10,5};
Output: 10 15
Explanation: The frequency of 10 is 3, i.e. the highest and the frequency of 15 is 1 i.e. the lowest.

Example 2:

Input: array[] = {2,2,3,4,4,2};
Output: 2 3
Explanation: The frequency of 2 is 3, i.e. the highest and the frequency of 3 is 1 i.e. the lowest.

'''
# Asked to Solve using 2 Methods

# Method - I (Brute-Force approach(Using two loops):)
def highest_lowest_frequency(arr):
    # Step 1: Create a frequency map using a dictionary
    freq_map = {}
    
    # First loop: Count the frequency of each element
    for num in arr:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1
    
    # Step 2: Initialize variables to keep track of highest and lowest frequencies
    highest_freq = -1
    lowest_freq = float('inf')
    highest_element = None
    lowest_element = None
    
    # Second loop: Traverse the frequency map to find the highest and lowest frequencies
    for num, freq in freq_map.items():
        if freq > highest_freq:
            highest_freq = freq
            highest_element = num
        if freq < lowest_freq:
            lowest_freq = freq
            lowest_element = num

    return highest_element, highest_freq, lowest_element, lowest_freq


# Test the function
arr = [10, 5, 10, 15, 10, 5]
highest, highest_freq, lowest, lowest_freq = highest_lowest_frequency(arr)

print(f"Highest frequency element: {highest} with frequency: {highest_freq}")
print(f"Lowest frequency element: {lowest} with frequency: {lowest_freq}")

