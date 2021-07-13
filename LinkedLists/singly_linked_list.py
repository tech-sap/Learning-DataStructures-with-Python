#creating a single node with data field and next field
#which contains reference to the next node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
#Creating a LinkedList class for maintaining everything under name of 
#linked list
class LinkedList:
    def __init__(self):
        self.head = None 
    
    #Creating a linked list
    def createLinkedList(self,data):
        if self.head==None:
            self.head = Node(data) 

    #finding length of the linked list
    def length(self):
        cnt = 0 
        ptr = self.head
        while ptr!=None:
            cnt += 1 
            ptr = ptr.next
        return cnt


    #adding a node to the linked list
    def append(self,data):  
        self.insertNode(self.length()+1,data)

    #adding a node to front of the linked list
    def addFrontNode(self,data):
        self.insertNode(1,data)


    #Inserting a node at a given position
    def insertNode(self, pos, data):
        newNode = Node(data)
        ptr = self.head
        if pos==1:
            newNode.next = ptr
            self.head = newNode 
        else:
            pos -= 1
            while pos>1:
                ptr = ptr.next
                pos -= 1
            newNode.next = ptr.next 
            ptr.next = newNode
    
    #Deletion
    #Delete the front node
    def deleteFrontNode(self):
        self.deleteNode(1)

    #Delete the last node
    def deleteLastNode(self):
        self.deleteNode(self.length())
    
    #Deleting a node at a given position
    def deleteNode(self,position):
        ptr = self.head
        if ptr != None:
            if position==1:
                self.head = ptr.next
            else:
                position -= 1
                while position > 1:
                    position -= 1
                ptr = ptr.next
                ptr.next = ptr.next.next
        else:
            print('Linked list is empty!!!')

    #displaying a linked lists
    #1-->2-->3-->4-->5-->NULL
    def displayLinkedList(self):
        #print('\nPrinting linked lists')
        ptr = self.head
        while ptr != None:
            print(ptr.data,'--> ',end='')
            ptr = ptr.next
        print('NULL')

    #Reversal of linked lists
    def reverseLinkedList(self):
        ptr = self.head
        while ptr != None:
            if ptr==self.head:
                prevNode = ptr 
                nextNode = ptr.next 
                ptr.next = None 
            else:
                nextNode = ptr.next
                ptr.next = prevNode
                prevNode = ptr

            ptr = nextNode
        self.head = prevNode 
    
llist1 = LinkedList() #Linked List 1
llist2 = LinkedList() #Linked List 2

llist1.createLinkedList(10)
llist1.append(20)
llist1.append(30)
#printing Linked list 1
print('Original Linked List')
llist1.displayLinkedList()
#reversing Linked List 1
llist1.reverseLinkedList()
print('Reversed Linked list 1')
llist1.displayLinkedList()
print()

llist2.createLinkedList(50)
llist2.append(60)
llist1.append(70)
#printing Linked list 2
print('Original Linked List')
llist2.displayLinkedList()
#reversing Linked List 2
llist2.reverseLinkedList()
print('Reversed Linked list 2')
llist2.displayLinkedList()
print()