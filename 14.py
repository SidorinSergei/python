import random
import tkinter as tk
from random import randint

dict = {
'язык': 'language',
'актер': 'actor',
'берег': 'coastline',
'гречка': 'buckwheat',
'горох': 'peas',
'дверь': 'door',
'дождь': 'rain',
'стойло': 'stall',
'свинья': 'pig',
'негр': 'n****r',
'резня': 'massacre',
'шахтер': 'miner',
'элита': 'elite',
'якут': 'yakut',
'ягода': 'berry',
'байка': 'fable',
'молоко': 'milk',
'сигара': 'cigar',
'горилка': 'vodka',
'цветок': 'flower',
'юность': 'youth',
'апельсин': 'orange',
'ястреб': 'hawk',
'пить': 'drink',
'любовь': 'love',
'игра': 'game',
}

data= list(dict.items())
def task1():
    def click():
        key, value = data[randint(0, len(data) - 1)]
        word.set(key)
        word1.set(value)
        k.set(0)
    def prov():
        k.set(k.get()+1)
        if(k.get()<=3):
            if (str(entry.get()) == word1.get()):
                word2.set('Правильно!')
            else:
                word2.set('Дундук подумай хорошо!')
        else:
            word2.set('Дундук попытки закончились!')
    wind= tk.Tk()
    global k
    frame=tk.Frame(wind)
    frame.pack()
    button=tk.Button(frame, text='Сгенерировать',command=click)
    button.pack()
    word = tk.StringVar()
    word1 = tk.StringVar()
    word2 = tk.StringVar()
    lable=tk.Label(frame,textvariable=word)
    lable.pack()

    lable1 = tk.Label(frame,textvariable=word2)
    lable1.pack()
    entry = tk.Entry(frame)
    entry.pack()
    k=tk.IntVar()
    k.set(0)
    button1 = tk.Button(frame, text='Ответить', command=prov)
    button1.pack(pady=1000,padx=100)

    wind.mainloop()

task1()

