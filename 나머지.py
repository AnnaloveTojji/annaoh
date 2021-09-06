list1=[]
for i in range(10):
     a=int(input())
     list1.append(a)
list2=[]
for i in list1:
     b=i%42
     list2.append(b)
x=set(list2)
y=len(x)
print(y)
