
class ArrayList():
    data = []
    lenght = 0
    def __init__(self, array = None):
        if array != None:
            self.data = array

    def append(self, element):
        self.append(element)
        self.lenght = self.lenght + 1

    def insert(self, position, element):
        position = position-1
        ant = self.data[:position]
        ant.append(element)
        for i in self.data[position:]:
            ant.append(i)
        self.data = ant

    def remove(self):
        pass

    def removeAt(self, position):
        pass

    def indexOf(self, element):
        pass

    def size(self):
        pass

    def getElement(self, element):
        pass

    def isEmpty(self):
        pass

    def __str__(self):
        return str(self.data)
