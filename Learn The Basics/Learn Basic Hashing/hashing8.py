array = [1,2,4,1]

memory = {}

for num in array:
    if num in memory:
        memory[num] += 1
    else:
        memory[num] = 1

query = [1,4,2]

for number in query:
    print(memory.get(number,0))

'''
How It Works:

for number in query:

Loops through each number in the query list (the numbers you want to find the frequency for).
freq_map.get(number, 0):

Looks up the number in the dictionary freq_map.
If the number exists, it retrieves its frequency.
If the number does not exist, it returns 0 as the default value.
print():

Outputs the result for each queried number.

'''