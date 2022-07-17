import tkinter as tk
from tkinter import Tk, ttk  # модуль с виджетами ttk
import sys
from process import CpuBar
from widget_update import Configure_widgets

class Application(tk.Tk, Configure_widgets): # наследуемся от Configure_widgets
    # создаем окно, создаем методы
    def __init__(self):
        tk.Tk.__init__(self)
        self.attributes('-alpha', 1) # прозрачность окна
        self.attributes('-topmost', True)
        self.overrideredirect(True)  # убираем рамку
        self.resizable(False, False) # нельзя менять размер (растягивать) ширину и длинну
        self.title('CPU-RAM usage monitor bar GK')  # надпись вверху на окне

        self.cpu = CpuBar() # создаем свойство которое будем использовать для построения графических баров
        self.set_ui()  # запускаем метод который строит базовое окно программы
        self.make_bar_cpu_usage() # запускаем метод который показывает колличество ядер и потоков
        self.configure_cpu_bar() # запускаем метод обновляющий виджеты прогрессбаров

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
        ttk.Button(self.bar2, text='двигать', command=self.configure_win).pack(side=tk.LEFT)
        ttk.Button(self.bar2, text='>>>>>>>').pack(side=tk.LEFT)

        self.bar = ttk.LabelFrame(self, text='ЗАГРУЗКА CPU') # создаем рамку (фрейм) в которую разместим прогрессбары
        self.bar.pack(fill=tk.BOTH)

        self.bind_class('Tk', '<Enter>', self.enter_mouse) # Enter срабатывает при наведении мыши
        self.bind_class('Tk', '<Leave>', self.leave_mouse) # Leave срабатывает при убирании мыши

    def make_bar_cpu_usage(self):  # создаем метод который показывает колличество ядер и потоков
        ttk.Label(self.bar, 
            text=f'Физические ядра: {self.cpu.cpu_count}, Логические потоки: {self.cpu.cpu_count_logical}', 
            anchor=tk.CENTER).pack(fill=tk.X) # размещаем текст во фрейме bar

    # размещаем прогрессбары и доп метки при помощи цикла, т.к. кол-во ядер и потоков бывает разное...
        self.list_label = [] # создаем пустые списки
        self.list_pbar = []  # 

        for i in range(self.cpu.cpu_count_logical):  # цикл сработает столько раз сколько у нас потоков
            self.list_label.append(ttk.Label(self.bar, anchor=tk.CENTER))  # размещаем в bar по центру
            self.list_pbar.append(ttk.Progressbar(self.bar, length=100)) # размещаем в bar, делится на 100 ед
        for i in range(self.cpu.cpu_count_logical):  # этим циклом упаковываем 
            self.list_label[i].pack(fill=tk.X)   
            self.list_pbar[i].pack(fill=tk.X)

            # создаем прогресбар и метку для отображения загрузки памяти
        self.ram_lab = ttk.Label(self.bar, text='', anchor=tk.CENTER) # создаем свойство для метки RAM
        self.ram_lab.pack(fill=tk.X)   # упаковываем (размещаем)
        self.ram_bar = ttk.Progressbar(self.bar, length=100)    # создаем свойство для прогресбара RAM
        self.ram_bar.pack(fill=tk.X)   # упаковываем (размещаем)

    def enter_mouse(self, event):  # событие которое будет происходить при наведении мыши
        if self.combo_win.current() == 0 or 1: # если выбрано "скрыто" или "поверх"
            self.geometry('')   # геометрия окна остается неизменной



    def leave_mouse(self, event):  # событие которое будет происходить при убирании мыши
        if self.combo_win.current() == 0: # если выбрано "скрыто"
            self.geometry(f'{self.winfo_width()}x1')   # раскрываем окно


    def app_exit(self): # создаем метод по которому работает кнопка 'Выход'
        self.destroy()  # закрыть окно
        sys.exit()  # дополнительно убить процесс






if __name__ == '__main__':
    root = Application()
    root.mainloop()
