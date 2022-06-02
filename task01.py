# Дан список чисел. Создать список, в который попадают числа, 
# описываемые возрастающую последовательность. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] 
# или [1, 7] или [1, 6, 7] и т.д. 
# Порядок элементов менять нельзя


def some_sequence(n,local_list): # n - с какой позиции списка начинаем искать последовательность
    if n < 0 or n > len(local_list)-1: return [] # защита от неправильного ввода
    ret = [local_list[n]]
    j = n
    for i in range(n,len(local_list)):
        if local_list[i] > local_list[j]: # опираемся на меньший, и если текущий больше - то запоминаем его
            ret.append(local_list[i])
            j = i
    return ret

my_list = [1, 5, 2, 3, 4, 6, 1, 7]

print(my_list)
print(some_sequence(0,my_list))
print(some_sequence(6,my_list))

