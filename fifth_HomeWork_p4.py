
# 4 p -------------------------------------------------

'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу,
открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

tmp_list = []
fig_list = ['Один', 'Два', 'Три', 'Четыре']
i = 0
try:
    with open('ДЗ 4 пункт.txt', 'r') as f_rd:
        for line in f_rd:
            tmp_list = line.split()
            tmp_list[0] = fig_list[i]
            my_str = ' '.join(tmp_list)
            i += 1
            with open("ДЗ 4 пункт перезаписанный.txt", "a") as f_wr:
                print(my_str, file=f_wr)
except IOError:
    print('Ошибка ввода-вывода!')
