a = input("Enter the statement: ")
print(a)

l = a.split()
print(l)


# For multiple inputs

l=[]
for i in range(1,4):
    n = input("Enter the colour "+str(i)+"- ")
    l.append(n)
print(l)