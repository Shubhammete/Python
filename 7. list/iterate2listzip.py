l = [1,2,3,4,5]
t = [6,7,8,9,0]

for a,b in zip(l,t):
    print(a,b)

print("")

#without zip fxn
q=len(l)
for c in range(q):
    print(l[c],t[c])
