#팰린드롬수
my_list = []
while True:
   number = input()
   if number == "0":
      break
   my_list.append(number)
for i in my_list:
   after = i[::-1]
   if i == after:
      print("yes")
   else:
      print("no")
   
