class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
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

    def deleteAtBeginning(self):
        temp = self.head
        self.head = temp.next
        temp.next = None

    def deleteAtPosition(self, position):
        temp = self.head.next
        prev = self.head
        for i in range(position-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next = None

    def deleteAtEnd(self):
        temp = self.head.next
        prev = self.head
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None

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
L.display()
n = int(input("Enter the Number of Operations to be done:"))
print("1-Insert a element at the beginning of the List:")
print("2-Insert an Element at a Specified Position of the List:")
print("3-Insert an Element at the End of the List:")
print("4-Delete the Element at the Beginning of the List:")
print("5-Delete an Element from a Specified Position of the List:")
print("6-Delete the Element at the End of the List:")
while n != 0:
    choice = int(input("Enter your choice:"))
    if choice == 1:
        element = int(input("Enter the Element to be inserted at the beginning of the list:"))
        L.insertAtBeginning(element)
        L.display()
    elif choice == 2:
        element = int(input("Enter the Element to be inserted at the specified Position in the list:"))
        pos = int(input("Enter the Index number where the Element should be placed:"))
        L.insertAtPosition(element, pos)
        L.display()
    elif choice == 3:
        element = int(input("Enter the Element to be inserted at the end of the List:"))
        L.insertAtEnd(element)
        L.display()
    elif choice == 4:
        L.deleteAtBeginning()
        L.display()
    elif choice == 5:
        pos = int(input("Enter the Index number of the Element to be deleted:"))
        L.deleteAtPosition(pos)
        L.display()
    elif choice == 6:
        L.deleteAtEnd()
        L.display()
    else:
        print("CHOOSE THE CORRECT OPTIONS FROM THE GIVEN MENU !!")

    n -= 1
