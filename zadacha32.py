# Задача 32:
# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

list=[-4,7,0,3,-1,-3,1,5,-6,10,3,0,-9,8,10,-9,0,-6,-6,7]
min_number = int(input("Минимальный диапазон = "))
max_number = int(input("Максимальный диапазон = "))
for i in range(len(list)):
    if min_number <= list[i] <= max_number:
        print(i)