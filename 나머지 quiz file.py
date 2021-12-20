word_list = []
for i in range(10):
    word = int(input())
    word_list.append(word)
new_list = []
for i in word_list:
    left_over = i%42
    new_list.append(left_over)
remember_list = []
count = 0
for i in new_list:
    if not i in remember_list:
        remember_list.append(i)
        count += 1
print(count)
