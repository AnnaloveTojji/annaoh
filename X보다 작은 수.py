#X보다 작은 수
n, x = map(int, input().split())
a = input().split()
list_a = list(a)
new_list = []
for i in list_a:
    if i < x:
        new_list.append(i)
print(new_list)
