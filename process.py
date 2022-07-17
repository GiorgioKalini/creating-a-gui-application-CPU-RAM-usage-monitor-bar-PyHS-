import psutil as pt   # импортируем модуль psutil


class CpuBar:       # создаем класс
    def __init__(self):

        self.cpu_count = pt.cpu_count(logical=False)  # определяем колличество ядер
        self.cpu_count_logical = pt.cpu_count()       # определяем колличество потоков

    def cpu_percent_return(self):  # создаем метод который возвращает процент загрузки каждого ядра
        return pt.cpu_percent(percpu=True) # percpu=True - отдельно по каждому потоку

    def ram_usage(self):  # создаем метод который возвращает загруженность опер. памяти
        return pt.virtual_memory()  # возвращает кортэж с параметрами памяти


