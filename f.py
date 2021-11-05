counter=0
total=0
while counter<101:
      total=total+counter
      counter=counter+1
print(total)

my_list=[10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
counter=0
while counter<len(my_list):
      if my_list[counter]==100:
            print("There is 100 at index",counter)
      counter=counter+1

my_list=["Joe", "Sarah", "Mike", "Jess", "", "Matt", "", "Greg"]
def name_adder(list):
      newlist=[]
      counter=0
      while counter<len(list):
            if list[counter]!="":
                  newlist.append(list[counter])
            counter=counter+1
      return newlist
print(name_adder(my_list))
      
