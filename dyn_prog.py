from tkinter import messagebox, Tk, Label, LEFT, RIGHT, Entry, Button, BOTTOM
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
    if (depth > len(table)):
        text = 'слишкое большое значение глубины\n максимум: ' + str(len(table))
        messagebox.showerror('Ошибка', text)
    else:
        cash = len(table)                  #находим кол-во денег, это просто высота таблицы               
        mx = max(table[cash-1])       #список вариантов размещения, изначально дбавляем произведение денег на максимальную ставку
        indexs = [0 for x in table[0]]     #искомые индексы
        indx = table[cash-1].index(max(table[cash-1]))
        indexs[indx] = cash
        cash -= 1
        incr = 0
        for t in table[:depth]:
            yet_indx = [indx]
            if not table.index(t) > max(indexs):
                for x in range(len(t)):
                    if x not in yet_indx:
                        if mx < t[x] + table[cash-1][indx] + incr:
                            cash -= 1
                            mx = t[x] + table[cash][indx] + incr
                            incr += t[x]
                            yet_indx += [x]
                            indexs[indx] -= 1
                            indexs[x] += 1
        res = 0
        for x in range(len(indexs)):
            if indexs[x] != 0:
                res += table[indexs[x]-1][x]
        out = str(indexs) + '\n' + format(res, '.2f')
        messagebox.showinfo('Результат', out)  #выводим максимальный вариант в формате с двумя цифрами после точки

#обрабатываем события
button=Button(tk,text="Посчитать",command=find_the_best)
button.pack(side=BOTTOM)
 
tk.mainloop()
