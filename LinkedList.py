class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
            
    def traverse(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            current = self.head
            while current is not None:
                print(current.data, end=" ")
                current = current.next
            print()
            
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        
    def insert_at_specified_node(self, position, data):
        new_node = Node(data)
        
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        for i in range(1, position - 1):
            # if current is None:
            #     print("Position out of range")
            #     return
            # current = current.next
        
         if current is None:
            print("Position out of range")
            return
        
        new_node.next = current.next
        current.next = new_node
        
    
         
        
    def delete_at_beginning(self):
        if self.head is None:
            print("Linked list is empty, nothing to delete.")
            return

        deleted_node = self.head
        self.head = deleted_node.next
        deleted_node.next = None 
        
        
    def deletion_at_end(self):
        prev = self.head
        a = self.head.next
        while a.next is not None:
            a = a.next  
            prev = prev.next
        prev.next = None 
        
    def deletion_at_perticular_node(self,position):
        prev=self.head
        a=self.head.next
        for i in range(1,position-1):
            a=a.next
            prev=prev.next
            
        prev.next=a.next
        a.next=None    
        

# Creating nodes and linked list
node1 = Node(5)
node2 = Node(10)
node3 = Node(15)
node4 = Node(20)

sll = SingleLinkedList()
sll.head = node1
node1.next = node2
node2.next = node3
node3.next = node4

# Traversing and printing the linked list
print("Original Linked List:")
sll.traverse()
print("\n")

# Inserting a node at the beginning
sll.insert_at_beginning(66)
print("Linked List after inserting at the beginning:")
sll.traverse()

# Inserting a node at the end
sll.insert_at_end(833)
print("Linked List after inserting at the end:")
sll.traverse()

# Inserting a node at a specified position (e.g., position 3)
sll.insert_at_specified_node(3, 25)
print("Linked List after inserting at a specified position:")
sll.traverse()
print("\n")

##deletion
sll.delete_at_beginning()
print("Linked List after deleting the first node:")
sll.traverse()

print("Linked List after deleting the end")
sll.deletion_at_end()
sll.traverse()


sll.deletion_at_perticular_node(3)
print("Linked List after deleting the specif node ")
sll.traverse()