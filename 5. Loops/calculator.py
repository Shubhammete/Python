s='''
   Enter the operation
   Addition +
   Subtraction -
   Multipilcation *
   Division /'''
print(s)
a=int(input("num 1 = "))
b=int(input("num 2 = "))
c=input("Enter Operation")

if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
else:
    print("Enter Valid operator")
    
