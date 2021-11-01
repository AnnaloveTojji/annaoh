my_list1=["Joe", "Sarah", "Mike", "Jess", "","Matt", "", "Greg"]


#Type your code here.

def name_adder(list):
    i=0
    my_list2=[]
    while i<len(list):
        if list[i]!="":
            my_list2.append(list[i])
        i=i+1
    return my_list2
print(name_adder(my_list1))
