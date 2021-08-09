while True:
   n=int(input("몇개의 숫자를 입력할 건가요?"))
   numbers=list(map(int,input("숫자를 모두 입력해주세요").split()))
   print(numbers)
   x=len(numbers)
   if x!=n:
      print("다시 입력해주세요.")
   else:
      break
print("a는 가장 큰 숫자이고 b는 가장 작은 숫자입니다.")
a=numbers[0]
b=numbers[0]
for j in numbers:
   if a<j:
      a=j
   if b>j:
      b=j
print("가장 큰 수가 출력됐습니다.")
print(a)
print("가장 작은 수가 출력됐습니다.")
print(b)
   
      
   
