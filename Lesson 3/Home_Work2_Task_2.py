number=input("Введіть чотирьохзначне число: ")
n1=int(number[0])
n2=int(number[1])
n3=int(number[2])
n4=int(number[3])
print('Добуток: ', n1*n2*n3*n4)

reverse_num='{3}{2}{1}{0}'.format(n1,n2,n3,n4)
print('Реверсний порядок: ',reverse_num)

print("Посортований масив в порядку зростання: ",sorted(number))
