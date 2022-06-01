# Вот вам файл с английскими именами. https://cloud.mail.ru/public/J7aq/iHnLspVJR
# Начните с сортировки в алфавитном порядке. Затем подсчитайте алфавитные значения 
# каждого имени и умножьте это значение на порядковый номер имени в отсортированном 
# списке для получения количества очков имени.

# Например, если список отсортирован по алфавиту, имя COLIN 
# (алфавитное значение которого 3 + 15 + 12 + 9 + 14 = 53) является 938-м в списке. 
# Поэтому, имя COLIN получает 938 × 53 = 49714 очков.

# Какова сумма очков имен в файле?
            
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
abc_cost = {alphabet[i]:i+1 for i in range(len(alphabet))}

# Вычисляем "стоимость" одного слова
def CostWord(local_str): return sum([abc_cost[local_str[i]] for i in range(len(local_str))])

# Читаем файл и суммируем произведения стоимости слов на их позицию в файле
def GetMyScores(file_name):
    with open(file_name,'r') as f:
        english_names = f.read().replace('"','').split(',') # парсинг файла
        return sum([(i+1)*CostWord(english_names[i]) for i in range(len(english_names))])
    return -1 # это если файл не открылся

print(GetMyScores('english_names.txt'))
