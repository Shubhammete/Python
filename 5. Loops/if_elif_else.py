# if[condition expression]:
#     [statement to execute]
# elif[condition 2]:
#     [alternate statement to execute]
#elif[condition 3]:
#     [statement 3]
#else:
#     [statement if all conditions are false]
a=eval(input("Enter the Percentage:  "))
if a>=60:
    print(a,"First Class")
elif a>=40:
    print(a,"Second Class")
elif a>=35:
    print(a,"Third Class")
else:
    print(a,"Fail")