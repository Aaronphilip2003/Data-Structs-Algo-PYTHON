class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def deleteAtPosition(self, position):
        temp = self.head.next
        prev = self.head
        for i in range(position-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next = None

    def display(self):
        if self.head is None:
            print("The List is Empty")
        else:
            temp = self.head
            while temp:
                if temp.next is not None:
                    print(temp.data, "--->", end=" ")
                    temp = temp.next
                else:
                    print(temp.data)
                    temp = temp.next


L = SingleLinkedList()
n1 = Node(0)
L.head = n1
n2 = Node(10)
L.head.next = n2
n3 = Node(20)
n2.next = n3
L.display()
L.deleteAtPosition(1)
L.display()
