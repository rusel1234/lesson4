# 
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:
# def avg(a, b):
#     if a * b >= 0:
#         return (a * b) ** 0.5
#     else:
#         raise ValueError("Невозможно определить среднее геометрическое "
#                          "введенных чисел.")
# try:
#     a = float(input("a = "))
#     b = float(input("b = "))
#     c = avg(a, b)
#     print("Среднее геометрическое = {:.2f}".format(c))
# except ValueError as err:
#     print("Ошибка:", err, ". Проверьте введенные числа.")
# except Exception as err:
#     print("Ошибка:", err)



#  Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
# import os
# try:
#     for i in range(1, 10):
#         os.mkdir("dir_" + str(i))
# except:
#     print("Already exist")
# try:
#     for i in range(1, 10):
#         os.rmdir("dir_" + str(i))
# except:
#     print("Already removed")
# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.
# import os
# list = os.listdir()
# for i in list:
#     print(i)



# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil
i = shutil.copy
print(i)





