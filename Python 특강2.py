#Python 특강
#2강
#선생님 오주현
#아시아 정보올림피아드
people=int(input("참가자의 수를 입력해 주세요.")) #참가자 수를 입력 받아 줍니다.
my_list1=[] #my_list1을 만들어 줍니다.
my_list2=[] #my_list2을 만들어 줍니다.
my_list3=[] #my_list3을 만들어 줍니다.
for i in range(people): #people 만큼 반복하게 해 줍니다.
    country, number, point=map(int,input("참가국, 참가번호, 점수를 입력 해 주세요.").split()) # 참가국, 참가번호, 점수를 입력 받아 주고 split을 해 줍니다.
    my_list1.append(country) #참가국을 my_list1에 모두 넣어 줍니다.
    my_list2.append(number) #참가번호를 my_list2에 모두 넣어 줍니다.
    my_list3.append(point) #점수를 my_list3에 모두 넣어 줍니다.
#my_list들이 모두 잘 들어갔는지 확인 해 봅시다.
gold=max(my_list3)
my_list3.remove(max(my_list3))
silver=max(my_list3)
print(gold)
print(silver)
