# Brute Force Approach
# Time Complexit  - O(n)
# Space Complexit - O(n)

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
    
    def check_palindrome(self):
        if self.head is None:
            return "Linked List is Empty"
        
        values = []
        itr = self.head
        
        while itr:
            values.append(itr.data)
            itr = itr.next
        
        
        return values == values[::-1]

if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(2)
    ll.head.next.next = Node(1)
    ans = ll.display()
    print(ans)
    response = ll.check_palindrome()
    print(response)