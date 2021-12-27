#트로피 진열
n = int(input())
my_list = []
for i in range(n):
    k = int(input())
    my_list.append(k)
max = my_list[0]
count = 1
for i in my_list:
    if i > max:
        max = i
        count += 1
print(count)
my_list.reverse()
max = my_list[0]
count = 1
for i in my_list:
    if i > max:
        max = i
        count += 1
print(count)
