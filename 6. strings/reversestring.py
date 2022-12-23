w="Shubham is sweet boy"
# w=w[-1::-1]  instead of second method we can use this but 2nd one is recommend
print(w)
t=len(w)
for a in range(t):
    print(w[a])
#2nd method
print()
for a in range(t-1,-1,-1):
    print(w[a])
print()
# 3rd one those not need range or length  so for reversing we have to reverse it before the loop by w=w[-1::-1] method
for a in w:
    print(a)