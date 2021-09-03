number=int(input("입력해"))
print("1",number)
if number<10:
    number=number*10
print("34",number)
x=list(str(number))
print("6",x)
count=0
print("8",count)
y=0
print("10",y)
while True:
##    if (int(x[0])+int(x[1]))>9:
##        y=(int(x[0])+int(x[1]))%10
##    else:
##        y=(int(x[0])+int(x[1]))
    for i in x:
        y += int(i)
    y = y%10
    print("1316",y)
    if len(x) ==1:
        y=int(x[0]*10)+y
    else:
        y=int(x[1])*10+y
    print("18",y)
    x=list(str(y))
    print("20",x)
    count=count+1
    if y == number:
        break
print(count)
