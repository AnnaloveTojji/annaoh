burgur_list=[]
drink_list=[]
for i in range(3):
    burgur=int(input())
    burgur_list.append(burgur)
for i in range(2):
    drink=int(input())
    drink_list.append(drink)
cheepest_burgur=min(burgur_list)
cheepest_drink=min(drink_list)
final_value=cheepest_burgur+cheepest_drink-50
print(final_value)