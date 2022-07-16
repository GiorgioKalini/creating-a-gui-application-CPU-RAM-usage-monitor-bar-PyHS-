import psutil as pt   # импортируем модуль psutil


class CpuBar:       # создаем класс
    def __init__(self):

        self.cpu_count = pt.cpu_count(logical=False)  # определяем колличество ядер
        self.cpu_count_logical = pt.cpu_count()       # определяем колличество потоков

