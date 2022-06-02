# Создать функцию, которая из списка чисел возвращает число, 
# являющее суммой двух или нескольких других элементов, либо возвращающее None, 
# если такого числа нет.
from random import randint

# Наверно можно было сделать более оптимально, но мало времени на задачу
def GetNumSumm(local_list):  # решение получилось какое-то непитоновское (((
    ret = []
    flag = False
    for i in range(len(local_list)):
        flag = False
        if not local_list[i] in ret:
            for j in range(len(local_list)-1): # последний элемент не берем
                for k in range(j+1,len(local_list)): # первый элемент не берем
                    if local_list[i] == local_list[j] + local_list[k]:
                        ret.append(local_list[i])
                        flag = True
                        break
                if flag: break # если нашли, то уже больше искать не надо
    return ret

my_list = [10, 7, 1, 9, 3, 7, 4, 6, 3, 11, 10, 11]
#my_list = [randint(1,11) for _ in range(0,10)]
print(my_list)
print(GetNumSumm(my_list))


