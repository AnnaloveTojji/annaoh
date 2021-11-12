# -*- coding: utf-8 -*-
#1
lst1=[1,2,3,4,5]
lst2=[i for i in lst1]
print(lst2)
#2
rng=range(1200,2000,130)
lst=[i for i in rng]
print(lst)
#3
lst1=[44,54,64,74,104]
lst2=[i +6 for i  in lst1]
print(lst2)
#4
lst1=[2, 4, 6, 8, 10, 12, 14]
lst2=[i**2 for i in lst1]
print(lst2)
#5
lst1=[2, 4, 6, 8, 10, 12, 14]
lst2=[i**2 for i in lst1 if i**2>50]
print(lst2)
#6
dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
lst=[i.upper() for i in dict if dict[i]<5000]
print(lst)