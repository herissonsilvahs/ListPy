
class Node():
    element=None
    next=None

    def __init__(self, element):
        self.element = element

class LinkedList():
    lenght=0
    head=None

    def __init__(self):
        pass

    def append(self, element):
        node = Node(element)
        current = self.head

        if current == None:
            self.head = node

        current = self.head

        while(current.next):
            current = current.next

        current.next = node
        self.lenght += 1

    def insert(self, position, element):
        pass

    def remove(self, element):
        pass

    def removeAt(self, position):
        pass

    def indexOf(self, element):
        pass

    def size(self):
        return self.lenght

    def getElement(self, position):
        pass

    def isEmpty(self):
        if self.lenght == 0:
            return True
        return False