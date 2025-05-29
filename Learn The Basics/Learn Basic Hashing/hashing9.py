def main():
    array = list(map(int,input("Array: ").split()))
    memory = {}

    for num in array:
        if num in memory:
            memory[num] += 1
        else:
            memory[num] = 1
    query = list(map(int,input("Query: ").split()))
    for number in query:
        print(f" frequency {number} is {memory.get(number,0)}")
if __name__ == "__main__":
    main()