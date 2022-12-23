#update element in the list 
l=[23,43,322,42,1]
l[1]=9
print(l)

#insert an element without deleting an element
l.insert(2,100)
print(l)

#inserts element at last index
l.append(121)
print(l)
n=[23,45]
l.append(n)
print(l)

# extend it is similiar to the append but it works on internal data
# i.e it not forms nested list either puts data in it
n=[23,45]
l.extend(n)
print(l)