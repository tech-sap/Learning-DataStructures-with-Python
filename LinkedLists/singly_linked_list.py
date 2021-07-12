class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
#Creating a linked list
def CreateNewLinkedList():
    head = None
    data = int(input())
    while data!=0:
        newNode = Node(data)
        if head==None:
            head = newNode
        else:
            ptr = head
            while(ptr.next!=None):
                ptr = ptr.next 
            ptr.next = newNode 
        data = int(input()) 
    return head

#finding length of the linked list
def length(head):
    cnt = 0 
    ptr = head
    while ptr!=None:
        cnt += 1 
        ptr = ptr.next
    return cnt


#adding a node to the linked list
def addNode(length, head, data):  
    return insertNode(head,length+1,data)

#adding a node to front of the linked list
def addFrontNode(head,data):
    return insertNode(head,1,data)


#Inserting a node at a given position
def insertNode(head, pos, data):
    newNode = Node(data)
    ptr = head
    if pos==1:
        newNode.next = head
        head = newNode 
    else:
        pos -= 1
        while pos>1:
            ptr = ptr.next
            pos -= 1
        newNode.next = ptr.next 
        ptr.next = newNode 
    return head
    
#Deletion
#Delete the front node
def deleteFrontNode(head):
    return deleteNode(head,1)

#Delete the last node
def deleteLastNode(head):
    return deleteNode(head,length(head))
    
#Deleting a node at a given position
def deleteNode(head,position):
    ptr = head
    if head != None:
      if position==1:
        head = head.next
      else:
        position -= 1
        while position > 1:
          position -= 1
          ptr = ptr.next
        ptr.next = ptr.next.next
    return head

#displaying a linked lists
#1-->2-->3-->4-->5-->NULL
def displayLinkedList(head):
    print('\nPrinting linked lists')
    ptr = head
    while ptr != None:
        print(ptr.data,'--> ',end='')
        ptr = ptr.next
    print('NULL')
    print()

#Reversal of linked lists
def reverseLinkedList(head):
    ptr = head
    while ptr != None:
        if ptr==head:
            prevNode = head 
            nextNode = ptr.next 
            ptr.next = None 
        else:
            nextNode = ptr.next
            ptr.next = prevNode
            prevNode = ptr

        ptr = nextNode
    head = prevNode 
    return head
    
print('1.Create a new linked list')
print('2.display the linked list')
print('3.Reverse the linked list')
print('4.Add node to end of the linked list')
print('5.Add node to front of the linked list')
print('6.Delete the front node of the linked list')
print('7.Delete the last node of the linked list')
print('8.Delete the node at the given position')
print('9.Insert node at the given position')
print('10.Press \'0\' to exit\n')
try:
    ch = int(input("Enter your choice : "))
except ValueError:
    print('Please enter an interger value!!!')
    ch=  int(input("Enter your choice : "))

head = None
while ch!=0:
    if ch==1:
        head = CreateNewLinkedList()
    elif ch==2:
        displayLinkedList(head)
    elif ch==3:
        head = reverseLinkedList(head)
    elif ch==4:
        data = int(input("Enter the data of the last node : "))
        head = addNode(length(head),head, data)
    elif ch==5:
        data = int(input("Enter the data for the front node : "))
        head = addFrontNode(head,data)
    elif ch==6:
        head = deleteFrontNode(head)
    elif ch==7:
        head = deleteLastNode(head)
    elif ch==8:
        valid = 1
        no_of_elements = length(head)
        while valid:
            pos = int(input("Enter the position of the value : "))
            if pos>0 and pos<=no_of_elements:
                valid = 0
            else:
                print("Please enter the valid position!!!")
        head = deleteNode(head,pos)
    elif ch==9:
        valid = 1
        no_of_elements = length(head)
        while valid:
            pos = int(input("Enter the position of the value : "))
            if pos>0 and pos<=no_of_elements+1:
                valid = 0
            else:
                print("Please enter the valid position!!!")
        data = int(input("Enter the data : "))
        head = insertNode(head,pos,data)
    else:
        print("Please enter a valid choice")
    print()
    print('1.Create a new linked list')
    print('2.display the linked list')
    print('3.Reverse the linked list')
    print('4.Add node to end of the linked list')
    print('5.Add node to front of the linked list')
    print('6.Delete the front node of the linked list')
    print('7.Delete the last node of the linked list')
    print('8.Delete the node at the given position')
    print('9.Insert node at the given position')
    print('10.Press \'0\' to exit\n')
    try:
        ch = int(input("Enter your choice : "))
    except ValueError:
        print('Please enter an interger value!!!')
        ch=  int(input("Enter your choice : "))