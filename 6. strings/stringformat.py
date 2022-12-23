#string format by empty space holder
w="{} Welcome {}".format("hello",20)
print(w)
#string format by indexing
w="{1} Welcome {0}".format("hello",20)
print(w)
w="{1} Welcome {1}".format("hello",20)
print(w)
w="{0} Welcome {1}".format("hello",20)
print(w)
#string format by passing parameters
w="{a} Welcome {b}".format(a="hello",b=20)
print(w)
w="{b} Welcome {a}".format(a="hello",b=20)
print(w)
#this allocates size of 10 places to string
w="{b:10} Welcome {a}".format(a="hello",b=20)
print(w)
# put the value in middle of space allocated
w="{b:^10} Welcome {a:^10}".format(a="hello",b=20)
print(w)
# out the value on left side of space allocated
w="{b:<10} Welcome {a}".format(a="hello",b=20)
print(w)