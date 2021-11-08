number1= int(input())
my_list = []
for _ in range(number1):
    x, y = map(int, input().split())
    my_list.append([x,y])
my_list.sort(key=lambda x: (x[1], x[0]))
for i in range(len(my_list)):
    print(my_list[i][0], my_list[i][1])
    
