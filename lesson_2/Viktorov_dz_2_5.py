# 5. Создать вручную список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
# A. Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде
# <r> руб <kk> коп (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки,
# как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп
# или 00 коп).
# B. Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что
# объект списка после сортировки остался тот же).
# C. Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# D. Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по
# возрастанию, написав минимум кода?

my_list = [57.8, 46.51, 97, 61.2, 35, 99.99, 1.15, 34.5, 22, 1.1, 19.87]
prise = []
for i in my_list:
    rub = int(i)
    kop = (i - rub) * 100
    prise.append(f' {rub} руб {kop:02.0f} коп')
print(prise)
print(id(prise))
prise.sort()
print(prise)
print(id(prise))
print(sorted(prise, reverse=True))

my_list = [57.8, 46.51, 97, 61.2, 35, 99.99, 1.15, 34.5, 22, 1.1, 19.87]
prise   = []
for i in sorted(my_list)[::-1][:5]:
    rub = int(i)
    kop = (i - rub) * 100
    prise.append(f' {rub} руб {kop:02.0f} коп')
print(prise)