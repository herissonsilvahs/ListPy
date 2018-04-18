from arraylist import ArrayList
from linkedlist import LinkedList

arl = ArrayList([1,2,3,4,5])
lkl = LinkedList()

lkl.append(4)
lkl.append(6)
lkl.append(5)

#lkl.insert(3, 9)

#print(lkl.size())

#lkl.showHead()

lkl.remove(5)

print(lkl.size())

print(lkl.indexOf(4))

element = lkl.getElement(1)

print(element)

rmElement = lkl.removeAt(0)

print(rmElement)
print(lkl.lenght)