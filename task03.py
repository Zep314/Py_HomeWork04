# Дан список чисел. Создать список в который попадают числа, 
# описывающие возрастающую последовательность и содержащие 
# максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
# Порядок элементов менять нельзя

# # Функция из 1-й задачи 
# def some_sequence(n,local_list): # n - с какой позиции списка начинаем искать последовательность
#     if n < 0 or n > len(local_list)-1: return [] # защита от неправильного ввода
#     ret = [local_list[n]]
#     j = n
#     for i in range(n,len(local_list)):
#         if local_list[i] > local_list[j]:
#             ret.append(local_list[i])
#             j = i
#     return ret



# def some_sequence2(local_list):
#     max_len = 0
#     j = 0
#     for i in range(len(local_list)):
#         if len(some_sequence(i,local_list)) > max_len: 
#             j = i
#             max_len = len(some_sequence(i,local_list))
#     return some_sequence(j,local_list)


from math import ceil
from stat import S_IFBLK


def some_sequence2(local_list):
    L = 0  # текущий максимум длины подпоследовательности
    P = [] # индекс предшествующего символа для наидлиннейшей возрастающей подпоследовательности, оканчивающейся в i-й позиции
    M = [0 for _ in range(len(local_list)+1)] # индексы min по величине из последних элементов local_list на текущем шаге
    for i in range(0,len(local_list)): # используем бинарный поиск по массиву M
        lo = 1
        hi = L
        while lo <= hi: 
            mid = ceil((lo+hi)/2) # округление в большую сторону
            if local_list[M[mid]] < local_list[i]:
                lo = mid + 1
            else:
                hi = mid - 1
        newL = lo # индекс конечного символа

        P.append(M[newL - 1])
        M[newL] = i
        if newL > L:
            L = newL
    # готовим ответ
    S = []
    k = M[L]
    for _ in range(L,0,-1):
        S.append(local_list[k])
        k = P[k]
    S.reverse()
    return S

#my_list = [1, 5, 2, 3, 4, 6, 1, 7]
my_list = [2, 8, 5, 9, 12, 6]
print(my_list)
print(some_sequence2(my_list))

print('=============')
my_list = [5, 2, 3, 4, 6, 1, 7]
print(my_list)
print(some_sequence2(my_list))
