"""
Singly linked list consists of several nodes. Nodes linked to each other

Each node has a data and next. Data has a value in it. Next is beside the data within the node.

Head is at the start of the list (data of the first node)

As iterate through the list, head will traverse along the list to access an element along the list. 

Null/None is the end of the list after the last node terminates the list. 


                            Array                   Linked List
Insertion/Deletion          O(n)                    O(1)


Access Element              O(1)                    O(n)


Contiguous memory?          Yes                     No

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
            
    def append(self, data):
        new_node = Node(data)

        if self.head is None :
            self.head = new_node
            return 
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return
        
        new_node = Node(data)

        new_node.next = prev_node.next 
        prev_node.next = new_node

        

llist = LinkedList()

llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

#llist.prepend("E") #ABCDE 

#print(llist.head.data) #get head of the linked list
#print(llist.head.next.data) #get the data after the head

llist.insert_after_node(llist.head.next, "I") #ABICD



llist.print_list()