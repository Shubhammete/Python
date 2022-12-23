l=[20,30,40,60,10,100]

del l[2]
print(l)
# same as del but shows value at output
a = l.pop(0)
print(a)
print(l)

# remove it deletes element by value
b = l.remove(30) 
print(b)
print(l)

#clear  it clears all the list
l.clear()
print(l)