'''Implementation of Linked List'''

#Defining class Node
class Node:
    
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return str(self.value)


#Defining class LinkedList 
class LinkedList:
    
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple_nodes(values)
            
    def __str__(self):
        return ' -> '.join([str(node) for node in self])
    
    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
            
    @property
    def values(self):
        return [node.value for node in self]
    
    def display(self):
        return [node.value for node in self]
    
    def add_node(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail
    
    def add_multiple_nodes(self, values):
        for value in values:
            self.add_node(value)
            
    def add_node_as_head(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        return self.head

    def deleteNode(self, key): 
        temp = self.head 
        if (temp is not None): 
            if (temp.value == key): 
                self.head = temp.next
                temp = None
                return
        while(temp is not None): 
            if temp.value == key: 
                break
            prev = temp 
            temp = temp.next
        if(temp == None): 
            return
        prev.next = temp.next
        temp = None
    
    def find(self, value: int) -> bool:
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False
