class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")

class Pen(Stationery):
    def draw(self):
        print(f"{self.title}: Начинаем писать ручкой.")

class Pencil(Stationery):
    def draw(self):
        print(f"{self.title}: Рисуем карандашом.")

class Handle(Stationery):
    def draw(self):
        print(f"{self.title}: Используем маркер для отрисовки.")

# Пример использования классов
pen_instance = Pen(title="Blue Pen")
pencil_instance = Pencil(title="HB Pencil")
handle_instance = Handle(title="Red Handle")

pen_instance.draw()
pencil_instance.draw()
handle_instance.draw()