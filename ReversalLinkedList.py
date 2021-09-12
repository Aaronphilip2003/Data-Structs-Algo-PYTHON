class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SingleLinkedList:
    def __init__(self):
        self.head=None
    
    def insertAtBeginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    
    def insertAtPosition(self,data,position):
        np=Node(data)
        temp=self.head
        for i in range(position-1):
            temp=temp.next
        np.data=data
        np.next=temp.next
        temp.next=np
    
    def insertAtEnd(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
    
    def deleteAtBeginning(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    
    def deleteAtPosition(self,position):
        temp=self.head.next
        prev=self.head
        for i in range(position-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
    
    def deleteAtEnd(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
    
    def reversalLinkedList(self):
        prev=None
        current=self.head
        while current is not None:
             next=current.next
             current.next=prev
             prev=current
             current=next
        self.head=prev

    def display(self):
        if self.head is None:
            print("The Linked List is Empty")
        else:
            temp=self.head
            while temp:
                if temp.next is not None:
                    print(temp.data,"---->",end=" ")
                    temp=temp.next
                else:
                    print(temp.data)
                    temp=temp.next

L=SingleLinkedList()
n1=Node(10)
L.head=n1
n2=Node(20)
L.head.next=n2
L.display()
L.insertAtBeginning(0)
L.display()
L.insertAtPosition(5,1)
L.display()
L.insertAtEnd(30)
L.display()
L.reversalLinkedList()
L.display()
# L.deleteAtBeginning()
# L.display()
# L.deleteAtPosition(2)
# L.display()
# L.deleteAtEnd()
# L.display()