# Function to print each letter of the name
def print_T():
    for i in range(5):
        if i == 0:
            print("*" * 5)
        else:
            print("  *  ")

def print_E():
    for i in range(5):
        if i == 0 or i == 4 or i == 2:
            print("*" * 5)
        else:
            print("*")

def print_J():
    for i in range(5):
        if i < 4:
            print("    *")
        else:
            print("*" * 4)

def print_A():
    for i in range(5):
        if i == 0:
            print("  *  ")
        elif i == 1:
            print(" * * ")
        elif i == 2:
            print("*****")
        else:
            print("*   *")

def print_K():
    for i in range(5):
        if i == 0:
            print("*   *")
        elif i == 1:
            print("*  * ")
        elif i == 2:
            print("***  ")
        elif i == 3:
            print("*  * ")
        else:
            print("*   *")

def print_U():
    for i in range(4):
        print("*   *")
    print(" *** ")

def print_M():
    for i in range(5):
        if i == 0:
            print("*   *")
        elif i == 1:
            print("** **")
        elif i == 2:
            print("* * *")
        else:
            print("*   *")

def print_R():
    for i in range(5):
        if i == 0:
            print("**** ")
        elif i == 1:
            print("*   *")
        elif i == 2:
            print("**** ")
        elif i == 3:
            print("*  * ")
        else:
            print("*   *")

# Printing the name "TEJA KUMAR"
print_T()
print()
print_E()
print()
print_J()
print()
print_A()
print()
print_K()
print()
print_U()
print()
print_M()
print()
print_A()
print()
print_R()
