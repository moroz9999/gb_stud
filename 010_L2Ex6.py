# Lesson2, Ex.6
# -*- coding: windows-1251 -*-
n = int(input('������� ���������� ������� ��� �����:\n'))
goods = []
i = 1
while i <= n:
    title = input('������� �������� ������: ')
    price = input('������� ���� ������: ')
    q = input('������� ���������� ������ ������: ')
    unit = input('������� ������� ���������: ')
    goods.append((i, {'��������': title, '����': price, '����������': q, '��': unit}))
    print(f'����� {title} �������� � ������')
    i += 1
print(goods)
name_list, price_list, q_list, unit_list = [], [], [], []
for i in range(len(goods)):
    name_list.append(goods[i][1].get('��������'))
    price_list.append(goods[i][1].get('����'))
    q_list.append(goods[i][1].get('����������'))
    unit_list.append(goods[i][1].get('��'))
state = {'��������': name_list, '����': price_list, '����������': q_list, '��': list(set(unit_list))}
print(state)
