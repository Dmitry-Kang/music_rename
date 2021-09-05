import os
from tkinter import *
from tkinter import filedialog as fd

shit_prefixes = [
]

def selectDir():
    return fd.askdirectory()+'/'

def startRename(directory):
    global shit_prefixes
    global ti
    if (str(directory) == "/"):
        t2.config(state=NORMAL)
        t2.insert(ti, "--Не выбрана директория, выберите ещё раз--\n")
        ti = ti + 1
        t2.config(state=DISABLED)
        return

    # Запись на экран действий
    t2.config(state=NORMAL)
    t2.insert(ti, "--Выбрана директория " + str(directory) + "--\n")
    ti = ti + 1
    t2.config(state=DISABLED)

    shit_prefixes = str(t1.get(1.0, END)).split('\n')
    for shit in shit_prefixes:
        if len(shit) < 1:
            shit_prefixes.remove(shit)
    directory1=directory.replace('/', '\\')
    files=sorted([path for path in os.listdir(directory) if os.path.isfile(directory+path)])

    for cur_music in files:
        if (cur_music.find('.mp3') > -1):
            old_name = str(cur_music)
            name = str(cur_music)
            for prefix in shit_prefixes:
                name = str(name.replace(prefix, ""))
            name = name.replace(".mp3", "") + ".mp3"
            print(old_name + " " +  name + "\n")
            if (old_name != name):
                os.rename( directory1 + cur_music, directory1 + name)
                t2.config(state=NORMAL)
                t2.insert(ti, "--Изменено название--" + "\n")
                ti = ti + 1
                t2.insert(ti, "C " + old_name + "\n")
                ti = ti + 1
                t2.insert(ti, "На " + name + "\n")
                ti = ti + 1
                t2.config(state=DISABLED)
    t2.config(state=NORMAL)
    t2.insert(ti, "--Конец работы --\n")
    ti = ti + 1
    t2.config(state=DISABLED)


root = Tk()
root.geometry('750x250')
l1 = Label(text="Список убираемых слов")
l1.grid(row=0, column=1)
t1 = Text(width=30, height=10, bg="gray")
t1.insert(1.0, "--kissvk.com\n-kissvk.com\nkissvk.com\n[muzmo.ru]\n[ electro music ]")
t1.grid(row=1, column=1)
b1 = Button(text='Выбрать папку', command=lambda: startRename(selectDir()))
b1.grid(row=2,column=1)

l2 = Label(text="Журнал действий")
l2.grid(row=0, column=2)
t2 = Text(width=50, height=10)
ti = 2.0
t2.insert(1.0, "--ожидание ввода убираемых слов и выборе папки--\n")
t2.config(state=DISABLED)
t2.grid(row=1, column=2)

root.mainloop()