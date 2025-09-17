class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def display(self, head):
        if head is None:
            return ""
        
        itr = head
        llstr = ""

        while itr:
            llstr += str(itr.data) + "--->" if itr.next else str(itr.data)
            itr = itr.next
        
        return llstr

    def getIntersectionNode(self, list1, list2):
        visited = set()

        itr = list1
        while itr:
            visited.add(itr)
            itr = itr.next

        itr = list2
        while itr:
            if itr in visited:
                return itr
            itr = itr.next
        
        return None

if __name__ == "__main__":
    shared = Node(8)
    shared.next = Node(4)
    shared.next.next = Node(5)

    list1 = Node(4)
    list1.next = Node(1)
    list1.next.next = shared

    list2 = Node(5)
    list2.next = Node(6)
    list2.next.next = Node(1)
    list2.next.next.next = shared

    ll = LinkedList()

    print("List 1")
    print(ll.display(list1))
    print("List 2")
    print(ll.display(list2))

    intersection = ll.getIntersectionNode(list1, list2)
    if intersection:
        print("Intersection Node:", intersection.data)
    else:
        print("No intersection")
