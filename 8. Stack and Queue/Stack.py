l = []
while True:
    c = print('''
               1 Push element
               2 Pop Element
               3 Peek Element
               4 Display Stack
               5 Exit
               ''')
    a = int(input("Enter Your choice: "))
    if a == 1:
       b=input("Enter the value: ")
       l.append(b)
       print(b,"Added succesfully")
       print(l)
    elif a == 2 :
        if len(l)==0:
           print("Stack is empty")
        else:
           p=l.pop()  #here p is variable in which popped element is stored
           print(p,"Deleted Sucessfully")
           print(l)
    elif a == 3:
        if len(l)==0:
           print("stack is empty")
        else:
            print("Last stack value is: ",l[-1])
    elif a == 4:
        print("The stack is: ",l)
    elif a == 5:
        break;
    else:
        print("Invalid Choice")

print("Thanks of Using program!!")

