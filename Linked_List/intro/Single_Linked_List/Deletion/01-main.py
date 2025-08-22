# Deletion

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printThing(self):
        if self.head == None:
            return "Linked List is Empty"
        itr = self.head
        llstr = ""
        
        while itr:
            llstr += str(itr.data) + "----->" if itr.next else str(itr.data)
            itr = itr.next
        return llstr

    def deletion(self, indx):
        if indx == 0:
            self.head = self.head.next
            return
        itr = self.head
        count = 0
        while itr:
            if count == indx - 1:
                itr.next = itr.next.next 
                return
            itr = itr.next 
            count += 1
        print("Index out of Bound")
        
if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(2)
    ll.head.next = Node(4)
    ll.head.next.next = Node(6)
    ll.head.next.next.next = Node(7)
    ll.head.next.next.next.next = Node(8)
    ll.head.next.next.next.next.next = Node(10)
    result = ll.printThing()
    print(result)
    ll.deletion(3)
    result = ll.printThing()
    print(result)