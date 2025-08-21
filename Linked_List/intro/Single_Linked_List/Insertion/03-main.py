# Insertion at middle
# Two cases similar to last problem

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
        llstr = ""
        itr = self.head
        while itr:
            llstr += str(itr.data) + "--->" if itr.next else str(itr.data)
            itr = itr.next
        return llstr
    
    def InsertionAtMiddle(self, indx, data):
        if indx == 0:
            node = Node(data)
            node.next = self.head
            self.head = node
            return
        cnt = 0
        itr = self.head
        while itr:
            if cnt == indx - 1:
                node = Node(data)
                node.next = itr.next
                itr.next = node
                return
            itr = itr.next
            cnt += 1
        print("Index out of Range")

if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(2)
    ll.head.next.next = Node(3)
    ll.head.next.next.next = Node(5)
    ll.head.next.next.next.next = Node(6)
    ll.head.next.next.next.next.next = Node(7)
    ll.head.next.next.next.next.next.next = Node(8)
    ll.head.next.next.next.next.next.next.next = Node(9)
    ll.head.next.next.next.next.next.next.next.next = Node(10)
    response = ll.printThing()
    print(response)
    ll.InsertionAtMiddle(3, 4)
    response = ll.printThing()
    print(response)