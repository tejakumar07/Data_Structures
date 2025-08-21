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
        iterator = self.head
        while iterator:
            print(iterator.data)
            iterator = iterator.next
    
    def InsertionAtEnd(self):
        