
# 2 p -------------------------------------------------

'''
Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке.
'''

f = open('ДЗ 2 пункт.txt', 'r')
try:
    len_f = len(f.readlines())
    f.seek(0)
    print('Количество строк в файле:', len_f)
    i = 0
    for line in f:
        i += 1
        print(f'{i}-я строка: {len(line)} Байт')
except IOError:
    print('Ошибка ввода-вывода!')
finally:
    f.close()
