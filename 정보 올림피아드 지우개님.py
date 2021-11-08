#정보 올림피아드 문제
# 지우개님
number=int(input("마지막 숫자를 입력해주세요."))
my_list=[]
for i in range(1,number+1):
    my_list.append(i)
while len(my_list)!=1:
    del my_list[::2]
print(my_list[0])
