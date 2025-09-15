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
        
        llstr = ""
        itr = self.head
        
        while itr:
            llstr += str(itr.data) + "--->" if itr.next else str(itr.data)
            itr = itr.next 
        
        return llstr
    
    def sorting_linked_list(self):
        if self.head is None or self.head.next is None:
            return self.head.data
        
        stack = []
        itr = self.head
        
        while itr:
            stack.append(itr.data)
            itr = itr.next 
        
        stack.sort()
        itr = self.head
        
        indx = 0
        while itr:
            itr.data = stack[indx]
            indx += 1
            itr = itr.next 
        
        return self.head.data


if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(12)
    ll.head.next = Node(14)
    ll.head.next.next = Node(9)
    ll.head.next.next.next = Node(4)
    ll.head.next.next.next.next = Node(19)
    ll.head.next.next.next.next.next = Node(6)
    print(ll.display())
    print(ll.sorting_linked_list())
    print(ll.display())