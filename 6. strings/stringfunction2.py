w="Welcome"
e="Welcome123"
n="12345654"
#find
print(w.find("e"))
print(w.find("el"))
print(w.find("e",2)) # from 2nd index i.e from l
print()
#index
print(w.index("c"))
#find and index are same but find gives -1 if string not found but index gives error

#isalpha()  gives true if all elements in string is alphabets
print(w.isalpha())
print(e.isalpha())
print(n.isalpha())
print()

#isdigit()
print(w.isdigit())
print(e.isdigit())
print(n.isdigit())
print()

#isalnum()
print(w.isalnum())
print(e.isalnum())
print(n.isalnum())

#note space is counted as character in string