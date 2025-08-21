# Insertion at the end
# Here the Insertion at the end had two cases

'''
1) The Linked List might empty
2) Or it might had an elements
   In second case we need to traverse the entire the linked list and then we insert at the end
'''

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
        itr = self.head
        
        while itr:
            llstr += str(itr.data) + "----->" if itr.next else str(itr.data)
            itr = itr.next 
        print(llstr)
    
    def insertionAtEnd(self, data):
        if self.head == None:
            self.head = Node(data)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)
        return

if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(21)
    second = Node(16)
    third = Node(99)
    fourth = Node(80)
    ll.head.next = second
    second.next = third
    third.next = fourth
    ll.printThing()
    ll.insertionAtEnd(1)
    ll.printThing()