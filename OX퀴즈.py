number = int(input())
my_list = []
for i in range(number):
   OX = input()
   my_list.append(OX)
for i in my_list:
   count = 0
   a = 0
   for j in i:
      if j =="O":
         a += 1
         count += a
      else:
         a = 0
   print(count)
