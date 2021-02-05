#Linked list programming assignment
#Charlie Irmiger
#add methods for lookup, update_by_value, and update_by_key
class Node:
    def __init__(self, key, value, next_node):
        self.key = key
        self.value = value
        self.next_node = next_node
    def __str__(self):
        return '{}: {}'.format(self.key, self.value)
    
class List:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self, key, value):
        new_node = Node(key, value, None)
        if self.tail:
            self.tail.next_node = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
            
    def write(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next_node

    def lookup(self, key):
        current_node = self.head
        while current_node:
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next_node
        return None

    def update_by_value(self, old_value, new_value):
        #Substitute first occurance of old_value with new_value
        current_node = self.head
        while current_node:
            if current_node.value == old_value:
                current_node.value = new_value
            current_node = current_node.next_node
        return None

    def update_by_key(self, key, new_value):
        current_node = self.head
        while current_node:
            if current_node.key == key:
                current_node.value = new_value
            current_node = current_node.next_node
        return None
            
lista = List()
lista.insert(1, 'one')
lista.insert(3, 'three')
lista.insert(2, 'two')
lista.insert(5, 'five')
lista.insert(4, 'four')
lista.insert(6, 'TARGET')
lista.insert(7, 'KEY7')

print("############################################")
print('Original list:')
lista.write()
print("############################################")
print("Searching for '2' (in list):")
print(lista.lookup(2))
print("Searching for '20' (not in list):")
print(lista.lookup(20))
print("Searching for '6' (in list):")
print(lista.lookup(6))

print("############################################")
print("Updating by value: 'TARGET'")
lista.update_by_value('TARGET', 'replacement1')
lista.write()
print()
print("Updating by value: 'Not in list'")
lista.update_by_value('Not in list', 'replacement2')
lista.write()
print()

print("############################################")
print("Updating by key: 'KEY1' (in list):")
lista.update_by_key(7, 'New Key')
lista.write()
