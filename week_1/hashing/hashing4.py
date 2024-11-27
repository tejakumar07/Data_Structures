def character_check(c):
    count = 0
    for i in range(len(name)):
        if name[i] == c:
            count += 1
    return count


if __name__ == "__main__":
    name = input("Name: ")
    target = input("Enter the Single target only: ")
    result = character_check(target)
    print(result)