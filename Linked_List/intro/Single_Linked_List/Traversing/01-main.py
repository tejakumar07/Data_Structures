# Traversing Linked List

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
    
    def transeverseThing(self):
        count = 0
        iterator = self.head
        while iterator:
            count += 1
            iterator = iterator.next
        print(count)
        

ll = LinkedList()
ll.head = Node(1)
second = Node(3)
third = Node(5)
ll.head.next = second
second.next = third
ll.printThing()
ll.transeverseThing()