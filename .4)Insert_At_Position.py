class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insertAtPosition(self, position, data):
        np = Node(data)
        temp = self.head
        for i in range(position-1):
            temp = temp.next
        np.data = data
        np.next = temp.next
        temp.next = np

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
n1 = Node(10)
L.head = n1
n2 = Node(20)
L.head.next = n2
n3 = Node(30)
n2.next = n3
n4 = Node(40)
n3.next = n4
L.insertAtPosition(2, 25)
L.display()
