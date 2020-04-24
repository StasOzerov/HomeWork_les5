
# 5 p -------------------------------------------------

'''
Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

f = open('ДЗ 5 пункт.txt', 'a+')
while True:
    user = input('Введите числа через пробел\n(отсутствие чисел завершит программу):\n')
    print(user, file=f)
    if len(user) == 0:
        break

f.seek(0)
rezult = i = 0
for line in f:
    i += 1
    tmp_list = line.split()
    for itm in tmp_list:
        try:
            itm = float(itm)
        except ValueError:
            print("В строке", i, "обнаружено не число!")
            tmp_list.remove(itm)
    tmp_list = list(map(float, tmp_list))
    rezult += sum(tmp_list)
f.close()

print("Сумма ликвидных чисел равна:", rezult)
