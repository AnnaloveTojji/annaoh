#Python 특강
#2강
#선생님 오주현
number=int(input("참가하는 사람의 수를 입력해 주세요."))
my_list1=[]
for i in range(number):
     countrynumber, innumber, score=map(int,input("국가번호, 참가번호, 점수를 차례로 입력해주세요.").split())
     my_list1.append([countrynumber, innumber, score])
my_list1.sort(key=lambda x:x[2],reverse=True)
my_list2=[0]*number
counter=0
for i in my_list1:
     if counter>2:
          break
     else:
          index=i[0]
          my_list2[index]+=1
          if my_list2[index]<3:
               print(i[0],i[1])
               counter +=1
