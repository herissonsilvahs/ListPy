
class ArrayList():
    data = []
    def __init__(self, array = None):
        if array != None:
            self.data = array

    def append(self, element):
        self.append(element)

    def insert(self, position, element):
        ant = self.data[:position] # break the array in position
        ant.append(element) # add element
        for i in self.data[position:]: # scroll through the rest of array adding the elements
            ant.append(i)
        self.data = ant

    def remove(self, element):
        index = 0
        for item in self.data:
            if item == element:
                self.removeAt(index)
                return item
            index=index+1
        return None

    def removeAt(self, position):
        ant = self.data[:position+1] # cut array in element position
        ant.pop() # remove last element
        for i in self.data[1+position:]: # scroll through the rest of array
            ant.append(i) # add in truncated array
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
