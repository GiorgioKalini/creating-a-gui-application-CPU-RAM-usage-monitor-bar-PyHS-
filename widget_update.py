# создаем класс который будем использовать для обновления виджетов программы.
from cgitb import text


class Configure_widgets:
    def configure_cpu_bar(self): # создаем метод с помощью которого мы сможем унаследовать этот код в наш основной класс

        r = self.cpu.cpu_percent_return() # создаем перем. r в которой хранится список с процентами загрузки
        for i in range(self.cpu.cpu_count_logical):  # чтобы цикл отработал по колл-ву потоков
            self.list_label[i].configure(text=f'Поток {i+1} используется: {r[i]}%') # конфигурируем текст метки
            self.list_pbar[i].configure(value=r[i])  # конфигурируем прогресбар

        r2 = self.cpu.ram_usage() # создаем переменную в которой хранится кортэж с параметрпми памяти
        self.ram_lab.configure(text=f'Используется памяти (RAM): {r2[2]}%, или {round(r2[3]/1048576)} Мб,\
            \nСвободно памяти (RAM): {round(r2[1]/1048576)} Мб') # конфигурируем текст метки
        self.ram_bar.configure(value=r2[2])  # конфигурируем прогресбар


        self.wheel = self.after(1000, self.configure_cpu_bar)  # метод из tkinter который будет циклически перезапускать код через заданное время
        
    def configure_win(self): # создаем метод позволяющий перетаскивать окно программы
        if self.wm_overrideredirect():  # проверяем текущее сост. окна, если с рамкой возвращает True
            self.overrideredirect(False)
        else:
            self.overrideredirect(True)
        self.update()
