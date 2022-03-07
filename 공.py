my_list = [1, 2, 3]
a = int(input())
for i in range(a):
    b, c = map(int, input().split())
    bi = my_list.index(b)
    ci = my_list.index(c)
    t = my_list[bi]
    my_list[bi] = my_list[ci]
    my_list[ci] = t
print(my_list[0])
