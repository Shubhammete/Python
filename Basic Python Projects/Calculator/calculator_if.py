# Basic calculator using if conditional statement


s='''
   Enter the operation
   Addition +
   Subtraction -
   Multipilcation *
   Division /'''
print(s)
a=int(input("num 1 = "))
b=int(input("num 2 = "))
c=input("Enter Operator = ")
if c=="+":
    print(a+b)
if c=="-":
    print(a-b)
if c=="*":
    print(a*b)
if c=="/":
    print(a/b)
if c!="+" and c!="-" and c!="*" and c!="/":
    print("Enter Valid operator")
