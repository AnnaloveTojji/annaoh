#Coding Class
#Class 1
#필요한 책 안내
#Code and Hack, Let's Code!, Let's Hack!
#Code and Hack 책은 숫자 1 입니다! 기억하세요!
#Let's Code! 책은 숫자 2 입니다! 기억하세요!
#Let's Hack! 책은 숫자 2 입니다! 기억하세요!
my_list1=[x for x in range(10) if x%2==0]
print(my_list1)

my_list2=[x for x in range(10) if x%2==0]
print(my_list2)

my_list3=[x for x in range(10) if x%2==0 if x%5==0]
print(my_list3)

my_list4=["even" if i%2==0 else "odd" for i in range(10)]
print(my_list4)

fruits= ["apple","banana","cherry","kiwi","mango","orange"]
my_list5=[x for x in fruits if "a" in x]
print(my_list5)

fruits= ["apple","banana","cherry","kiwi","mango","orange"]
my_list6=[x if x!="banana" else "orange" for x in fruits]
print(my_list6)

#a 함수
a=lambda x:x*2
print(a(3))

my_list1=[1,3,2,4,3,5,6,8,9]
my_list2=list(filter(lambda x: (x%2==0), my_list1))
print(my_list2)

