# Lesson2, Ex.6
# -*- coding: windows-1251 -*-
n = int(input('Укажите количество позиций для ввода:\n'))
goods = []
i = 1
while i <= n:
    title = input('Введите название товара: ')
    price = input('Введите цену товара: ')
    q = input('Введите количество единиц товара: ')
    unit = input('Укажите единицу измерения: ')
    goods.append((i, {'название': title, 'цена': price, 'количество': q, 'ед': unit}))
    print(f'Товар {title} добавлен в список')
    i += 1
print(goods)
name_list, price_list, q_list, unit_list = [], [], [], []
for i in range(len(goods)):
    name_list.append(goods[i][1].get('название'))
    price_list.append(goods[i][1].get('цена'))
    q_list.append(goods[i][1].get('количество'))
    unit_list.append(goods[i][1].get('ед'))
state = {'название': name_list, 'цена': price_list, 'количество': q_list, 'ед': list(set(unit_list))}
print(state)
