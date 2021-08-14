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

    def insertAtPosition(self, data, position):
        np = Node(data)
        temp = self.head
        for i in range(position-1):
            temp = temp.next
        np.data = data
        np.next = temp.next
        temp.next = np

    def insertAtEnd(self, data):
        ne = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne

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
L.display()

n = int(input("Enter the number of new elements to be added to the list:"))
print("1-Insert Element at the beginning of the List")
print("2-Insert Element at the end of the List")
print("3-Insert Element at a specified position in the List")
while n != 0:
    choice = int(input("Enter your Choice:"))
    if choice == 1:
        element = int(input("Enter the element to be inserted at the beginning:"))
        L.insertBeginning(element)
        L.display()
    elif choice == 2:
        element = int(input("Enter the element to be inserted at the end:"))
        L.insertAtEnd(element)
        L.display()
    elif choice == 3:
        element = int(input("Enter the element to be inserted at the specified position:"))
        posn = int(input("Enter the position to insert the element:"))
        L.insertAtPosition(element, posn)
        L.display()
    else:
        print("Enter the correct option")

    n -= 1
