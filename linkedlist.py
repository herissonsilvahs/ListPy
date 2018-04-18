from node import Node

class LinkedList():
    lenght=0
    head=None

    def __init__(self):
        pass

    def append(self, element):
        node = Node(element)

        if self.head == None: # if first element
            self.head = node
        else: # if existing some element
            current = self.head
            while(current.next):
                current = current.next

            current.next = node
        self.lenght += 1

    def insert(self, position, element):
        if position >= 0 and position <= self.lenght-1:
            node = Node(element)
            current = self.head
            if position == 0:
                node.next = current
                self.head = node
            else:
                pos = 0
                while(pos < position):
                    current = current.next
                    pos+=1
                node.next = current.next
                current.next = node

            self.lenght += 1

    def remove(self, element):
        indice = self.indexOf(element)
        return self.removeAt(indice)

    def removeAt(self, position):
        indice = 0
        current = self.head
        prev = None

        if(position == 0):
            self.head = current.next
            self.lenght -= 1
            return current.element

        prev = current
        current = current.next
        indice += 1

        while(current):
            prev = current
            current = current.next
            indice += 1
            if indice == position:
                prev.next = current.next
                self.lenght -= 1
                current.next = None
                return current.element

        return None

    def indexOf(self, element):
        if self.head.element == element:
            return 0

        current = self.head
        indice=0
        while(current):
            if current.element == element:
                return indice
            indice+=1
            current = current.next

        return -1

    def size(self):
        return self.lenght

    def getElement(self, position):
        current = self.head
        indice=0

        while(current):
            if position == indice:
                return current.element
            current = current.next
            indice+=1
        
        return False

    def isEmpty(self):
        if self.lenght == 0:
            return True
        return False
