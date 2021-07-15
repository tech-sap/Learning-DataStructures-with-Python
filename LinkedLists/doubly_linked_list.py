#creating doubly linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None 

class Doubly_Linked_List:
    def __init__(self):
        self.head = None 
    
    #creating the linked list
    def create_list(self,data):
        if self.head==None:
            self.head = Node(data)
        else:
            self.insertnode(self.length(),data)
    
    #finding length of the list
    def length(self):
        ptr = self.head 
        cnt = 0
        while ptr:
            cnt += 1 
            ptr = ptr.next  
        return cnt 
    
    #display the linked list
    def display_list(self,ptr):
        if ptr==None:
            return
        print('{0} <--> '.format(ptr.data),end='')
        self.display_list(ptr.next)
       

    #display the reverse
    def display_reverse_list(self,ptr):
        if ptr.next==None:
            print('{0} <--> ',ptr.data)
            return   
        self.display_list(ptr.next)
        if ptr.prev:
            print('{0} <--> '.format(ptr.prev.data),end='')
        else:
            print('{0} <--> '.format(ptr.data),end='')
    
    #append elements
    def append_list(self,data):
        self.insertnode(self.length(),data)

    #insert at front 
    def frontNode(self, data):
        self.insertnode(1,data)

    #insert the node at the given position
    def insertnode(self,pos,data):
        ptr = self.head  
        index = 1
        newNode = Node(data)
        
        if pos==1:
            newNode.prev = None    
            newNode.next = self.head  
            self.head = newNode  
        else:
            while index<pos and ptr.next:
                ptr = ptr.next 
                index += 1
            newNode.prev = ptr.prev    
            newNode.next = ptr    
            ptr.prev = newNode  
        

llist1 = Doubly_Linked_List()
llist1.create_list(10)
llist1.create_list(20)
llist1.append_list(30)
llist1.append_list(40)
llist1.frontNode(5)
print('The Doubly Linked list  ')
print('        |  ')
print('        |  ')
print('        |  ')
print('     \     /')
print('      \   /')
print('       \ /')
print('        V')
llist1.display_list(llist1.head)
print('NULL')
print('Reversed one')
llist1.display_reverse_list(llist1.head)
print('NULL')