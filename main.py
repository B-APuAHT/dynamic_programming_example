from tkinter import *
#считываем данные из файла data.txt и заполняем двумерный массив table
table = [[float(i) for i in line.split()] for line in open('data.txt')]

depth = 5                      #"глубина" перебора
cash = len(table)              #находим кол-во денег, это просто высота таблицы               
variants = [cash * max(table[-1])] #список вариантов размещения, изначально дбавляем произведение денег на максимальную ставку

#начинаем перебирать возможные варианты в зависимости от глубины
for k in range(depth):
    tmp = [ max(table[k])*(k+1) ]
    tmp += [ max(table[x])*(x+1) + max(table[k-x-1])*(k-x) for x in range(k//2) ]
    variants += [max(tmp) + (cash-k-1) * max(table[cash-k-2])]
print(format(max(variants), '.2f'))  #печатаем максимальный вариант в формате с двумя цифрами после точки

