# Optimal Approach

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
    
    def find_the_length_of_the_linked_list(self, head):
        
        if head is None:
            return 0
        
        elif head.next is None:
            return 1
        
        count = 0
        itr = head

        while itr:
            count += 1
            itr = itr.next
        
        return count


    def collision_point(self, t1, t2, d):

        while d:
            d -= 1
            t2 = t2.next
        
        while t1 and t2:
            if t1.data != t2.data:
                t1 = t1.next
                t2 = t2.next
            
            return t1.data
        
        return None

    def getIntersectionNode(self, head1, head2):
        n1 = self.find_the_length_of_the_linked_list(head1)
        n2 = self.find_the_length_of_the_linked_list(head2)

        if n1 < n2:
            return self.collision_point(head1, head2, n2 - n1)
        else:
            return self.collision_point(head2, head1, n1 - n2)
        

if __name__ == "__main__":
    ll = LinkedList()
    shared = Node(1)
    shared.next = Node(13)
    shared.next.next = Node(17)
    shared.next.next.next = Node(9)
    shared.next.next.next.next = Node(11)

    l1 = Node(2)
    l1.next = Node(7)
    l1.next.next = Node(4)
    l1.next.next.next = Node(6)
    l1.next.next.next.next = shared

    l2 = Node(23)
    l2.next = Node(54)
    l2.next.next = Node(59)
    l2.next.next.next = Node(55)
    l2.next.next.next.next = shared

    print("First Linked List")
    print(ll.display(l1))
    
    print("Second Linked List")
    print(ll.display(l2))

    print(ll.getIntersectionNode(l1, l2))