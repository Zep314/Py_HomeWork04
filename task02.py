# Создать и заполнить файл случайными целыми значениями. 
# Выполнить сортировку содержимого файла по возрастанию. 

from random import randint

my_filename = 'data_task02.txt'

# создаем радномное количество рандомных чисел и пишем их в файл, чтобы потом с ним работать
my_list = [randint(0,100) for _ in range(randint(0,100))]
print(my_list)
with open(my_filename,'w') as f:
    f.write("\n".join(map(str,my_list)))

# задача начинается тут
my_list = []
with open(my_filename,'r') as f:
    my_list = list(map(int, f.readlines()))
    my_list.sort()

with open(my_filename,'w') as f:
    f.write("\n".join(map(str,my_list)))
    print(my_list)





