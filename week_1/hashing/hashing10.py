def main():
    name = "abracadabra"
    memory = {}

    for char in name:
        if char in memory:
            memory[char] += 1
        else:
            memory[char] = 1
    query = ['a','s','t','z','b']

    for character in query:
        print(f"The {character} is repeated in {memory.get(character,0)}")

if __name__ == "__main__":
    main()

'''
1. Ordered Map in Python
In Python, starting from version 3.7, the regular dict maintains insertion order by default. This is similar to an ordered map.
dict keeps the order of characters as they first appear in the string.


2. Unordered Map in Python
Python doesn’t have a direct unordered map, but for hashing purposes, we don’t care about the order.
The regular dict behaves like an unordered map if you’re only using it for lookups and counts.

Explanation:
Here, dict is being used for quick lookups without worrying about order.
The .get(char, 0) method ensures that if a character isn’t found, it defaults to 0.

'''