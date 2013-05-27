from tkinter import *
#считываем данные из файла data.txt и заполняем двумерный массив table
table = [[float(i) for i in line.split()] for line in open('data.txt')]                    

#настройки интерфейса
tk = Tk()
tk.title("Динамическое программирование")
tk.geometry('300x300')
L1 = Label(tk, text="Глубина перебора")
L1.pack( side = LEFT)
E1 = Entry(tk, bd=5)
E1.insert('3',0)
E1.pack(side = RIGHT)

def find_the_best():
    depth = int(E1.get())              #"глубина" перебора
    cash = len(table)                  #находим кол-во денег, это просто высота таблицы               
    variants = [cash * max(table[-1])] #список вариантов размещения, изначально дбавляем произведение денег на максимальную ставку

    #начинаем перебирать возможные варианты в зависимости от глубины
    for k in range(depth):
        tmp = [ max(table[k])*(k+1) ]
        tmp += [ max(table[x])*(x+1) + max(table[k-x-1])*(k-x) for x in range(k//2) ]
        variants += [max(tmp) + (cash-k-1) * max(table[cash-k-2])]
    messagebox.showinfo('Результ', format(max(variants), '.2f'))  #выводим максимальный вариант в формате с двумя цифрами после точки
button=Button(tk,text="Посчитать",command=find_the_best)
button.pack(side=BOTTOM)
 
tk.mainloop()
