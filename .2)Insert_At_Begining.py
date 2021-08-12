class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insertBeginning(self, data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def display(self):
        if self.head is None:
            print("The List is empty")
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
L.display()
L.insertBegining(0)
L.display()
