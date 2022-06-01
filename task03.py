# Дан список чисел. Создать список в который попадают числа, 
# описывающие возрастающую последовательность и содержащие 
# максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
# Порядок элементов менять нельзя

# Функция из 1-й задачи 
def some_sequence(n,local_list): # n - с какой позиции списка начинаем искать последовательность
    if n < 0 or n > len(local_list)-1: return [] # защита от неправильного ввода
    ret = [local_list[n]]
    j = n
    for i in range(n,len(local_list)):
        if local_list[i] > local_list[j]:
            ret.append(local_list[i])
            j = i
    return ret

def some_sequence2(local_list):
    max_len = 0
    j = 0
    for i in range(len(local_list)):
        if len(some_sequence(i,local_list)) > max_len: 
            j = i
            max_len = len(some_sequence(i,local_list))
    return some_sequence(j,local_list)

my_list = [1, 5, 2, 3, 4, 6, 1, 7]
print(my_list)
print(some_sequence2(my_list))
print(some_sequence(0,my_list))
# print('=============')
# my_list = [5, 2, 3, 4, 6, 1, 7]
# print(my_list)
# print(some_sequence2(my_list))
