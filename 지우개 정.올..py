#지우개
number1=int(input("정수 1개를 입력해."))
my_list=[]
number2=1
for i in range(number1):
     my_list.append(number2)
     nujmber2=number2
while len(my_list)!=1:
     del my_list[0::2]
