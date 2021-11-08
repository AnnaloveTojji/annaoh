number1= int(input())
my_list = []
for _ in range(number1):
    x, y = map(int, input().split())
    my_list.append([x,y])
my_list.sort()
for x, y in my_list:
    print(x, y)
