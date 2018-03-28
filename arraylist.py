
class ArrayList():
    data = []
    def __init__(self, array = None):
        if array != None:
            self.data = array

    def append(self, element):
        self.append(element)

    def insert(self, position, element):
        ant = self.data[:position]
        ant.append(element)
        for i in self.data[position:]:
            ant.append(i)
        self.data = ant

    def remove(self):
        self.data.pop()

    def removeAt(self, position):
        ant = self.data[:position+1]
        ant.pop()
        for i in self.data[1+position:]:
            ant.append(i)
        self.data = ant

    def indexOf(self, element):
        index = 0
        while(index < len(self.data)):
            if(self.data[index] == element):
                return index
            else:
                index = index+1
        return -1

    def size(self):
        return len(self.data)

    def getElement(self, position):
        return self.data[position]

    def isEmpty(self):
        if(len(self.data) > 0):
            return True
        return False

    def __str__(self):
        return str(self.data)
