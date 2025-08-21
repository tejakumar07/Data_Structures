# Basic LinkedList
# Creating Single Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printThing(self):
        if self.head == None:
            print("Linked List is Empty")
            return
        
        iterator = self.head
        llstr = ""
        while iterator:
            llstr += str(iterator.data) + "----->" if (iterator.next) else str(iterator.data)
            iterator = iterator.next
        print(llstr)
        return

if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(1)
    second = Node(3)
    ll.head.next = second
    third = Node(5)
    fourth = Node(7)
    fifth = Node(9)
    second.next = third
    third.next = fourth
    fourth.next = fifth
    ll.printThing()