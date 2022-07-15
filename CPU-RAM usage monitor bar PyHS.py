import tkinter as tk
from tkinter import Tk, ttk  # модуль с виджетами ttk
import sys

class Application(tk.Tk):
    # создаем окно, создаем методы
    def __init__(self):
        tk.Tk.__init__(self)
        self.attributes('-alpha', 1) # прозрачность окна
        self.attributes('-topmost', True)
        self.overrideredirect(True)  # убираем рамку
        self.resizable(False, False) # нельзя менять размер (растягивать) ширину и длинну
        self.title('CPU-RAM usage monitor bar GK')  # надпись вверху на окне

        self.set_ui()

    # создаем виджеты
    def set_ui(self):
        exit_but = ttk.Button(self, text='Выход', command=self.app_exit) # создаем кнопку, привязываем команду
        exit_but.pack(fill=tk.X)  # pack-упаковщик, размещает кнопку

        self.bar2 = ttk.LabelFrame(self, text='УПРАВЛЕНИЕ') # создаем рамку (фрейм) в которую разместим виджет (кнопку)
        self.bar2.pack(fill=tk.X)
        # создаем выпадающий список
        self.combo_win = ttk.Combobox(self.bar2, values=["скрыто", "поверх", 'мини'], 
                                      width=9, state='readonly')

        self.combo_win.current(1) # выбираем то что будет по умолчанию 1 - "поверх"
        self.combo_win.pack(side=tk.LEFT)

        # создаем на фрейме кнопки и упаковываем их
        ttk.Button(self.bar2, text='двигать').pack(side=tk.LEFT)
        ttk.Button(self.bar2, text='>>>>>>>').pack(side=tk.LEFT)

        self.bar2 = ttk.LabelFrame(self, text='СИЛА') # создаем рамку (фрейм) в которую разместим прогрессбары
        self.bar2.pack(fill=tk.BOTH)

        self.bind_class('Tk', '<Enter>', self.enter_mouse) # Enter срабатывает при наведении мыши
        self.bind_class('Tk', '<Leave>', self.leave_mouse) # Leave срабатывает при убирании мыши

    def enter_mouse(self, event):  # событие которое будет происходить при наведении мыши
        if self.combo_win.current() == 0 or 1: # если выбрано "скрыто" или "поверх"
            self.geometry('')   # геометрия окна остается неизменной



    def leave_mouse(self, event):  # событие которое будет происходить при убирании мыши
        if self.combo_win.current() == 0: # если выбрано "скрыто"
            self.geometry(f'{self.winfo_width()}x1')   # раскрываем окно


    def app_exit(self): # создаем метод по которому работает кнопка 'Выход'
        self.destroy()  # закрыть окно
        sys.exit()  # дополнительно убить процесс







root = Application()
root.mainloop()
