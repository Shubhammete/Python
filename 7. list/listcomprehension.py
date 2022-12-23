# to add 1 to 100 elements in list
l=[]
for i in range(1,101):
    l.append(i)
print(l)
print("")
# method of comprehension
a = [n for n in range(1,101)]
print(a)
print("")
# filter or condition
b=[s for s in range(1,101) if s%2 == 0]
print(b)
print("")
# put string in list 
d = "Shubham"
c =[f for f in d ]
print(c)