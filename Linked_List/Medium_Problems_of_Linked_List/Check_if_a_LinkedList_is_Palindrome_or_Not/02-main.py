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

    def reverse_linked_list(self, head):
        if head is None or head.next is None:
            return head
        
        prev = None
        current = head
        
        while current:
            new_node = current.next
            current.next = prev
            prev = current
            current = new_node
        
        return prev

    def check_palindrome(self):
        if self.head is None or self.head.next is None:
            return True
        
        slow = fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        new_head = self.reverse_linked_list(slow.next)
        
        first = self.head
        second = new_head
        
        is_palindrome = True
        while first and second:
            if first.data != second.data:
                is_palindrome = False
                break
            
            first = first.next
            second = second.next
        
        return is_palindrome

if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(2)
    ll.head.next.next = Node(2)
    ll.head.next.next.next = Node(1)
    
    print(ll.display())
    response = ll.check_palindrome()
    print(response)