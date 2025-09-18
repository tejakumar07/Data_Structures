class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def display(self, head):
        if head is None:
            return "Linked List is Empty"
        
        itr = head
        llstr = ""

        while itr:
            llstr += str(itr.data) + "--->" if itr.next else str(itr.data)
            itr = itr.next
        
        return llstr

    def find_the_length_of_the_linked_list(self, head):
        count = 0

        itr = head

        while itr:
            count += 1
            itr = itr.next
        
        return count
    
    def collision(self, headA, headB, d):
        while d:
            headA = headA.next
            d -= 1
        
        while headA and headB:
            if headA.data == headB.data:
                return headA.data
            
            headA = headA.next
            headB = headB.next
        
        return None

    def getIntersectionNode(self, head1, head2):
        n1 = self.find_the_length_of_the_linked_list(head1)
        n2 = self.find_the_length_of_the_linked_list(head2)

        if n1 < n2:
            return self.collision(head2, head1, n2 - n1)
        
        else:
            return self.collision(head1, head2, n1 - n2)

if __name__ == "__main__":
    ll = LinkedList()

    shared = Node(12)
    shared.next = Node(14)
    shared.next.next = Node(16)
    shared.next.next.next = Node(18)
    shared.next.next.next.next = Node(20)
    
    l1 = Node(1)
    l1.next = Node(3)
    l1.next.next = Node(5)
    l1.next.next.next = Node(7)
    l1.next.next.next.next = Node(9)

    l2 = Node(2)
    l2.next = Node(4)
    l2.next.next = Node(6)
    l2.next.next.next = Node(8)
    
    l1.next.next.next.next.next = shared
    l2.next.next.next.next = shared

    print("Linked List 1")
    print(ll.display(l1))

    print("Linked List 2")
    print(ll.display(l2))

    print(ll.getIntersectionNode(l1, l2))