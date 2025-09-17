class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def display(self, head):
        if head is None or head.next is None:
            return head
    
        itr = head
        llstr = ""

        while itr:
            llstr += str(itr.data) + "--->" if itr.next else str(itr.data)
            itr = itr.next
        
        return llstr
    
    def sorting(self, head):
        if head is None or head.next is None:
            return head
        
        count0 = count1 = count2 = 0
        itr = head

        while itr:
            if itr.data == 0:
                count0 += 1
            
            elif itr.data == 1:
                count1 += 1
            
            else:
                count2 += 1
            
            itr = itr.next
        
        itr = head

        while itr:
            if count0:
                itr.data = 0
                count0 -= 1
            
            elif count1:
                itr.data = 1
                count1 -= 1
            
            else:
                itr.data = 2
                count2 -= 1
            
            itr = itr.next

if __name__ == "__main__":
    ll = LinkedList()
    head = Node(2)
    head.next = Node(0)
    head.next.next = Node(0)
    head.next.next.next = Node(1)
    head.next.next.next.next = Node(2)
    head.next.next.next.next.next = Node(1)
    print("Orginal Linked List")
    print(ll.display(head))
    print("After Sorting Linked List")
    ll.sorting(head)
    print(ll.display(head))