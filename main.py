from tkinter import *
#считываем данные из файла data.txt и заполняем двумерный массив table
table = [[float(i) for i in line.split()] for line in open('data.txt')]

depth = 5
cash = len(table)               #находим кол-во денег, это просто высота таблицы
amount = cash * max(table[-1])  #находим максимальную ставку для
variants = []
for k in range(depth):
    tmp = [ max(table[k])*(k+1) ]
    tmp += [ max(table[x])*(x+1) + max(table[k-x-1])*(k-x) for x in range(k//2) ]
    variants += tmp

#favorite_index = table.index(max(tmp))
#temp_amount = 
#root = Tk()
