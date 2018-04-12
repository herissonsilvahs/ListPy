
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

    def showHead(self):
        print(self.head.element)