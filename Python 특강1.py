#Python 연구소에서 개최하는 최초의 Python 특강
#1강
#안녕하세요. 저는 Python 특강 1강을 맡은 선생님 입니다.
#문제를 풀어봅시다.
#1번 문제입니다.
#가지고 있는 백준 책의 3052번 나머지를 보겠습니다.
#나머지
my_list1=[] #my_list1라는 리스트를 만들어 줍니다.
for i in range(10): #열번 반복해 줍니다.
    number=int(input("숫자 1개를 입력해주세요.")) #input을 받아 줍니다.
    my_list1.append(number) #my_list1에 모두 넣어 줍니다.
my_list2=[]
for i in my_list1: #my_list1를 모두 꺼내어 반복하게 해 줍니다.
    a=i%42 #i는 my_list1에서 꺼낸 값이고 그것을 42로 나누어 변수 a에 담아 줍니다.
    my_list2.append(a) #a를 my_list2에 넣어 줍니다.
my_set=set(my_list2)
my_setlen=len(my_set)
print(my_setlen)
