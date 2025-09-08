# Optimal Approach

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            return "Linked List is Empty"
        
        itr = self.head
        llstr = ""
        
        while itr:
            llstr += str(itr.data) + "--->" if itr.next else str(itr.data)
            itr = itr.next
        
        return llstr

    def oddEvenList(self):
        if self.head is None:
            return "Linked List is empty"
        
        arr = []
        itr = self.head
        
        while itr and itr.next:
            arr.append(itr.data)
            itr = itr.next.next
        
        if itr:
            arr.append(itr.data)
        
        itr = self.head.next
        
        while itr and itr.next:
            arr.append(itr.data)
            itr = itr.next.next
        
        if itr:
            arr.append(itr.data)
            
        i = 0
        itr = self.head
        
        while itr:
            itr.data = arr[i]
            i += 1
            itr = itr.next
        
        return "Operation is Completed please check yourself"
    
if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(2)
    ll.head.next = Node(1)
    ll.head.next.next = Node(3)
    ll.head.next.next.next = Node(5)
    ll.head.next.next.next.next = Node(6)
    ll.head.next.next.next.next.next = Node(4)
    ll.head.next.next.next.next.next.next = Node(7)
    ans = ll.display()
    print(ans)
    response = ll.oddEvenList()
    print(response)
    ans = ll.display()
    print(ans)