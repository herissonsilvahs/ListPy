from arraylist import ArrayList

arl = ArrayList([1,2,3,4,5])

arl.insert(0, 4)

print(arl)

print("Posicao do elemento 5:")

print(arl.indexOf(5))

arl.removeAt(1)

print(arl)

print(arl.indexOf(5))