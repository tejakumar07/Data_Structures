# Insertion at Start

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
        llstr = ""
        iterator = self.head

        while iterator:
            llstr += str(iterator.data) + "----->" if iterator.next else str(iterator.data)
            iterator = iterator.next
        print(llstr)
        return
    
    def insertionAtBeginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
    
if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(1)
    second = Node(3)
    third = Node(5)
    fourth = Node(7)
    fifth = Node(9)
    ll.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    ll.printThing()
    ll.insertionAtBeginning(0)
    ll.printThing()
    
        
