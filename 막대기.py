#Python 연구소가 개최한 겨울 맞이 Python 특강
#막대기
number=int(input())
my_list1=[]
for i in range(number):
    heights=int(input())
    my_list1.append(heights)
my_list1.reverse()
index=my_list1.index(max(my_list1))
